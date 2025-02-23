from enum import Enum

from dacite import Config, from_dict

from . import grvt_raw_types as types
from .grvt_raw_base import GrvtApiConfig, GrvtError, GrvtRawSyncBase

# mypy: disable-error-code="no-any-return"


class GrvtRawSync(GrvtRawSyncBase):
    def __init__(self, config: GrvtApiConfig):
        super().__init__(config)
        self.md_rpc = self.env.market_data.rpc_endpoint
        self.td_rpc = self.env.trade_data.rpc_endpoint

    def get_instrument_v1(
        self, req: types.ApiGetInstrumentRequest
    ) -> types.ApiGetInstrumentResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/instrument", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiGetInstrumentResponse, resp, Config(cast=[Enum]))

    def get_all_instruments_v1(
        self, req: types.ApiGetAllInstrumentsRequest
    ) -> types.ApiGetAllInstrumentsResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/all_instruments", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiGetAllInstrumentsResponse, resp, Config(cast=[Enum]))

    def get_filtered_instruments_v1(
        self, req: types.ApiGetFilteredInstrumentsRequest
    ) -> types.ApiGetFilteredInstrumentsResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/instruments", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(
            types.ApiGetFilteredInstrumentsResponse, resp, Config(cast=[Enum])
        )

    def mini_ticker_v1(
        self, req: types.ApiMiniTickerRequest
    ) -> types.ApiMiniTickerResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/mini", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiMiniTickerResponse, resp, Config(cast=[Enum]))

    def ticker_v1(
        self, req: types.ApiTickerRequest
    ) -> types.ApiTickerResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/ticker", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiTickerResponse, resp, Config(cast=[Enum]))

    def orderbook_levels_v1(
        self, req: types.ApiOrderbookLevelsRequest
    ) -> types.ApiOrderbookLevelsResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/book", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiOrderbookLevelsResponse, resp, Config(cast=[Enum]))

    def trade_v1(self, req: types.ApiTradeRequest) -> types.ApiTradeResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/trade", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiTradeResponse, resp, Config(cast=[Enum]))

    def trade_history_v1(
        self, req: types.ApiTradeHistoryRequest
    ) -> types.ApiTradeHistoryResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/trade_history", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiTradeHistoryResponse, resp, Config(cast=[Enum]))

    def candlestick_v1(
        self, req: types.ApiCandlestickRequest
    ) -> types.ApiCandlestickResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/kline", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiCandlestickResponse, resp, Config(cast=[Enum]))

    def funding_rate_v1(
        self, req: types.ApiFundingRateRequest
    ) -> types.ApiFundingRateResponse | GrvtError:
        resp = self._post(False, self.md_rpc + "/full/v1/funding", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiFundingRateResponse, resp, Config(cast=[Enum]))

    def create_order_v1(
        self, req: types.ApiCreateOrderRequest
    ) -> types.ApiCreateOrderResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/create_order", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiCreateOrderResponse, resp, Config(cast=[Enum]))

    def cancel_order_v1(
        self, req: types.ApiCancelOrderRequest
    ) -> types.AckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/cancel_order", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.AckResponse, resp, Config(cast=[Enum]))

    def cancel_all_orders_v1(
        self, req: types.ApiCancelAllOrdersRequest
    ) -> types.AckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/cancel_all_orders", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.AckResponse, resp, Config(cast=[Enum]))

    def get_order_v1(
        self, req: types.ApiGetOrderRequest
    ) -> types.ApiGetOrderResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/order", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiGetOrderResponse, resp, Config(cast=[Enum]))

    def open_orders_v1(
        self, req: types.ApiOpenOrdersRequest
    ) -> types.ApiOpenOrdersResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/open_orders", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiOpenOrdersResponse, resp, Config(cast=[Enum]))

    def order_history_v1(
        self, req: types.ApiOrderHistoryRequest
    ) -> types.ApiOrderHistoryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/order_history", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiOrderHistoryResponse, resp, Config(cast=[Enum]))

    def pre_order_check_v1(
        self, req: types.ApiPreOrderCheckRequest
    ) -> types.ApiPreOrderCheckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/pre_order_check", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiPreOrderCheckResponse, resp, Config(cast=[Enum]))

    def cancel_trigger_order_v1(
        self, req: types.ApiCancelOrderRequest
    ) -> types.AckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/cancel_trigger_order", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.AckResponse, resp, Config(cast=[Enum]))

    def cancel_all_trigger_orders_v1(
        self, req: types.ApiCancelAllOrdersRequest
    ) -> types.AckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/cancel_all_trigger_orders", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.AckResponse, resp, Config(cast=[Enum]))

    def dedust_position_v1(
        self, req: types.ApiDedustPositionRequest
    ) -> types.ApiDedustPositionResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/dedust_position", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiDedustPositionResponse, resp, Config(cast=[Enum]))

    def fill_history_v1(
        self, req: types.ApiFillHistoryRequest
    ) -> types.ApiFillHistoryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/fill_history", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiFillHistoryResponse, resp, Config(cast=[Enum]))

    def positions_v1(
        self, req: types.ApiPositionsRequest
    ) -> types.ApiPositionsResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/positions", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiPositionsResponse, resp, Config(cast=[Enum]))

    def funding_payment_history_v1(
        self, req: types.ApiFundingPaymentHistoryRequest
    ) -> types.ApiFundingPaymentHistoryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/funding_payment_history", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(
            types.ApiFundingPaymentHistoryResponse, resp, Config(cast=[Enum])
        )

    def deposit_history_v1(
        self, req: types.ApiDepositHistoryRequest
    ) -> types.ApiDepositHistoryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/deposit_history", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiDepositHistoryResponse, resp, Config(cast=[Enum]))

    def transfer_v1(self, req: types.ApiTransferRequest) -> types.AckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/transfer", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.AckResponse, resp, Config(cast=[Enum]))

    def transfer_history_v1(
        self, req: types.ApiTransferHistoryRequest
    ) -> types.ApiTransferHistoryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/transfer_history", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiTransferHistoryResponse, resp, Config(cast=[Enum]))

    def withdrawal_v1(
        self, req: types.ApiWithdrawalRequest
    ) -> types.AckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/withdrawal", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.AckResponse, resp, Config(cast=[Enum]))

    def withdrawal_history_v1(
        self, req: types.ApiWithdrawalHistoryRequest
    ) -> types.ApiWithdrawalHistoryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/withdrawal_history", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiWithdrawalHistoryResponse, resp, Config(cast=[Enum]))

    def pre_deposit_check_v1(
        self, req: types.ApiPreDepositCheckRequest
    ) -> types.ApiPreDepositCheckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/pre_deposit_check", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiPreDepositCheckResponse, resp, Config(cast=[Enum]))

    def sub_account_summary_v1(
        self, req: types.ApiSubAccountSummaryRequest
    ) -> types.ApiSubAccountSummaryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/account_summary", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiSubAccountSummaryResponse, resp, Config(cast=[Enum]))

    def sub_account_history_v1(
        self, req: types.ApiSubAccountHistoryRequest
    ) -> types.ApiSubAccountHistoryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/account_history", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiSubAccountHistoryResponse, resp, Config(cast=[Enum]))

    def aggregated_account_summary_v1(
        self, req: types.EmptyRequest
    ) -> types.ApiAggregatedAccountSummaryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/aggregated_account_summary", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(
            types.ApiAggregatedAccountSummaryResponse, resp, Config(cast=[Enum])
        )

    def funding_account_summary_v1(
        self, req: types.EmptyRequest
    ) -> types.ApiFundingAccountSummaryResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/funding_account_summary", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(
            types.ApiFundingAccountSummaryResponse, resp, Config(cast=[Enum])
        )

    def socialized_loss_status_v1(
        self, req: types.EmptyRequest
    ) -> types.ApiSocializedLossStatusResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/socialized_loss_status", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiSocializedLossStatusResponse, resp, Config(cast=[Enum]))

    def get_all_initial_leverage_v1(
        self, req: types.ApiGetAllInitialLeverageRequest
    ) -> types.ApiGetAllInitialLeverageResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/get_all_initial_leverage", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(
            types.ApiGetAllInitialLeverageResponse, resp, Config(cast=[Enum])
        )

    def set_initial_leverage_v1(
        self, req: types.ApiSetInitialLeverageRequest
    ) -> types.ApiSetInitialLeverageResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/set_initial_leverage", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.ApiSetInitialLeverageResponse, resp, Config(cast=[Enum]))

    def cancel_on_disconnect_v1(
        self, req: types.ApiCancelOnDisconnectRequest
    ) -> types.AckResponse | GrvtError:
        resp = self._post(True, self.td_rpc + "/full/v1/cancel_on_disconnect", req)
        if resp.get("code"):
            return GrvtError(**resp)
        return from_dict(types.AckResponse, resp, Config(cast=[Enum]))
