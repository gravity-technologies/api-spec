# Trading APIs
All requests should be made using the `POST` HTTP method.

## Order
### Create Order
```
FULL ENDPOINT: full/v1/create_order
LITE ENDPOINT: lite/v1/create_order
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiCreateOrderRequest"
        Create an order on the orderbook for this trading account.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |order|o|Order|True|The order to create|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br><br>All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|False|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|False|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |post_only|po|boolean|False|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|False|If True, Order must reduce the position size, or be cancelled|
            |legs|l|[OrderLeg]|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|False|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
            ??? info "TimeInForce"
                |                       | Must Fill All | Can Fill Partial |
                | -                     | -             | -                |
                | Must Fill Immediately | FOK           | IOC              |
                | Can Fill Till Time    | AON           | GTC              |
                <br>

                |Value| Description |
                |-|-|
                |`GOOD_TILL_TIME` = 1|GTT - Remains open until it is cancelled, or expired|
                |`ALL_OR_NONE` = 2|AON - Either fill the whole order or none of it (Block Trades Only)|
                |`IMMEDIATE_OR_CANCEL` = 3|IOC - Fill the order as much as possible, when hitting the orderbook. Then cancel it|
                |`FILL_OR_KILL` = 4|FOK - Both AoN and IoC. Either fill the full order when hitting the orderbook, or cancel it|
            ??? info "OrderLeg"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |instrument|i|string|True|The instrument to trade in this leg|
                |size|s|string|True|The total number of assets to trade in this leg, expressed in underlying asset decimal units.|
                |limit_price|lp|string|False|The limit price of the order leg, expressed in `9` decimals.<br>This is the number of quote currency units to pay/receive for this leg.<br>This should be `null/0` if the order is a market order|
                |is_buying_asset|ib|boolean|True|Specifies if the order leg is a buy or sell|
            ??? info "Signature"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |signer|s|string|True|The address (public key) of the wallet signing the payload|
                |r|r|string|True|Signature R|
                |s|s1|string|True|Signature S|
                |v|v|number|True|Signature V|
                |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
            ??? info "OrderMetadata"
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|False|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|[string]|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|[string]|True|The total number of assets traded. Sorted in same order as Order.Legs|
                |update_time|ut|string|True|Time at which the order was updated by GRVT, expressed in unix nanoseconds|
                ??? info "OrderStatus"
                    |Value| Description |
                    |-|-|
                    |`PENDING` = 1|Order is waiting for Trigger Condition to be hit|
                    |`OPEN` = 2|Order is actively matching on the orderbook, could be unfilled or partially filled|
                    |`FILLED` = 3|Order is fully filled and hence closed|
                    |`REJECTED` = 4|Order is rejected by GRVT Backend since if fails a particular check (See OrderRejectReason)|
                    |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason)|
                ??? info "OrderRejectReason"
                    |Value| Description |
                    |-|-|
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "order": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }
        }
        ```
        ```json
        {
            "o": {
                "oi": "0x1234567890abcdef",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "im": false,
                "ti": "GOOD_TILL_TIME",
                "po": false,
                "ro": false,
                "l": [{
                    "i": "BTC_USDT_Perp",
                    "s": "10.5",
                    "lp": "65038.01",
                    "ib": true
                }],
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "e": "1697788800000000000",
                    "n": "1234567890"
                },
                "m": {
                    "co": "23042",
                    "ct": "1697788800000000000"
                },
                "s1": {
                    "s": "PENDING",
                    "rr": "CLIENT_CANCEL",
                    "bs": ["3.0", "6.0"],
                    "ts": ["3.0", "6.0"],
                    "ut": "1697788800000000000"
                }
            }
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiCreateOrderResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |order|o|Order|True|The created order|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br><br>All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|False|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|False|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |post_only|po|boolean|False|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|False|If True, Order must reduce the position size, or be cancelled|
            |legs|l|[OrderLeg]|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|False|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
            ??? info "TimeInForce"
                |                       | Must Fill All | Can Fill Partial |
                | -                     | -             | -                |
                | Must Fill Immediately | FOK           | IOC              |
                | Can Fill Till Time    | AON           | GTC              |
                <br>

                |Value| Description |
                |-|-|
                |`GOOD_TILL_TIME` = 1|GTT - Remains open until it is cancelled, or expired|
                |`ALL_OR_NONE` = 2|AON - Either fill the whole order or none of it (Block Trades Only)|
                |`IMMEDIATE_OR_CANCEL` = 3|IOC - Fill the order as much as possible, when hitting the orderbook. Then cancel it|
                |`FILL_OR_KILL` = 4|FOK - Both AoN and IoC. Either fill the full order when hitting the orderbook, or cancel it|
            ??? info "OrderLeg"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |instrument|i|string|True|The instrument to trade in this leg|
                |size|s|string|True|The total number of assets to trade in this leg, expressed in underlying asset decimal units.|
                |limit_price|lp|string|False|The limit price of the order leg, expressed in `9` decimals.<br>This is the number of quote currency units to pay/receive for this leg.<br>This should be `null/0` if the order is a market order|
                |is_buying_asset|ib|boolean|True|Specifies if the order leg is a buy or sell|
            ??? info "Signature"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |signer|s|string|True|The address (public key) of the wallet signing the payload|
                |r|r|string|True|Signature R|
                |s|s1|string|True|Signature S|
                |v|v|number|True|Signature V|
                |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
            ??? info "OrderMetadata"
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|False|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|[string]|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|[string]|True|The total number of assets traded. Sorted in same order as Order.Legs|
                |update_time|ut|string|True|Time at which the order was updated by GRVT, expressed in unix nanoseconds|
                ??? info "OrderStatus"
                    |Value| Description |
                    |-|-|
                    |`PENDING` = 1|Order is waiting for Trigger Condition to be hit|
                    |`OPEN` = 2|Order is actively matching on the orderbook, could be unfilled or partially filled|
                    |`FILLED` = 3|Order is fully filled and hence closed|
                    |`REJECTED` = 4|Order is rejected by GRVT Backend since if fails a particular check (See OrderRejectReason)|
                    |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason)|
                ??? info "OrderRejectReason"
                    |Value| Description |
                    |-|-|
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "order": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You are not authorized to access this functionality|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1003|404|Data Not Found|
        |1004|401|Logged in user does not match the sub account|
        |1005|500|Unknown Error|
        |2001|401|Order signature is from an unauthorized signer|
        |2002|401|Order signature has expired|
        |2003|401|Order signature does not match payload|
        |2004|401|Order sub account does not match logged in user|
        |2005|400|Order ID should be empty when creating an order|
        |2006|400|Client Order ID should be supplied when creating an order|
        |2007|400|Client Order ID overlaps with existing active order|
        |2010|400|Orderbook Orders must have a TimeInForce of GTT/IOC/FOK|
        |2011|400|RFQ Orders must have a TimeInForce of GTT/AON/IOC/FOK|
        |2012|400|Post Only can only be set to true for GTT/AON orders|
        |2013|400|Market Order must always be supplied without a limit price|
        |2014|400|Limit Order must always be supplied with a limit price|
        |2016|400|Order must contain at least one leg|
        |2017|400|Order Legs must be sorted by Derivative.Instrument/Underlying/BaseCurrency/Expiration/StrikePrice|
        |2018|400|Orderbook Orders must contain only one leg|
        |2019|400|Order state must be empty upon creation|
        |2020|400|Order execution metadata must be empty upon creation|
        |2021|400|Order Legs contain one or more inactive derivative|
        |2022|400|Unsupported Instrument Requested|
        |2023|400|Order size smaller than min size|
        |2024|400|Order size smaller than min block size in block trade venue|
        |2025|400|Invalid limit price tick|
        |2026|400|Liquidation Order is not supported|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1003,
            "message":"Data Not Found",
            "status":404
        }
        {
            "code":1004,
            "message":"Logged in user does not match the sub account",
            "status":401
        }
        {
            "code":1005,
            "message":"Unknown Error",
            "status":500
        }
        {
            "code":2001,
            "message":"Order signature is from an unauthorized signer",
            "status":401
        }
        {
            "code":2002,
            "message":"Order signature has expired",
            "status":401
        }
        {
            "code":2003,
            "message":"Order signature does not match payload",
            "status":401
        }
        {
            "code":2004,
            "message":"Order sub account does not match logged in user",
            "status":401
        }
        {
            "code":2005,
            "message":"Order ID should be empty when creating an order",
            "status":400
        }
        {
            "code":2006,
            "message":"Client Order ID should be supplied when creating an order",
            "status":400
        }
        {
            "code":2007,
            "message":"Client Order ID overlaps with existing active order",
            "status":400
        }
        {
            "code":2010,
            "message":"Orderbook Orders must have a TimeInForce of GTT/IOC/FOK",
            "status":400
        }
        {
            "code":2011,
            "message":"RFQ Orders must have a TimeInForce of GTT/AON/IOC/FOK",
            "status":400
        }
        {
            "code":2012,
            "message":"Post Only can only be set to true for GTT/AON orders",
            "status":400
        }
        {
            "code":2013,
            "message":"Market Order must always be supplied without a limit price",
            "status":400
        }
        {
            "code":2014,
            "message":"Limit Order must always be supplied with a limit price",
            "status":400
        }
        {
            "code":2016,
            "message":"Order must contain at least one leg",
            "status":400
        }
        {
            "code":2017,
            "message":"Order Legs must be sorted by Derivative.Instrument/Underlying/BaseCurrency/Expiration/StrikePrice",
            "status":400
        }
        {
            "code":2018,
            "message":"Orderbook Orders must contain only one leg",
            "status":400
        }
        {
            "code":2019,
            "message":"Order state must be empty upon creation",
            "status":400
        }
        {
            "code":2020,
            "message":"Order execution metadata must be empty upon creation",
            "status":400
        }
        {
            "code":2021,
            "message":"Order Legs contain one or more inactive derivative",
            "status":400
        }
        {
            "code":2022,
            "message":"Unsupported Instrument Requested",
            "status":400
        }
        {
            "code":2023,
            "message":"Order size smaller than min size",
            "status":400
        }
        {
            "code":2024,
            "message":"Order size smaller than min block size in block trade venue",
            "status":400
        }
        {
            "code":2025,
            "message":"Invalid limit price tick",
            "status":400
        }
        {
            "code":2026,
            "message":"Liquidation Order is not supported",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/create_order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "order": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/create_order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "order": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/create_order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "order": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/create_order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "order": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }
        }
        '
        ```
