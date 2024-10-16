!!! info "[WSOrderStateFeedDataV1](/../../schemas/ws_order_state_feed_data_v1)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|Stream name|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
    |feed<br>`f` |OrderStateFeed|True|The Order State Feed|
    ??? info "[OrderStateFeed](/../../schemas/order_state_feed)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |order_id<br>`oi` |string|True|A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
        |client_order_id<br>`co` |string|True|A unique identifier for the active order within a subaccount, specified by the client|
        |order_state<br>`os` |OrderState|True|The order state object being created or updated|
        ??? info "[OrderState](/../../schemas/order_state)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |status<br>`s` |OrderStatus|True|The status of the order|
            |reject_reason<br>`rr` |OrderRejectReason|True|The reason for rejection or cancellation|
            |book_size<br>`bs` |[string]|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
            |traded_size<br>`ts` |[string]|True|The total number of assets traded. Sorted in same order as Order.Legs|
            |update_time<br>`ut` |string|True|Time at which the order was updated by GRVT, expressed in unix nanoseconds|
            ??? info "[OrderStatus](/../../schemas/order_status)"
                |Value| Description |
                |-|-|
                |`PENDING` = 1|Order is waiting for Trigger Condition to be hit|
                |`OPEN` = 2|Order is actively matching on the orderbook, could be unfilled or partially filled|
                |`FILLED` = 3|Order is fully filled and hence closed|
                |`REJECTED` = 4|Order is rejected by GRVT Backend since if fails a particular check (See OrderRejectReason)|
                |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason)|
            ??? info "[OrderRejectReason](/../../schemas/order_reject_reason)"
                |Value| Description |
                |-|-|
                |`UNSPECIFIED` = 0|order is not cancelled or rejected|
                |`CLIENT_CANCEL` = 1|client called a Cancel API|
                |`CLIENT_BULK_CANCEL` = 2|client called a Bulk Cancel API|
                |`CLIENT_SESSION_END` = 3|client called a Session Cancel API, or set the WebSocket connection to 'cancelOrdersOnTerminate'|
                |`MARKET_CANCEL` = 4|the market order was cancelled after no/partial fill. Takes precedence over other TimeInForce cancel reasons|
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
