from . import types
from .grvt_api_base import GrvtApiAsyncBase, GrvtApiConfig, GrvtError


class GrvtApiAsync(GrvtApiAsyncBase):
    def __init__(self, config: GrvtApiConfig):
        super().__init__(config)

        self.md_rpc = self.env.market_data.rpc_endpoint
        self.td_rpc = self.env.trade_data.rpc_endpoint

    async def get_all_instruments(
        self, req: types.ApiGetAllInstrumentsRequest
    ) -> types.ApiGetAllInstrumentsResponse | GrvtError:
        resp = await self._post(False, self.md_rpc + "/full/v1/all_instruments", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return types.ApiGetAllInstrumentsResponse(**resp)

    async def get_open_orders(
        self, req: types.ApiOpenOrdersRequest
    ) -> types.ApiOpenOrdersResponse | GrvtError:
        resp = await self._post(True, self.td_rpc + "/full/v1/open_orders", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return types.ApiOpenOrdersResponse(**resp)