<hr class="solid">
### Cancel Order
```
FULL ENDPOINT: full/v1/cancel_order
LITE ENDPOINT: lite/v1/cancel_order
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiCancelOrderRequest"
        Cancel an order on the orderbook for this trading account. Either `order_id` or `client_order_id` must be provided.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID cancelling the order|
        |order_id|oi|string|False|Cancel the order with this `order_id`|
        |client_order_id|co|string|False|Cancel the order with this `client_order_id`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "oi": "0x1028403",
            "co": "23042"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "AckResponse"
        Used to acknowledge a request has been received and will be processed<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |acknowledgement|a|boolean|True|Gravity has acknowledged that the request has been successfully received and it will process it in the backend|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "acknowledgement": "true"
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/cancel_order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/cancel_order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/cancel_order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/cancel_order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
<hr class="solid">
### Cancel All Orders
```
FULL ENDPOINT: full/v1/cancel_all_orders
LITE ENDPOINT: lite/v1/cancel_all_orders
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiCancelAllOrdersRequest"
        Cancel all orders on the orderbook for this trading account. This may not match new orders in flight.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID cancelling all orders|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "AckResponse"
        Used to acknowledge a request has been received and will be processed<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |acknowledgement|a|boolean|True|Gravity has acknowledged that the request has been successfully received and it will process it in the backend|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "acknowledgement": "true"
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |2004|401|Order sub account does not match logged in user|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":2004,
            "message":"Order sub account does not match logged in user",
            "status":401
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/cancel_all_orders' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/cancel_all_orders' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/cancel_all_orders' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/cancel_all_orders' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        '
        ```
<hr class="solid">
### Get Order
```
FULL ENDPOINT: full/v1/order
LITE ENDPOINT: lite/v1/order
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetOrderRequest"
        Retrieve the order for the account. Either `order_id` or `client_order_id` must be provided.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
        |order_id|oi|string|False|Filter for `order_id`|
        |client_order_id|co|string|False|Filter for `client_order_id`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "oi": "0x1028403",
            "co": "23042"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetOrderResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |order|o|Order|True|The order object for the requested filter|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br><br>All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|False|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|False|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |post_only|po|boolean|False|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|False|If True, Order must reduce the position size, or be cancelled|
            |legs|l|[OrderLeg]|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|False|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
            ??? info "TimeInForce"
                |                       | Must Fill All | Can Fill Partial |
                | -                     | -             | -                |
                | Must Fill Immediately | FOK           | IOC              |
                | Can Fill Till Time    | AON           | GTC              |
                <br>

                |Value| Description |
                |-|-|
                |`GOOD_TILL_TIME` = 1|GTT - Remains open until it is cancelled, or expired|
                |`ALL_OR_NONE` = 2|AON - Either fill the whole order or none of it (Block Trades Only)|
                |`IMMEDIATE_OR_CANCEL` = 3|IOC - Fill the order as much as possible, when hitting the orderbook. Then cancel it|
                |`FILL_OR_KILL` = 4|FOK - Both AoN and IoC. Either fill the full order when hitting the orderbook, or cancel it|
            ??? info "OrderLeg"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |instrument|i|string|True|The instrument to trade in this leg|
                |size|s|string|True|The total number of assets to trade in this leg, expressed in underlying asset decimal units.|
                |limit_price|lp|string|False|The limit price of the order leg, expressed in `9` decimals.<br>This is the number of quote currency units to pay/receive for this leg.<br>This should be `null/0` if the order is a market order|
                |is_buying_asset|ib|boolean|True|Specifies if the order leg is a buy or sell|
            ??? info "Signature"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |signer|s|string|True|The address (public key) of the wallet signing the payload|
                |r|r|string|True|Signature R|
                |s|s1|string|True|Signature S|
                |v|v|number|True|Signature V|
                |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
            ??? info "OrderMetadata"
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|False|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|[string]|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|[string]|True|The total number of assets traded. Sorted in same order as Order.Legs|
                |update_time|ut|string|True|Time at which the order was updated by GRVT, expressed in unix nanoseconds|
                ??? info "OrderStatus"
                    |Value| Description |
                    |-|-|
                    |`PENDING` = 1|Order is waiting for Trigger Condition to be hit|
                    |`OPEN` = 2|Order is actively matching on the orderbook, could be unfilled or partially filled|
                    |`FILLED` = 3|Order is fully filled and hence closed|
                    |`REJECTED` = 4|Order is rejected by GRVT Backend since if fails a particular check (See OrderRejectReason)|
                    |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason)|
                ??? info "OrderRejectReason"
                    |Value| Description |
                    |-|-|
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "order": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1003|404|Data Not Found|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1003,
            "message":"Data Not Found",
            "status":404
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/order' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
<hr class="solid">
### Open Orders
```
FULL ENDPOINT: full/v1/open_orders
LITE ENDPOINT: lite/v1/open_orders
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiOpenOrdersRequest"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
        |kind|k|[Kind]|True|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|[Currency]|True|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|[Currency]|True|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
        ??? info "Kind"
            The list of asset kinds that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`PERPETUAL` = 1|the perpetual asset kind|
            |`FUTURE` = 2|the future asset kind|
            |`CALL` = 3|the call option asset kind|
            |`PUT` = 4|the put option asset kind|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "u": ["BTC", "ETH"],
            "q": ["USDT", "USDC"]
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiOpenOrdersResponse"
        Retrieves all open orders for the account. This may not match new orders in flight.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |orders|o|[Order]|True|The Open Orders matching the request filter|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br><br>All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|False|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|False|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |post_only|po|boolean|False|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|False|If True, Order must reduce the position size, or be cancelled|
            |legs|l|[OrderLeg]|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|False|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
            ??? info "TimeInForce"
                |                       | Must Fill All | Can Fill Partial |
                | -                     | -             | -                |
                | Must Fill Immediately | FOK           | IOC              |
                | Can Fill Till Time    | AON           | GTC              |
                <br>

                |Value| Description |
                |-|-|
                |`GOOD_TILL_TIME` = 1|GTT - Remains open until it is cancelled, or expired|
                |`ALL_OR_NONE` = 2|AON - Either fill the whole order or none of it (Block Trades Only)|
                |`IMMEDIATE_OR_CANCEL` = 3|IOC - Fill the order as much as possible, when hitting the orderbook. Then cancel it|
                |`FILL_OR_KILL` = 4|FOK - Both AoN and IoC. Either fill the full order when hitting the orderbook, or cancel it|
            ??? info "OrderLeg"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |instrument|i|string|True|The instrument to trade in this leg|
                |size|s|string|True|The total number of assets to trade in this leg, expressed in underlying asset decimal units.|
                |limit_price|lp|string|False|The limit price of the order leg, expressed in `9` decimals.<br>This is the number of quote currency units to pay/receive for this leg.<br>This should be `null/0` if the order is a market order|
                |is_buying_asset|ib|boolean|True|Specifies if the order leg is a buy or sell|
            ??? info "Signature"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |signer|s|string|True|The address (public key) of the wallet signing the payload|
                |r|r|string|True|Signature R|
                |s|s1|string|True|Signature S|
                |v|v|number|True|Signature V|
                |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
            ??? info "OrderMetadata"
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|False|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|[string]|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|[string]|True|The total number of assets traded. Sorted in same order as Order.Legs|
                |update_time|ut|string|True|Time at which the order was updated by GRVT, expressed in unix nanoseconds|
                ??? info "OrderStatus"
                    |Value| Description |
                    |-|-|
                    |`PENDING` = 1|Order is waiting for Trigger Condition to be hit|
                    |`OPEN` = 2|Order is actively matching on the orderbook, could be unfilled or partially filled|
                    |`FILLED` = 3|Order is fully filled and hence closed|
                    |`REJECTED` = 4|Order is rejected by GRVT Backend since if fails a particular check (See OrderRejectReason)|
                    |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason)|
                ??? info "OrderRejectReason"
                    |Value| Description |
                    |-|-|
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "orders": [{
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }]
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/open_orders' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/open_orders' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/open_orders' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/open_orders' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
<hr class="solid">
### Order History
```
FULL ENDPOINT: full/v1/order_history
LITE ENDPOINT: lite/v1/order_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiOrderHistoryRequest"
        Retrieves the order history for the account.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
        |kind|k|[Kind]|True|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|[Currency]|True|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|[Currency]|True|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
        |start_time|st|string|False|The start time to apply in nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned|
        |end_time|et|string|False|The end time to apply in nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the query from|
        ??? info "Kind"
            The list of asset kinds that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`PERPETUAL` = 1|the perpetual asset kind|
            |`FUTURE` = 2|the future asset kind|
            |`CALL` = 3|the call option asset kind|
            |`PUT` = 4|the put option asset kind|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "u": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "st": 1697788800000000000,
            "et": 1697788800000000000,
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiOrderHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |orders|o|[Order]|True|The Open Orders matching the request filter|
        |next|n|string|True|The cursor to indicate when to start the query from|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br><br>All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|False|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|False|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |post_only|po|boolean|False|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|False|If True, Order must reduce the position size, or be cancelled|
            |legs|l|[OrderLeg]|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|False|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
            ??? info "TimeInForce"
                |                       | Must Fill All | Can Fill Partial |
                | -                     | -             | -                |
                | Must Fill Immediately | FOK           | IOC              |
                | Can Fill Till Time    | AON           | GTC              |
                <br>

                |Value| Description |
                |-|-|
                |`GOOD_TILL_TIME` = 1|GTT - Remains open until it is cancelled, or expired|
                |`ALL_OR_NONE` = 2|AON - Either fill the whole order or none of it (Block Trades Only)|
                |`IMMEDIATE_OR_CANCEL` = 3|IOC - Fill the order as much as possible, when hitting the orderbook. Then cancel it|
                |`FILL_OR_KILL` = 4|FOK - Both AoN and IoC. Either fill the full order when hitting the orderbook, or cancel it|
            ??? info "OrderLeg"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |instrument|i|string|True|The instrument to trade in this leg|
                |size|s|string|True|The total number of assets to trade in this leg, expressed in underlying asset decimal units.|
                |limit_price|lp|string|False|The limit price of the order leg, expressed in `9` decimals.<br>This is the number of quote currency units to pay/receive for this leg.<br>This should be `null/0` if the order is a market order|
                |is_buying_asset|ib|boolean|True|Specifies if the order leg is a buy or sell|
            ??? info "Signature"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |signer|s|string|True|The address (public key) of the wallet signing the payload|
                |r|r|string|True|Signature R|
                |s|s1|string|True|Signature S|
                |v|v|number|True|Signature V|
                |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
            ??? info "OrderMetadata"
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|False|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|[string]|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|[string]|True|The total number of assets traded. Sorted in same order as Order.Legs|
                |update_time|ut|string|True|Time at which the order was updated by GRVT, expressed in unix nanoseconds|
                ??? info "OrderStatus"
                    |Value| Description |
                    |-|-|
                    |`PENDING` = 1|Order is waiting for Trigger Condition to be hit|
                    |`OPEN` = 2|Order is actively matching on the orderbook, could be unfilled or partially filled|
                    |`FILLED` = 3|Order is fully filled and hence closed|
                    |`REJECTED` = 4|Order is rejected by GRVT Backend since if fails a particular check (See OrderRejectReason)|
                    |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason)|
                ??? info "OrderRejectReason"
                    |Value| Description |
                    |-|-|
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "orders": [{
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["3.0", "6.0"],
                    "traded_size": ["3.0", "6.0"],
                    "update_time": "1697788800000000000"
                }
            }],
            "next": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/order_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/order_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/order_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/order_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
