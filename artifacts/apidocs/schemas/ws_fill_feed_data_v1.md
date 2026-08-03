!!! info "[WSFillFeedDataV1](/../../schemas/ws_fill_feed_data_v1)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|The websocket channel to which the response is sent|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A sequence number used to determine message order within a stream.<br>- If `useGlobalSequenceNumber` is **false**, this returns the gateway sequence number, which increments by one locally within each stream and resets on gateway restarts.<br>- If `useGlobalSequenceNumber` is **true**, this returns the global sequence number, which uniquely identifies messages across the cluster.<br>  - A single cluster payload can be multiplexed into multiple stream payloads.<br>  - To distinguish each stream payload, a `dedupCounter` is included.<br>  - The returned sequence number is computed as: `cluster_sequence_number * 10^5 + dedupCounter`.|
    |feed<br>`f` |Fill|True|A private trade matching the request filter|
    |prev_sequence_number<br>`ps` |string|True|The previous sequence number that determines the message order|
    ??? info "[Fill](/../../schemas/fill)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
        |sub_account_id<br>`sa` |string|True|The sub account ID that participated in the trade|
        |instrument<br>`i` |string|True|The instrument being represented|
        |is_buyer<br>`ib` |boolean|True|The side that the subaccount took on the trade|
        |is_taker<br>`it` |boolean|True|The role that the subaccount took on the trade|
        |size<br>`s` |string|True|The number of assets being traded, expressed in base asset decimal units|
        |price<br>`p` |string|True|The traded price, expressed in `9` decimals|
        |mark_price<br>`mp` |string|False<br>`None`|The mark price of the instrument at point of trade, expressed in `9` decimals|
        |index_price<br>`ip` |string|True|The index price of the instrument at point of trade, expressed in `9` decimals|
        |interest_rate<br>`ir` |string|True|The interest rate of the underlying at point of trade, expressed in centibeeps (1/100th of a basis point)|
        |forward_price<br>`fp` |string|False<br>`None`|[Options] The forward price of the option at point of trade, expressed in `9` decimals|
        |realized_pnl<br>`rp` |string|True|The realized PnL of the trade, expressed in quote asset decimal units (0 if increasing position size)|
        |fee<br>`f` |string|True|The fees paid on the trade, expressed in quote asset decimal unit (negative if maker rebate applied)|
        |fee_rate<br>`fr` |string|True|The fee rate paid on the trade|
        |trade_id<br>`ti` |string|True|A trade identifier, globally unique, and monotonically increasing (not by `1`).<br>All trades sharing a single taker execution share the same first component (before `-`), and `event_time`.<br>`trade_id` is guaranteed to be consistent across MarketData `Trade` and Trading `Fill`.|
        |order_id<br>`oi` |string|True|An order identifier|
        |venue<br>`v` |Venue|True|The venue where the trade occurred|
        |is_liquidation<br>`il` |boolean|True|If the trade was a liquidation|
        |client_order_id<br>`co` |string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
        |signer<br>`s1` |string|True|The address (public key) of the wallet signing the payload|
        |broker<br>`b` |BrokerTag|False<br>``|Specifies the broker who brokered the order|
        |is_rpi<br>`ir1` |boolean|True|If the trade is a RPI trade|
        |builder<br>`b1` |string|True|The main account ID of the builder. referred to Order.builder|
        |builder_fee_rate<br>`bf` |string|True|Builder fee percentage charged for this order. referred to Order.builder builderFee |
        |builder_fee<br>`bf1` |string|True|The builder fee paid on the trade, expressed in quote asset decimal unit. referred to Trade.builderFee|
        |fee_currency<br>`fc` |string|True|The currency of the fee paid on the trade|
        |repayment_scenario<br>`rs` |RepaymentScenario|True|If this fill was a MAM repayment/exchange, the scenario (manual / auto / liquidation); unspecified for normal trades.|
        |rfq_id<br>`ri` |string|False<br>`None`|The RFQ this fill was cleared against. Only set for RFQ venue fills; unset otherwise|
        |counterparty_type<br>`ct` |RfqCounterpartyType|False<br>`None`|The type of counterparty this fill was matched against (maker quote / resting order / forced-exit netting). Only set for RFQ venue fills; unset otherwise|
        ??? info "[Venue](/../../schemas/venue)"
            The list of Trading Venues that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`ORDERBOOK` = 1|the trade is cleared on the orderbook venue|
            |`RFQ` = 2|the trade is cleared on the RFQ venue|
        ??? info "[BrokerTag](/../../schemas/broker_tag)"
            BrokerTag is a tag for the broker that the order is sent from.<br>

            |Value| Description |
            |-|-|
            |`UNSPECIFIED` = 0||
            |`COIN_ROUTES` = 1|CoinRoutes|
            |`ALERTATRON` = 2|Alertatron|
            |`ORIGAMI` = 3|Origami|
        ??? info "[RepaymentScenario](/../../schemas/repayment_scenario)"
            Server-only fee scenario tag for spot orders that repay MAM USDT debt against the insurance fund.<br>The default value 'unspecified' means the order is NOT a repayment (regular spot fees apply).<br>Risk rejects any user-submitted order with a non-unspecified value.<br>

            |Value| Description |
            |-|-|
            |`MANUAL_REPAYMENT` = 1|User-initiated MAM repay via TDG; uses MRR (/8) divisor for fee.|
            |`AUTO_REPAYMENT` = 2|DEPRECATED — replaced by autoRepayBorrowLimit / autoRepayLTV. Kept for capnp ordinal compatibility; no producer emits this value.|
            |`LIQUIDATION_REPAYMENT` = 3|Liquidator MMR>=100% step 2 repayment; uses LRR (/2) divisor for fee.|
            |`AUTO_REPAY_BORROW_LIMIT` = 4|Liquidator borrow-limit auto-repay; uses ARR (/4) divisor for fee. Validator checks BL trigger is still active.|
            |`AUTO_REPAY_LTV` = 5|Liquidator undeployed-loan / LTV auto-repay; uses ARR (/4) divisor for fee. Validator checks LTV trigger is still active.|
        ??? info "[RfqCounterpartyType](/../../schemas/rfq_counterparty_type)"
            |Value| Description |
            |-|-|
            |`MAKER_QUOTE` = 1|the counterparty is a maker quote submitted to the RFQ|
            |`RESTING_ORDER` = 2|the counterparty is a resting order on the orderbook|
            |`FORCED_EXIT_NETTING` = 3|the counterparty is a forced-exit netting fill|
