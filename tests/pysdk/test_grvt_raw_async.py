import asyncio
import os

from artifacts.pysdk import grvt_raw_types
from artifacts.pysdk.grvt_raw_async import GrvtApiConfig, GrvtRawAsync
from artifacts.pysdk.grvt_raw_base import GrvtError
from artifacts.pysdk.grvt_raw_env import GrvtEnv


def get_config() -> GrvtApiConfig:
    conf = GrvtApiConfig(
        env=GrvtEnv(os.getenv("GRVT_ENV", "dev")),
        trading_account_id=os.getenv("GRVT_SUB_ACCOUNT_ID"),
        private_key=os.getenv("GRVT_PRIVATE_KEY"),
        api_key=os.getenv("GRVT_API_KEY"),
        logger=None,
    )
    print(conf)  # noqa: T201
    return conf


async def get_all_instruments() -> None:
    api = GrvtRawAsync(config=get_config())
    resp = await api.get_all_instruments_v1(
        grvt_raw_types.ApiGetAllInstrumentsRequest(is_active=True)
    )
    if isinstance(resp, GrvtError):
        raise ValueError(f"Received error: {resp}")
    if resp.result is None:
        raise ValueError("Expected results to be non-null")
    if len(resp.result) == 0:
        raise ValueError("Expected results to be non-empty")


async def open_orders() -> None:
    api = GrvtRawAsync(config=get_config())

    # Skip test if trading account id is not set
    if api.config.trading_account_id is None or api.config.api_key is None:
        return None  # Skip test if configs are not set

    resp = await api.open_orders_v1(
        grvt_raw_types.ApiOpenOrdersRequest(
            sub_account_id=str(api.config.trading_account_id),
            kind=[grvt_raw_types.Kind.PERPETUAL],
            base=[grvt_raw_types.Currency.BTC, grvt_raw_types.Currency.ETH],
            quote=[grvt_raw_types.Currency.USDT],
        )
    )
    if isinstance(resp, GrvtError):
        api.logger.error(f"Received error: {resp}")
        return None
    if resp.result is None:
        raise ValueError("Expected orders to be non-null")
    if len(resp.result) == 0:
        api.logger.info("Expected orders to be non-empty")


def test_get_all_instruments() -> None:
    asyncio.run(get_all_instruments())


def test_open_orders() -> None:
    asyncio.run(open_orders())