## Trade
### Private Trade History
```
FULL ENDPOINT: full/v1/trade_history
LITE ENDPOINT: lite/v1/trade_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPrivateTradeHistoryRequest"
        Query for all historical trades made by a single account. A single order can be matched multiple times, hence there is no real way to uniquely identify a trade.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The sub account ID to request for|
        |kind|k|[Kind]|True|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|[Currency]|True|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|[Currency]|True|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
        |start_time|st|string|False|The start time to apply in unix nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned|
        |end_time|et|string|False|The end time to apply in unix nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the query from|
        ??? info "Kind"
            The list of asset kinds that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`PERPETUAL` = 1|the perpetual asset kind|
            |`FUTURE` = 2|the future asset kind|
            |`CALL` = 3|the call option asset kind|
            |`PUT` = 4|the put option asset kind|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "u": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "st": 1697788800000000000,
            "et": 1697788800000000000,
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPrivateTradeHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[PrivateTrade]|True|The private trades matching the request asset|
        |next|n|string|True|The cursor to indicate when to start the query from|
        ??? info "PrivateTrade"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |sub_account_id|sa|string|True|The sub account ID that participated in the trade|
            |instrument|i|string|True|The instrument being represented|
            |is_buyer|ib|boolean|True|The side that the subaccount took on the trade|
            |is_taker|it|boolean|True|The role that the subaccount took on the trade|
            |size|s|string|True|The number of assets being traded, expressed in underlying asset decimal units|
            |price|p|string|True|The traded price, expressed in `9` decimals|
            |mark_price|mp|string|True|The mark price of the instrument at point of trade, expressed in `9` decimals|
            |index_price|ip|string|True|The index price of the instrument at point of trade, expressed in `9` decimals|
            |interest_rate|ir|string|True|The interest rate of the underlying at point of trade, expressed in centibeeps (1/100th of a basis point)|
            |forward_price|fp|string|True|[Options] The forward price of the option at point of trade, expressed in `9` decimals|
            |realized_pnl|rp|string|True|The realized PnL of the trade, expressed in quote asset decimal units (0 if increasing position size)|
            |fee|f|string|True|The fees paid on the trade, expressed in quote asset decimal unit (negative if maker rebate applied)|
            |fee_rate|fr|string|True|The fee rate paid on the trade|
            |trade_id|ti|string|True|A trade identifier|
            |order_id|oi|string|True|An order identifier|
            |venue|v|Venue|True|The venue where the trade occurred|
            |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
            ??? info "Venue"
                The list of Trading Venues that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`ORDERBOOK` = 1|the trade is cleared on the orderbook venue|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "is_buyer": true,
                "is_taker": true,
                "size": "0.30",
                "price": "65038.01",
                "mark_price": "65038.01",
                "index_price": "65038.01",
                "interest_rate": 0.0003,
                "forward_price": "65038.01",
                "realized_pnl": "2400.50",
                "fee": "9.75",
                "fee_rate": 0.0003,
                "trade_id": "209358",
                "order_id": "0x10000101000203040506",
                "venue": "ORDERBOOK",
                "client_order_id": "23042"
            }],
            "next": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/trade_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/trade_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/trade_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/trade_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
### Positions
```
FULL ENDPOINT: full/v1/positions
LITE ENDPOINT: lite/v1/positions
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPositionsRequest"
        Query the positions of a sub account<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The sub account ID to request for|
        |kind|k|[Kind]|True|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|[Currency]|True|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|[Currency]|True|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
        ??? info "Kind"
            The list of asset kinds that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`PERPETUAL` = 1|the perpetual asset kind|
            |`FUTURE` = 2|the future asset kind|
            |`CALL` = 3|the call option asset kind|
            |`PUT` = 4|the put option asset kind|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "u": ["BTC", "ETH"],
            "q": ["USDT", "USDC"]
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPositionsResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[Positions]|True|The positions matching the request filter|
        ??? info "Positions"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |sub_account_id|sa|string|True|The sub account ID that participated in the trade|
            |instrument|i|string|True|The instrument being represented|
            |size|s|string|True|The size of the position, expressed in underlying asset decimal units. Negative for short positions|
            |notional|n|string|True|The notional value of the position, negative for short assets, expressed in quote asset decimal units|
            |entry_price|ep|string|True|The entry price of the position, expressed in `9` decimals<br>Whenever increasing the size of a position, the entry price is updated to the new average entry price<br>`new_entry_price = (old_entry_price * old_size + trade_price * trade_size) / (old_size + trade_size)`|
            |exit_price|ep1|string|True|The exit price of the position, expressed in `9` decimals<br>Whenever decreasing the size of a position, the exit price is updated to the new average exit price<br>`new_exit_price = (old_exit_price * old_exit_trade_size + trade_price * trade_size) / (old_exit_trade_size + trade_size)`|
            |mark_price|mp|string|True|The mark price of the position, expressed in `9` decimals|
            |unrealized_pnl|up|string|True|The unrealized PnL of the position, expressed in quote asset decimal units<br>`unrealized_pnl = (mark_price - entry_price) * size`|
            |realized_pnl|rp|string|True|The realized PnL of the position, expressed in quote asset decimal units<br>`realized_pnl = (exit_price - entry_price) * exit_trade_size`|
            |total_pnl|tp|string|True|The total PnL of the position, expressed in quote asset decimal units<br>`total_pnl = realized_pnl + unrealized_pnl`|
            |roi|r|string|True|The ROI of the position, expressed as a percentage<br>`roi = (total_pnl / (entry_price * abs(size))) * 100^`|
            |quote_index_price|qi|string|True|The index price of the quote currency. (reported in `USD`)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "size": "2635000.50",
                "notional": "2635000.50",
                "entry_price": "65038.01",
                "exit_price": "65038.01",
                "mark_price": "65038.01",
                "unrealized_pnl": "135000.50",
                "realized_pnl": "-35000.30",
                "total_pnl": "100000.20",
                "roi": "10.20",
                "quote_index_price": "1.0000102"
            }]
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/positions' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/positions' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/positions' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/positions' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
<hr class="solid">
## Transfer
### Deposit
```
FULL ENDPOINT: full/v1/deposit
LITE ENDPOINT: lite/v1/deposit
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiDepositRequest"
        GRVT runs on a ZKSync Hyperchain which settles directly onto Ethereum.<br>To Deposit funds from your L1 wallet into a GRVT SubAccount, you will be required to submit a deposit transaction directly to Ethereum.<br>GRVT's bridge verifier will scan Ethereum from time to time. Once it receives proof that your deposit has been confirmed on Ethereum, it will initiate the deposit process.<br><br>This current payload is used for alpha testing only.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |to_account_id|ta|string|True|The main account to deposit into|
        |token_currency|tc|Currency|True|The token currency to deposit|
        |num_tokens|nt|string|True|The number of tokens to deposit, quoted in token_currency decimals|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0"
        }
        ```
        ```json
        {
            "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "tc": "USDT",
            "nt": "1500.0"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "AckResponse"
        Used to acknowledge a request has been received and will be processed<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |acknowledgement|a|boolean|True|Gravity has acknowledged that the request has been successfully received and it will process it in the backend|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "acknowledgement": "true"
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/deposit' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0"
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/deposit' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0"
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/deposit' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0"
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/deposit' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0"
        }
        '
        ```
