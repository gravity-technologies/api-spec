!!! info "[WSECNToBrokerFeedDataV1](/../../schemas/wsecn_to_broker_feed_data_v1)"
    The last-look request stream. Available only on SFP (`kind = STABLE_PERP`) instruments, and only relevant to<br>qualified market makers with ECN orders (`metadata.is_ecn = true`) — other accounts receive no traffic here.<br><br>When a taker's order matches one of your ECN orders, the matched size is held off-book and a confirmation<br>request is published on this stream. Each request identifies the ECN order by `order_id` / `client_order_id`<br>and carries a per-order monotonic `seq_no`; all sizes are cumulative over the life of the order. Respond via<br>`/ecn_from_broker` before the request's `expiry_time` (1 second): confirming the full `cumulative_request_size`<br>executes the held matches and leaves the order's remaining size live on the book; confirming less is terminal —<br>matches execute up to the confirmed size and the order's unconfirmed remainder is cancelled; silence cancels the<br>entire order (`ecnOrderExpired`). One response at the latest `seq_no` covers all earlier outstanding requests.<br>Frames that carry no new requested size (fill or shortfall updates) are informational and require no response.<br>On subscribe, the stream snapshots the most recent request per open ECN order.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|Stream name|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A sequence number used to determine message order within a stream.<br>- If `useGlobalSequenceNumber` is **false**, this returns the gateway sequence number, which increments by one locally within each stream and resets on gateway restarts.<br>- If `useGlobalSequenceNumber` is **true**, this returns the global sequence number, which uniquely identifies messages across the cluster.<br>  - A single cluster payload can be multiplexed into multiple stream payloads.<br>  - To distinguish each stream payload, a `dedupCounter` is included.<br>  - The returned sequence number is computed as: `cluster_sequence_number * 10^5 + dedupCounter`.|
    |feed<br>`f` |ECNToBrokerFeed|True|ECN to broker message|
    |prev_sequence_number<br>`ps` |string|True|The previous sequence number that determines the message order|
    ??? info "[ECNToBrokerFeed](/../../schemas/ecn_to_broker_feed)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |order_id<br>`oi` |string|True|A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
        |client_order_id<br>`co` |string|True|A unique identifier for the active order within a subaccount, specified by the client|
        |sub_account_id<br>`sa` |string|True|The subaccount initiating the order|
        |asset<br>`a` |string|True|The asset of the ECN order|
        |seq_no<br>`sn` |string|True|A sequence number used to determine message order for this ECN orders|
        |cumulative_request_size<br>`cr` |string|True|The cumulative request size for this ECN order|
        |cumulative_filled_size<br>`cf` |string|True|The cumulative filled size for this ECN order|
        |cumulative_shortfall<br>`cs` |string|True|The cumulative shortfall for this ECN order|
        |status<br>`s` |OrderStatus|True|The status of the ECN order|
        |reject_reason<br>`rr` |OrderRejectReason|True|The reason for rejection or cancellation|
        |expiry_time<br>`et` |string|True|[Filled by GRVT Backend] Time at which the ECN order will expire in unix nanoseconds|
        ??? info "[OrderStatus](/../../schemas/order_status)"
            |Value| Description |
            |-|-|
            |`PENDING` = 1|Order has been sent to the matching engine and is pending a transition to open/filled/rejected.|
            |`OPEN` = 2|Order is actively matching on the matching engine, could be unfilled or partially filled.|
            |`FILLED` = 3|Order is fully filled and hence closed. Taker Orders can transition directly from pending to filled, without going through open.|
            |`REJECTED` = 4|Order is rejected by matching engine since if fails a particular check (See OrderRejectReason). Once an order is open, it cannot be rejected.|
            |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason). Before an order is open, it cannot be cancelled.|
        ??? info "[OrderRejectReason](/../../schemas/order_reject_reason)"
            |Value| Description |
            |-|-|
            |`UNSPECIFIED` = 0|order is not cancelled or rejected|
            |`CLIENT_CANCEL` = 1|client called a Cancel API|
            |`CLIENT_BULK_CANCEL` = 2|client called a Bulk Cancel API|
            |`CLIENT_SESSION_END` = 3|client called a Session Cancel API, or set the WebSocket connection to 'cancelOrdersOnTerminate'|
            |`MARKET_CANCEL` = 4|the market order was cancelled after no/partial fill. Lower precedence than other TimeInForce cancel reasons|
            |`IOC_CANCEL` = 5|the IOC order was cancelled after no/partial fill|
            |`AON_CANCEL` = 6|the AON order was cancelled as it could not be fully matched|
            |`FOK_CANCEL` = 7|the FOK order was cancelled as it could not be fully matched|
            |`EXPIRED` = 8|the order was cancelled as it has expired|
            |`FAIL_POST_ONLY` = 9|the post-only order could not be posted into the orderbook|
            |`FAIL_REDUCE_ONLY` = 10|the reduce-only order would have caused position size to increase|
            |`MM_PROTECTION` = 11|the order was cancelled due to market maker protection trigger|
            |`SELF_TRADE_PROTECTION` = 12|the order was cancelled due to self-trade protection trigger|
            |`SELF_MATCHED_SUBACCOUNT` = 13|the order matched with another order from the same sub account|
            |`OVERLAPPING_CLIENT_ORDER_ID` = 14|an active order on your sub account shares the same clientOrderId|
            |`BELOW_MARGIN` = 15|the order will bring the sub account below initial margin requirement|
            |`LIQUIDATION` = 16|the sub account is liquidated (and all open orders are cancelled by Gravity)|
            |`INSTRUMENT_INVALID` = 17|instrument is invalid or not found on Gravity|
            |`INSTRUMENT_DEACTIVATED` = 18|instrument is no longer tradable on Gravity. (typically due to a market halt, or instrument expiry)|
            |`SYSTEM_FAILOVER` = 19|system failover resulting in loss of order state|
            |`UNAUTHORISED` = 20|the credentials used (userSession/apiKeySession/walletSignature) is not authorised to perform the action|
            |`SESSION_KEY_EXPIRED` = 21|the session key used to sign the order expired|
            |`SUB_ACCOUNT_NOT_FOUND` = 22|the subaccount does not exist|
            |`NO_TRADE_PERMISSION` = 23|the signature used to sign the order has no trade permission|
            |`UNSUPPORTED_TIME_IN_FORCE` = 24|the order payload does not contain a supported TimeInForce value|
            |`MULTI_LEGGED_ORDER` = 25|the order has multiple legs, but multiple legs are not supported by this venue|
            |`EXCEED_MAX_POSITION_SIZE` = 26|the order would have caused the subaccount to exceed the max position size|
            |`EXCEED_MAX_SIGNATURE_EXPIRATION` = 27|the signature supplied is more than 30 days in the future|
            |`MARKET_ORDER_WITH_LIMIT_PRICE` = 28|the market order has a limit price set|
            |`CLIENT_CANCEL_ON_DISCONNECT_TRIGGERED` = 29|client cancel on disconnect triggered|
            |`OCO_COUNTER_PART_TRIGGERED` = 30|the OCO counter part order was triggered|
            |`REDUCE_ONLY_LIMIT` = 31|the remaining order size was cancelled because it exceeded current position size|
            |`CLIENT_REPLACE` = 32|the order was replaced by a client replace request|
            |`DERISK_MUST_BE_IOC` = 33|the derisk order must be an IOC order|
            |`DERISK_MUST_BE_REDUCE_ONLY` = 34|the derisk order must be a reduce-only order|
            |`DERISK_NOT_SUPPORTED` = 35|derisk is not supported|
            |`INVALID_ORDER_TYPE` = 36|the order type is invalid|
            |`CURRENCY_NOT_DEFINED` = 37|the currency is not defined|
            |`INVALID_CHAIN_ID` = 38|the chain ID is invalid|
            |`BUILDER_ORDER_FEE_EXCEED` = 39|Builder fee exceed the limit|
            |`BUILDER_ORDER_FEE_NEGATIVE` = 40|Builder fee is below 0|
            |`BUILDER_ORDER_BUILDER_NOT_AUTHORIZED` = 41|Builder is not an authorized builder for client|
            |`BUILDER_ORDER_BUILDER_NOT_EXIST` = 42|Builder does not exist|
            |`TRADE_PRICE_WORSE_THAN_BANKRUPTCY_PRICE` = 44|the trade price is worse than the bankruptcy price|
            |`TOO_MANY_MAKER_ORDERS` = 45|the order was cancelled due to matching with too many maker orders|
            |`REDUCE_ONLY_NOT_SUPPORTED_FOR_SPOT_ORDER` = 46|reduce-only order is not supported for spot order|
            |`TPSL_NOT_SUPPORTED_FOR_SPOT_ORDER` = 47|tpsl is not supported for spot order|
            |`SPOT_ORDER_NOT_SUPPORTED` = 48|spot order is not supported|
            |`INSUFFICIENT_BALANCE` = 49|the subaccount has insufficient balance|
            |`SPOT_TRADING_BLOCKED_DURING_SOCIALIZED_LOSS` = 50|spot trading is blocked during socialized loss (SLOW)|
            |`BELOW_MARGIN_WITH_PENALTY_DEVIATION` = 51|the order will bring the sub account below initial margin requirement considering wide price deviation|
            |`CORPORATE_ACTION` = 56|Cancelled by the system due to Corporate Action|
            |`NOT_QUALIFIED_MAKER` = 57|the order was rejected because the sub account is not a qualified maker|
            |`PRIVATE_QUOTE_REQUIRES_RFQ` = 58|rfq_id is required when is_private = true|
            |`STABLE_PERP_REQUIRES_PRICE_BOUND` = 59|a signed slippage bound filled in limit_price is required|
            |`UNSUPPORTED_TRIGGER_BY` = 60|SFP order only supports trigger_by = index|
            |`RFQ_NOT_FOUND` = 61|the order was rejected because the referenced RFQ could not be found|
            |`RESTING_ORDER_WOULD_CROSS` = 62|post-only resting placement crosses opposite best resting or index mid|
            |`SESSION_CLOSED` = 63|the order was submitted when the trading session was either closed or under maintenance|
