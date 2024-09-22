import dataclasses
import json
import logging
import time
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from http.cookies import SimpleCookie
from typing import Any

import aiohttp
import requests  # type: ignore

from .grvt_env import GrvtEnv, GrvtEnvConfig, get_env_config


@dataclass
class GrvtApiConfig:
    env: GrvtEnv
    trading_account_id: str | None
    private_key: str | None
    api_key: str | None
    logger: logging.Logger | None


@dataclass
class GrvtError:
    code: int
    message: str
    status: int


@dataclass
class GrvtCookie:
    gravity: str
    expires: datetime


class GrvtApiBase:
    """
    GrvtApiBase is base class for Grvt Rest API classes.

    This should not be used directly, but rather through a derivative API class.
    """

    def __init__(self, config: GrvtApiConfig):
        self.config = config
        self.env: GrvtEnvConfig = get_env_config(config.env)
        self.logger: logging.Logger = config.logger or logging.getLogger(__name__)
        self._cookie: GrvtCookie | None = None
        self.logger.info(f"GrvtApiBase: {self.config=}, {self.env=}")

    """
    Cookie handling
    """

    def _should_refresh_cookie(self) -> bool:
        if not self.config.api_key:
            raise ValueError("Attempting to use Authenticated API without API key set")
        time_till_expiration = None
        if self._cookie and self._cookie.expires:
            time_till_expiration = self._cookie.expires.timestamp() - time.time()
        is_cookie_fresh = time_till_expiration is not None and time_till_expiration > 5
        if not is_cookie_fresh:
            self.logger.info(
                f"cookie should be refreshed {self._cookie=} now={time.time()}"
                f" {time_till_expiration=} secs"
            )
        return not is_cookie_fresh


class GrvtApiSyncBase(GrvtApiBase):
    def __init__(self, config: GrvtApiConfig):
        super().__init__(config)
        # Sync API session
        self._session: requests.Session = requests.Session()
        self._session.headers.update({"Content-Type": "application/json"})

    """
    Cookie handling
    """

    def _refresh_cookie(self) -> None:
        if not self._should_refresh_cookie():
            return None

        # Get cookie
        self._cookie = self._get_cookie(
            self.env.edge.rpc_endpoint, str(self.config.api_key)
        )

        # Logging
        if self._cookie:
            self.logger.info(f"refresh_cookie cookie={self._cookie}")
            self._session.cookie_jar.update_cookies({"gravity": self._cookie.gravity})
        return None

    def _get_cookie(self, path: str, api_key: str) -> GrvtCookie | None:
        FN = f"_get_cookie {path=}"
        data: dict[str, Any] = {}
        try:
            data = {"api_key": api_key}
            self.logger.info(f"{FN} ask for cookie {path=} {data=}")
            return_value = self._session.post(
                path,
                json=data,
                headers={"Content-Type": "application/json"},
            )
            self.logger.info(f"{FN} {return_value=}")
            if return_value.ok:
                cookie = SimpleCookie()
                cookie_header = return_value.headers.get("Set-Cookie")
                grvt_cookie = return_value.cookies.get("gravity")
                self.logger.info(
                    f"{FN} OK {return_value.headers=} \n "
                    f"{return_value.cookies=}\n{grvt_cookie=}\n{cookie_header=}"
                )
                cookie.load(cookie_header)
                cookie_value = cookie["gravity"].value
                cookie_expiry = datetime.strptime(
                    cookie["gravity"]["expires"],
                    "%a, %d %b %Y %H:%M:%S %Z",
                )
                return GrvtCookie(
                    gravity=cookie_value,
                    expires=cookie_expiry,
                )
            return None
        except Exception as e:
            self.logger.error(f"{FN} Error getting cookie: {e}")
            return None

    """
    Post handling
    """

    def _post(self, is_auth: bool, path: str, req: Any) -> Any:
        FN = f"_post {path=}"
        # Always see if need to referesh cookie before sending an authenticated request
        if is_auth:
            self._refresh_cookie()

        req_json = json.dumps(req, cls=DataclassJSONEncoder)
        resp_json: Any = {}

        self.logger.debug(f"{FN} {req_json=}")
        resp: requests.Response = self._session.post(path, data=req_json)
        try:
            resp_json = resp.json()
            if not resp.ok:
                self.logger.warning(f"{FN} Error {resp_json=}")
            else:
                self.logger.debug(f"{FN} OK {resp_json=}")
        except Exception as err:
            self.logger.error(f"{FN} Unable to parse {resp.text=} as json:{err=}")
        return resp_json


class GrvtApiAsyncBase(GrvtApiBase):
    def __init__(self, config: GrvtApiConfig):
        super().__init__(config)
        # Async API session
        self._session: aiohttp.ClientSession = aiohttp.ClientSession(
            headers={"Content-Type": "application/json"}
        )

    """
    Cookie handling
    """

    async def _refresh_cookie(self) -> None:
        if not self._should_refresh_cookie():
            return None

        # Get cookie
        self._cookie = await self._get_cookie(
            self.env.edge.rpc_endpoint, str(self.config.api_key)
        )

        # Logging
        if self._cookie:
            self.logger.info(f"refresh_cookie cookie={self._cookie}")
            self._session.cookie_jar.update_cookies({"gravity": self._cookie.gravity})
        return None

    async def _get_cookie(self, path: str, api_key: str) -> GrvtCookie | None:
        FN = f"_get_cookie {path=}"
        data: dict[str, Any] = {}
        try:
            data = {"api_key": api_key}
            self.logger.info(f"{FN} ask for cookie {path=} {data=}")
            async with aiohttp.ClientSession() as session:
                async with session.post(url=path, json=data) as return_value:
                    self.logger.info(f"{FN} {return_value=}")
                    if return_value.ok:
                        cookie = SimpleCookie()
                        cookie_header = return_value.headers.get("Set-Cookie")
                        grvt_cookie = return_value.cookies.get("gravity")
                        self.logger.info(
                            f"{FN} OK {return_value.headers=} \n "
                            f"{return_value.cookies=}\n{grvt_cookie=}\n{cookie_header=}"
                        )
                        cookie.load(cookie_header)
                        cookie_value = cookie["gravity"].value
                        cookie_expiry = datetime.strptime(
                            cookie["gravity"]["expires"],
                            "%a, %d %b %Y %H:%M:%S %Z",
                        )
                        return GrvtCookie(
                            gravity=cookie_value,
                            expires=cookie_expiry,
                        )
            return None
        except Exception as e:
            self.logger.error(f"{FN} Error getting cookie: {e}")
            return None

    """
    Post handling
    """

    async def _post(self, is_auth: bool, path: str, req: Any) -> Any:
        FN = f"_post {path=}"
        # Always see if need to referesh cookie before sending an authenticated request
        if is_auth:
            await self._refresh_cookie()

        req_json = json.dumps(req, cls=DataclassJSONEncoder)
        resp_json: Any = {}

        self.logger.debug(f"{FN} {req_json=}")
        resp: aiohttp.ClientResponse = await self._session.post(path, data=req_json)
        try:
            resp_json = await resp.json(content_type="application/json")
            if not resp.ok:
                self.logger.warning(f"{FN} Error {resp_json=}")
            else:
                self.logger.debug(f"{FN} OK {resp_json=}")
        except Exception as err:
            self.logger.error(f"{FN} Unable to parse {resp.text=} as json:{err=}")
        return resp_json


class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)  # type: ignore
        if isinstance(o, Enum):
            return o.value
        return super().default(o)