<hr class="solid">
### Deposit History
```
FULL ENDPOINT: full/v1/deposit_history
LITE ENDPOINT: lite/v1/deposit_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiDepositHistoryRequest"
        The request to get the historical deposits of an account<br>The history is returned in reverse chronological order<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |token_currency|tc|[Currency]|True|The token currency to query for, if nil or empty, return all deposits. Otherwise, only entries matching the filter will be returned|
        |start_time|st|string|False|The start time to query for in unix nanoseconds|
        |end_time|et|string|False|The end time to query for in unix nanoseconds|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the next query from|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "tc": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiDepositHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[DepositHistory]|True|The deposit history matching the request account|
        |next|n|string|False|The cursor to indicate when to start the next query from|
        ??? info "DepositHistory"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |tx_id|ti|string|True|The transaction ID of the deposit|
            |tx_hash|th|string|True|The txHash of the bridgemint event|
            |to_account_id|ta|string|True|The account to deposit into|
            |token_currency|tc|Currency|True|The token currency to deposit|
            |num_tokens|nt|string|True|The number of tokens to deposit|
            |event_time|et|string|True|The timestamp of the deposit in unix nanoseconds|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "tx_id": "1028403",
                "tx_hash": "0x10000101000203040506",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "token_currency": "USDT",
                "num_tokens": "1500.0",
                "event_time": "1697788800000000000"
            }],
            "next": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/deposit_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/deposit_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/deposit_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/deposit_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
### Transfer
```
FULL ENDPOINT: full/v1/transfer
LITE ENDPOINT: lite/v1/transfer
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTransferRequest"
        This API allows you to transfer funds in multiple different ways<ul><br><li>Between SubAccounts within your Main Account</li><br><li>Between your MainAccount and your SubAccounts</li><br><li>To other MainAccounts that you have previously allowlisted</li><br></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |from_account_id|fa|string|True|The main account to transfer from|
        |from_sub_account_id|fs|string|True|The subaccount to transfer from (0 if transferring from main account)|
        |to_account_id|ta|string|True|The main account to deposit into|
        |to_sub_account_id|ts|string|True|The subaccount to transfer to (0 if transferring to main account)|
        |token_currency|tc|Currency|True|The token currency to transfer|
        |num_tokens|nt|string|True|The number of tokens to transfer, quoted in tokenCurrency decimal units|
        |signature|s|Signature|True|The signature of the transfer|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
        ??? info "Signature"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |signer|s|string|True|The address (public key) of the wallet signing the payload|
            |r|r|string|True|Signature R|
            |s|s1|string|True|Signature S|
            |v|v|number|True|Signature V|
            |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
            |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        ```
        ```json
        {
            "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "fs": "'$GRVT_SUB_ACCOUNT_ID'",
            "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "ts": "'$GRVT_SUB_ACCOUNT_ID'",
            "tc": "USDT",
            "nt": "1500.0",
            "s": {
                "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "e": "1697788800000000000",
                "n": "1234567890"
            }
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "AckResponse"
        Used to acknowledge a request has been received and will be processed<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |acknowledgement|a|boolean|True|Gravity has acknowledged that the request has been successfully received and it will process it in the backend|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "acknowledgement": "true"
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/transfer' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/transfer' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/transfer' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/transfer' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        '
        ```
<hr class="solid">
### Transfer History
```
FULL ENDPOINT: full/v1/transfer_history
LITE ENDPOINT: lite/v1/transfer_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTransferHistoryRequest"
        The request to get the historical transfers of an account<br>The history is returned in reverse chronological order<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |token_currency|tc|[Currency]|True|The token currency to query for, if nil or empty, return all transfers. Otherwise, only entries matching the filter will be returned|
        |start_time|st|string|False|The start time to query for in unix nanoseconds|
        |end_time|et|string|False|The end time to query for in unix nanoseconds|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the next query from|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "tc": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTransferHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[TransferHistory]|True|The transfer history matching the request account|
        |next|n|string|False|The cursor to indicate when to start the next query from|
        ??? info "TransferHistory"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |tx_id|ti|string|True|The transaction ID of the transfer|
            |from_account_id|fa|string|True|The account to transfer from|
            |from_sub_account_id|fs|string|True|The subaccount to transfer from (0 if transferring from main account)|
            |to_account_id|ta|string|True|The account to deposit into|
            |to_sub_account_id|ts|string|True|The subaccount to transfer to (0 if transferring to main account)|
            |token_currency|tc|Currency|True|The token currency to transfer|
            |num_tokens|nt|string|True|The number of tokens to transfer|
            |signature|s|Signature|True|The signature of the transfer|
            |event_time|et|string|True|The timestamp of the transfer in unix nanoseconds|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "Signature"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |signer|s|string|True|The address (public key) of the wallet signing the payload|
                |r|r|string|True|Signature R|
                |s|s1|string|True|Signature S|
                |v|v|number|True|Signature V|
                |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "tx_id": "1028403",
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "token_currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "event_time": "1697788800000000000"
            }],
            "next": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/transfer_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/transfer_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/transfer_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/transfer_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
