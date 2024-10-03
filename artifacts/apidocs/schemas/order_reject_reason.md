!!! info "[OrderRejectReason](schemas/order_reject_reason.md)"
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