### Withdrawal
```
FULL ENDPOINT: full/v1/withdrawal
LITE ENDPOINT: lite/v1/withdrawal
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiWithdrawalRequest"
        Leverage this API to initialize a withdrawal from GRVT's Hyperchain onto Ethereum.<br>Do take note that the bridging process does take time. The GRVT UI will help you keep track of bridging progress, and notify you once its complete.<br><br>If not withdrawing the entirety of your balance, there is a minimum withdrawal amount. Currently that amount is ~25 USDT.<br>Withdrawal fees also apply to cover the cost of the Ethereum transaction.<br>Note that your funds will always remain in self-custory throughout the withdrawal process. At no stage does GRVT gain control over your funds.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |from_account_id|fa|string|True|The main account to withdraw from|
        |to_eth_address|te|string|True|The Ethereum wallet to withdraw into|
        |token_currency|tc|Currency|True|The token currency to withdraw|
        |num_tokens|nt|string|True|The number of tokens to withdraw, quoted in tokenCurrency decimal units|
        |signature|s|Signature|True|The signature of the withdrawal|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
        ??? info "Signature"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |signer|s|string|True|The address (public key) of the wallet signing the payload|
            |r|r|string|True|Signature R|
            |s|s1|string|True|Signature S|
            |v|v|number|True|Signature V|
            |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
            |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        ```
        ```json
        {
            "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "tc": "USDT",
            "nt": "1500.0",
            "s": {
                "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "e": "1697788800000000000",
                "n": "1234567890"
            }
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "AckResponse"
        Used to acknowledge a request has been received and will be processed<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |acknowledgement|a|boolean|True|Gravity has acknowledged that the request has been successfully received and it will process it in the backend|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "acknowledgement": "true"
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/withdrawal' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/withdrawal' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/withdrawal' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/withdrawal' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": "28",
                "expiration": "1697788800000000000",
                "nonce": "1234567890"
            }
        }
        '
        ```
<hr class="solid">
### Withdrawal History
```
FULL ENDPOINT: full/v1/withdrawal_history
LITE ENDPOINT: lite/v1/withdrawal_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiWithdrawalHistoryRequest"
        The request to get the historical withdrawals of an account<br>The history is returned in reverse chronological order<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |token_currency|tc|[Currency]|True|The token currency to query for, if nil or empty, return all withdrawals. Otherwise, only entries matching the filter will be returned|
        |start_time|st|string|False|The start time to query for in unix nanoseconds|
        |end_time|et|string|False|The end time to query for in unix nanoseconds|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the next query from|
        ??? info "Currency"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "tc": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiWithdrawalHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[WithdrawalHistory]|True|The withdrawals history matching the request account|
        |next|n|string|False|The cursor to indicate when to start the next query from|
        ??? info "WithdrawalHistory"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |tx_id|ti|string|True|The transaction ID of the withdrawal|
            |from_account_id|fa|string|True|The subaccount to withdraw from|
            |to_eth_address|te|string|True|The ethereum address to withdraw to|
            |token_currency|tc|Currency|True|The token currency to withdraw|
            |num_tokens|nt|string|True|The number of tokens to withdraw|
            |signature|s|Signature|True|The signature of the withdrawal|
            |event_time|et|string|True|The timestamp of the withdrawal in unix nanoseconds|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "Signature"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |signer|s|string|True|The address (public key) of the wallet signing the payload|
                |r|r|string|True|Signature R|
                |s|s1|string|True|Signature S|
                |v|v|number|True|Signature V|
                |expiration|e|string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce|n|number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "tx_id": "1028403",
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "token_currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                },
                "event_time": "1697788800000000000"
            }],
            "next": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/withdrawal_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/withdrawal_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/withdrawal_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/withdrawal_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
## Account
### Sub Account Summary
```
FULL ENDPOINT: full/v1/account_summary
LITE ENDPOINT: lite/v1/account_summary
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiSubAccountSummaryRequest"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiSubAccountSummaryResponse"
        Query for sub-account details, including base currency balance, all derivative positions, margin levels, and P&L.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|SubAccount|True|The sub account matching the request sub account|
        ??? info "SubAccount"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |sub_account_id|sa|string|True|The sub account ID this entry refers to|
            |margin_type|mt|MarginType|True|The type of margin algorithm this subaccount uses|
            |settle_currency|sc|Currency|True|The settlement, margin, and reporting currency of this account.<br>This subaccount can only open positions quoted in this currency<br><br>In the future, when users select a Multi-Currency Margin Type, this will be USD<br>All other assets are converted to this currency for the purpose of calculating margin|
            |unrealized_pnl|up|string|True|The total unrealized PnL of all positions owned by this subaccount, denominated in quote currency decimal units.<br>`unrealized_pnl = sum(position.unrealized_pnl * position.quote_index_price) / settle_index_price`|
            |total_equity|te|string|True|The notional value of your account if all positions are closed, excluding trading fees (reported in `settle_currency`).<br>`total_equity = sum(spot_balance.balance * spot_balance.index_price) / settle_index_price + unrealized_pnl`|
            |initial_margin|im|string|True|The `total_equity` required to open positions in the account (reported in `settle_currency`).<br>Computation is different depending on account's `margin_type`|
            |maintenance_margin|mm|string|True|The `total_equity` required to avoid liquidation of positions in the account (reported in `settle_currency`).<br>Computation is different depending on account's `margin_type`|
            |available_balance|ab|string|True|The notional value available to transfer out of the trading account into the funding account (reported in `settle_currency`).<br>`available_balance = total_equity - initial_margin - min(unrealized_pnl, 0)`|
            |spot_balances|sb|[SpotBalance]|True|The list of spot assets owned by this sub account, and their balances|
            |positions|p|[Positions]|True|The list of positions owned by this sub account|
            |settle_index_price|si|string|True|The index price of the settle currency. (reported in `USD`)|
            ??? info "MarginType"
                |Value| Description |
                |-|-|
                |`SIMPLE_CROSS_MARGIN` = 2|Simple Cross Margin Mode: all assets have a predictable margin impact, the whole subaccount shares a single margin|
                |`PORTFOLIO_CROSS_MARGIN` = 3|Portfolio Cross Margin Mode: asset margin impact is analysed on portfolio level, the whole subaccount shares a single margin|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "SpotBalance"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |currency|c|Currency|True|The currency you hold a spot balance in|
                |balance|b|string|True|This currency's balance in this trading account.|
                |index_price|ip|string|True|The index price of this currency. (reported in `USD`)|
                ??? info "Currency"
                    The list of Currencies that are supported on the GRVT exchange<br>

                    |Value| Description |
                    |-|-|
                    |`USDC` = 2|the USDC token|
                    |`USDT` = 3|the USDT token|
                    |`ETH` = 4|the ETH token|
                    |`BTC` = 5|the BTC token|
            ??? info "Positions"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
                |sub_account_id|sa|string|True|The sub account ID that participated in the trade|
                |instrument|i|string|True|The instrument being represented|
                |size|s|string|True|The size of the position, expressed in underlying asset decimal units. Negative for short positions|
                |notional|n|string|True|The notional value of the position, negative for short assets, expressed in quote asset decimal units|
                |entry_price|ep|string|True|The entry price of the position, expressed in `9` decimals<br>Whenever increasing the size of a position, the entry price is updated to the new average entry price<br>`new_entry_price = (old_entry_price * old_size + trade_price * trade_size) / (old_size + trade_size)`|
                |exit_price|ep1|string|True|The exit price of the position, expressed in `9` decimals<br>Whenever decreasing the size of a position, the exit price is updated to the new average exit price<br>`new_exit_price = (old_exit_price * old_exit_trade_size + trade_price * trade_size) / (old_exit_trade_size + trade_size)`|
                |mark_price|mp|string|True|The mark price of the position, expressed in `9` decimals|
                |unrealized_pnl|up|string|True|The unrealized PnL of the position, expressed in quote asset decimal units<br>`unrealized_pnl = (mark_price - entry_price) * size`|
                |realized_pnl|rp|string|True|The realized PnL of the position, expressed in quote asset decimal units<br>`realized_pnl = (exit_price - entry_price) * exit_trade_size`|
                |total_pnl|tp|string|True|The total PnL of the position, expressed in quote asset decimal units<br>`total_pnl = realized_pnl + unrealized_pnl`|
                |roi|r|string|True|The ROI of the position, expressed as a percentage<br>`roi = (total_pnl / (entry_price * abs(size))) * 100^`|
                |quote_index_price|qi|string|True|The index price of the quote currency. (reported in `USD`)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": {
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "margin_type": "SIMPLE_CROSS_MARGIN",
                "settle_currency": "USDT",
                "unrealized_pnl": "123456.78",
                "total_equity": "123456.78",
                "initial_margin": "123456.78",
                "maintenance_margin": "123456.78",
                "available_balance": "123456.78",
                "spot_balances": [{
                    "currency": "USDT",
                    "balance": "123456.78",
                    "index_price": "1.0000102"
                }],
                "positions": [{
                    "event_time": "1697788800000000000",
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "instrument": "BTC_USDT_Perp",
                    "size": "2635000.50",
                    "notional": "2635000.50",
                    "entry_price": "65038.01",
                    "exit_price": "65038.01",
                    "mark_price": "65038.01",
                    "unrealized_pnl": "135000.50",
                    "realized_pnl": "-35000.30",
                    "total_pnl": "100000.20",
                    "roi": "10.20",
                    "quote_index_price": "1.0000102"
                }],
                "settle_index_price": "1.0000102"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |2004|401|Order sub account does not match logged in user|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":2004,
            "message":"Order sub account does not match logged in user",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        '
        ```
<hr class="solid">
### Sub Account History
```
FULL ENDPOINT: full/v1/account_history
LITE ENDPOINT: lite/v1/account_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiSubAccountHistoryRequest"
        The request to get the history of a sub account<br>SubAccount Summary values are snapshotted once every hour<br>No snapshots are taken if the sub account has no activity in the hourly window<br>History is preserved only for the last 30 days<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The sub account ID to request for|
        |start_time|st|string|False|Start time of sub account history in unix nanoseconds|
        |end_time|et|string|False|End time of sub account history in unix nanoseconds|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the next query from|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiSubAccountHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[SubAccount]|True|The sub account history matching the request sub account|
        |next|n|string|True|The cursor to indicate when to start the next query from|
        ??? info "SubAccount"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |sub_account_id|sa|string|True|The sub account ID this entry refers to|
            |margin_type|mt|MarginType|True|The type of margin algorithm this subaccount uses|
            |settle_currency|sc|Currency|True|The settlement, margin, and reporting currency of this account.<br>This subaccount can only open positions quoted in this currency<br><br>In the future, when users select a Multi-Currency Margin Type, this will be USD<br>All other assets are converted to this currency for the purpose of calculating margin|
            |unrealized_pnl|up|string|True|The total unrealized PnL of all positions owned by this subaccount, denominated in quote currency decimal units.<br>`unrealized_pnl = sum(position.unrealized_pnl * position.quote_index_price) / settle_index_price`|
            |total_equity|te|string|True|The notional value of your account if all positions are closed, excluding trading fees (reported in `settle_currency`).<br>`total_equity = sum(spot_balance.balance * spot_balance.index_price) / settle_index_price + unrealized_pnl`|
            |initial_margin|im|string|True|The `total_equity` required to open positions in the account (reported in `settle_currency`).<br>Computation is different depending on account's `margin_type`|
            |maintenance_margin|mm|string|True|The `total_equity` required to avoid liquidation of positions in the account (reported in `settle_currency`).<br>Computation is different depending on account's `margin_type`|
            |available_balance|ab|string|True|The notional value available to transfer out of the trading account into the funding account (reported in `settle_currency`).<br>`available_balance = total_equity - initial_margin - min(unrealized_pnl, 0)`|
            |spot_balances|sb|[SpotBalance]|True|The list of spot assets owned by this sub account, and their balances|
            |positions|p|[Positions]|True|The list of positions owned by this sub account|
            |settle_index_price|si|string|True|The index price of the settle currency. (reported in `USD`)|
            ??? info "MarginType"
                |Value| Description |
                |-|-|
                |`SIMPLE_CROSS_MARGIN` = 2|Simple Cross Margin Mode: all assets have a predictable margin impact, the whole subaccount shares a single margin|
                |`PORTFOLIO_CROSS_MARGIN` = 3|Portfolio Cross Margin Mode: asset margin impact is analysed on portfolio level, the whole subaccount shares a single margin|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "SpotBalance"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |currency|c|Currency|True|The currency you hold a spot balance in|
                |balance|b|string|True|This currency's balance in this trading account.|
                |index_price|ip|string|True|The index price of this currency. (reported in `USD`)|
                ??? info "Currency"
                    The list of Currencies that are supported on the GRVT exchange<br>

                    |Value| Description |
                    |-|-|
                    |`USDC` = 2|the USDC token|
                    |`USDT` = 3|the USDT token|
                    |`ETH` = 4|the ETH token|
                    |`BTC` = 5|the BTC token|
            ??? info "Positions"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
                |sub_account_id|sa|string|True|The sub account ID that participated in the trade|
                |instrument|i|string|True|The instrument being represented|
                |size|s|string|True|The size of the position, expressed in underlying asset decimal units. Negative for short positions|
                |notional|n|string|True|The notional value of the position, negative for short assets, expressed in quote asset decimal units|
                |entry_price|ep|string|True|The entry price of the position, expressed in `9` decimals<br>Whenever increasing the size of a position, the entry price is updated to the new average entry price<br>`new_entry_price = (old_entry_price * old_size + trade_price * trade_size) / (old_size + trade_size)`|
                |exit_price|ep1|string|True|The exit price of the position, expressed in `9` decimals<br>Whenever decreasing the size of a position, the exit price is updated to the new average exit price<br>`new_exit_price = (old_exit_price * old_exit_trade_size + trade_price * trade_size) / (old_exit_trade_size + trade_size)`|
                |mark_price|mp|string|True|The mark price of the position, expressed in `9` decimals|
                |unrealized_pnl|up|string|True|The unrealized PnL of the position, expressed in quote asset decimal units<br>`unrealized_pnl = (mark_price - entry_price) * size`|
                |realized_pnl|rp|string|True|The realized PnL of the position, expressed in quote asset decimal units<br>`realized_pnl = (exit_price - entry_price) * exit_trade_size`|
                |total_pnl|tp|string|True|The total PnL of the position, expressed in quote asset decimal units<br>`total_pnl = realized_pnl + unrealized_pnl`|
                |roi|r|string|True|The ROI of the position, expressed as a percentage<br>`roi = (total_pnl / (entry_price * abs(size))) * 100^`|
                |quote_index_price|qi|string|True|The index price of the quote currency. (reported in `USD`)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "margin_type": "SIMPLE_CROSS_MARGIN",
                "settle_currency": "USDT",
                "unrealized_pnl": "123456.78",
                "total_equity": "123456.78",
                "initial_margin": "123456.78",
                "maintenance_margin": "123456.78",
                "available_balance": "123456.78",
                "spot_balances": [{
                    "currency": "USDT",
                    "balance": "123456.78",
                    "index_price": "1.0000102"
                }],
                "positions": [{
                    "event_time": "1697788800000000000",
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "instrument": "BTC_USDT_Perp",
                    "size": "2635000.50",
                    "notional": "2635000.50",
                    "entry_price": "65038.01",
                    "exit_price": "65038.01",
                    "mark_price": "65038.01",
                    "unrealized_pnl": "135000.50",
                    "realized_pnl": "-35000.30",
                    "total_pnl": "100000.20",
                    "roi": "10.20",
                    "quote_index_price": "1.0000102"
                }],
                "settle_index_price": "1.0000102"
            }],
            "next": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
        |1000|401|You are not authorized to access this functionality|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        {
            "code":1000,
            "message":"You are not authorized to access this functionality",
            "status":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/account_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/account_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/account_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/account_history' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
### Aggregated Account Summary
```
FULL ENDPOINT: full/v1/aggregated_account_summary
LITE ENDPOINT: lite/v1/aggregated_account_summary
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "EmptyRequest"
        Used for requests that do not require any parameters<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
        }
        ```
        ```json
        {
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiAggregatedAccountSummaryResponse"
        The aggregated account summary, that reports the total equity and spot balances of a funding (main) account, and its constituent trading (sub) accounts<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |main_account_id|ma|string|True|The main account ID of the account to which the summary belongs|
        |total_equity|te|string|True|Total equity of the main (+ sub) account, denominated in USD|
        |spot_balances|sb|[SpotBalance]|True|The list of spot assets owned by this main (+ sub) account, and their balances|
        ??? info "SpotBalance"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |currency|c|Currency|True|The currency you hold a spot balance in|
            |balance|b|string|True|This currency's balance in this trading account.|
            |index_price|ip|string|True|The index price of this currency. (reported in `USD`)|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "main_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "total_equity": "3945034.23",
            "spot_balances": [{
                "currency": "USDT",
                "balance": "123456.78",
                "index_price": "1.0000102"
            }]
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/aggregated_account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/aggregated_account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/aggregated_account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/aggregated_account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
        }
        '
        ```
<hr class="solid">
### Funding Account Summary
```
FULL ENDPOINT: full/v1/funding_account_summary
LITE ENDPOINT: lite/v1/funding_account_summary
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "EmptyRequest"
        Used for requests that do not require any parameters<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
        }
        ```
        ```json
        {
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiFundingAccountSummaryResponse"
        The funding account summary, that reports the total equity and spot balances of a funding (main) account<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |main_account_id|ma|string|True|The main account ID of the account to which the summary belongs|
        |total_equity|te|string|True|Total equity of the main account, denominated in USD|
        |spot_balances|sb|[SpotBalance]|True|The list of spot assets owned by this main account, and their balances|
        ??? info "SpotBalance"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |currency|c|Currency|True|The currency you hold a spot balance in|
            |balance|b|string|True|This currency's balance in this trading account.|
            |index_price|ip|string|True|The index price of this currency. (reported in `USD`)|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "main_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "total_equity": "3945034.23",
            "spot_balances": [{
                "currency": "USDT",
                "balance": "123456.78",
                "index_price": "1.0000102"
            }]
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
        |1002|400|Invalid Request|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1002,
            "message":"Invalid Request",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/funding_account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/funding_account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/funding_account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/funding_account_summary' \
        --header "Cookie: $GRVT_COOKIE" \
        --data '{
        }
        '
        ```
<hr class="solid">
