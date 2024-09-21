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
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>            GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>            This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>            Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br>            <br>            All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>            This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|True|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|True|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |taker_fee_percentage_cap|tf|number|True|The taker fee percentage cap signed by the order.<br>This is the maximum taker fee percentage the order sender is willing to pay for the order.<br>Expressed in 1/100th of a basis point. Eg. 100 = 1bps, 10,000 = 1%<br>|
            |maker_fee_percentage_cap|mf|number|True|Same as TakerFeePercentageCap, but for the maker fee. Negative for maker rebates|
            |post_only|po|boolean|True|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|True|If True, Order must reduce the position size, or be cancelled|
            |legs|l|OrderLeg|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|True|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
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
                |limit_price|lp|string|True|The limit price of the order leg, expressed in `9` decimals.<br>This is the total amount of base currency to pay/receive for all legs.|
                |oco_limit_price|ol|string|True|If a OCO order is specified, this must contain the other limit price<br>User must sign both limit prices. Depending on which trigger condition is activated, a different limit price is used<br>The smart contract will always validate both limit prices, by arranging them in ascending order|
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
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>                Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|True|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|string|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|string|True|The total number of assets traded. Sorted in same order as Order.Legs|
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
    !!! example
        ```json
        {
            "order": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
                "oi": "2927361400114782",
                "sa": "2927361400114782",
                "im": false,
                "ti": "GOOD_TILL_TIME",
                "tf": "0.05",
                "mf": "0.03",
                "po": false,
                "ro": false,
                "l": {
                    "i": "BTC_USDT_Perp",
                    "s": "10.5",
                    "lp": "65038.01",
                    "ol": "63038.01",
                    "ib": true
                },
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
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>            GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>            This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>            Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br>            <br>            All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>            This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|True|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|True|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |taker_fee_percentage_cap|tf|number|True|The taker fee percentage cap signed by the order.<br>This is the maximum taker fee percentage the order sender is willing to pay for the order.<br>Expressed in 1/100th of a basis point. Eg. 100 = 1bps, 10,000 = 1%<br>|
            |maker_fee_percentage_cap|mf|number|True|Same as TakerFeePercentageCap, but for the maker fee. Negative for maker rebates|
            |post_only|po|boolean|True|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|True|If True, Order must reduce the position size, or be cancelled|
            |legs|l|OrderLeg|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|True|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
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
                |limit_price|lp|string|True|The limit price of the order leg, expressed in `9` decimals.<br>This is the total amount of base currency to pay/receive for all legs.|
                |oco_limit_price|ol|string|True|If a OCO order is specified, this must contain the other limit price<br>User must sign both limit prices. Depending on which trigger condition is activated, a different limit price is used<br>The smart contract will always validate both limit prices, by arranging them in ascending order|
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
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>                Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|True|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|string|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|string|True|The total number of assets traded. Sorted in same order as Order.Legs|
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
    !!! example
        ```json
        {
            "order": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/create_order' \
        --data '{
            "order": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/create_order' \
        --data '{
            "order": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/create_order' \
        --data '{
            "order": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/create_order' \
        --data '{
            "order": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
        Cancel an order on the orderbook for this trading account.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID cancelling the order|
        |order_id|oi|string|True|Cancel the order with this `order_id`|
        |client_order_id|co|string|True|Cancel the order with this `client_order_id`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        ```
        ```json
        {
            "sa": "2927361400114782",
            "oi": "0x1028403",
            "co": "23042"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiCancelOrderResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |order|o|Order|True|The cancelled order|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>            GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>            This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>            Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br>            <br>            All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>            This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|True|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|True|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |taker_fee_percentage_cap|tf|number|True|The taker fee percentage cap signed by the order.<br>This is the maximum taker fee percentage the order sender is willing to pay for the order.<br>Expressed in 1/100th of a basis point. Eg. 100 = 1bps, 10,000 = 1%<br>|
            |maker_fee_percentage_cap|mf|number|True|Same as TakerFeePercentageCap, but for the maker fee. Negative for maker rebates|
            |post_only|po|boolean|True|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|True|If True, Order must reduce the position size, or be cancelled|
            |legs|l|OrderLeg|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|True|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
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
                |limit_price|lp|string|True|The limit price of the order leg, expressed in `9` decimals.<br>This is the total amount of base currency to pay/receive for all legs.|
                |oco_limit_price|ol|string|True|If a OCO order is specified, this must contain the other limit price<br>User must sign both limit prices. Depending on which trigger condition is activated, a different limit price is used<br>The smart contract will always validate both limit prices, by arranging them in ascending order|
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
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>                Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|True|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|string|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|string|True|The total number of assets traded. Sorted in same order as Order.Legs|
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
    !!! example
        ```json
        {
            "order": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/cancel_order' \
        --data '{
            "sub_account_id": "2927361400114782",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/cancel_order' \
        --data '{
            "sub_account_id": "2927361400114782",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/cancel_order' \
        --data '{
            "sub_account_id": "2927361400114782",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/cancel_order' \
        --data '{
            "sub_account_id": "2927361400114782",
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
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782"
        }
        ```
        ```json
        {
            "sa": "2927361400114782"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiCancelAllOrdersResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |num_cancelled|nc|number|True|The number of orders cancelled|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "num_cancelled": "52"
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/cancel_all_orders' \
        --data '{
            "sub_account_id": "2927361400114782"
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/cancel_all_orders' \
        --data '{
            "sub_account_id": "2927361400114782"
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/cancel_all_orders' \
        --data '{
            "sub_account_id": "2927361400114782"
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/cancel_all_orders' \
        --data '{
            "sub_account_id": "2927361400114782"
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
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
        |order_id|oi|string|True|Filter for `order_id`|
        |client_order_id|co|string|True|Filter for `client_order_id`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        ```
        ```json
        {
            "sa": "2927361400114782",
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
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>            GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>            This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>            Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br>            <br>            All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>            This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|True|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|True|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |taker_fee_percentage_cap|tf|number|True|The taker fee percentage cap signed by the order.<br>This is the maximum taker fee percentage the order sender is willing to pay for the order.<br>Expressed in 1/100th of a basis point. Eg. 100 = 1bps, 10,000 = 1%<br>|
            |maker_fee_percentage_cap|mf|number|True|Same as TakerFeePercentageCap, but for the maker fee. Negative for maker rebates|
            |post_only|po|boolean|True|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|True|If True, Order must reduce the position size, or be cancelled|
            |legs|l|OrderLeg|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|True|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
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
                |limit_price|lp|string|True|The limit price of the order leg, expressed in `9` decimals.<br>This is the total amount of base currency to pay/receive for all legs.|
                |oco_limit_price|ol|string|True|If a OCO order is specified, this must contain the other limit price<br>User must sign both limit prices. Depending on which trigger condition is activated, a different limit price is used<br>The smart contract will always validate both limit prices, by arranging them in ascending order|
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
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>                Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|True|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|string|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|string|True|The total number of assets traded. Sorted in same order as Order.Legs|
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
    !!! example
        ```json
        {
            "order": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/order' \
        --data '{
            "sub_account_id": "2927361400114782",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/order' \
        --data '{
            "sub_account_id": "2927361400114782",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/order' \
        --data '{
            "sub_account_id": "2927361400114782",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/order' \
        --data '{
            "sub_account_id": "2927361400114782",
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
        |kind|k|Kind|True|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|Currency|True|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|Currency|True|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
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
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        ```
        ```json
        {
            "sa": "2927361400114782",
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
        |orders|o|Order|True|The Open Orders matching the request filter|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>            GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>            This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>            Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br>            <br>            All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>            This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|True|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|True|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |taker_fee_percentage_cap|tf|number|True|The taker fee percentage cap signed by the order.<br>This is the maximum taker fee percentage the order sender is willing to pay for the order.<br>Expressed in 1/100th of a basis point. Eg. 100 = 1bps, 10,000 = 1%<br>|
            |maker_fee_percentage_cap|mf|number|True|Same as TakerFeePercentageCap, but for the maker fee. Negative for maker rebates|
            |post_only|po|boolean|True|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|True|If True, Order must reduce the position size, or be cancelled|
            |legs|l|OrderLeg|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|True|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
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
                |limit_price|lp|string|True|The limit price of the order leg, expressed in `9` decimals.<br>This is the total amount of base currency to pay/receive for all legs.|
                |oco_limit_price|ol|string|True|If a OCO order is specified, this must contain the other limit price<br>User must sign both limit prices. Depending on which trigger condition is activated, a different limit price is used<br>The smart contract will always validate both limit prices, by arranging them in ascending order|
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
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>                Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|True|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|string|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|string|True|The total number of assets traded. Sorted in same order as Order.Legs|
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
    !!! example
        ```json
        {
            "orders": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/open_orders' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/open_orders' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/open_orders' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/open_orders' \
        --data '{
            "sub_account_id": "2927361400114782",
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
        Retrieves the order history for the account.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
        |kind|k|Kind|True|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|Currency|True|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|Currency|True|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
        |expiration|e|string|True|The expiration time to apply in nanoseconds. If nil, this defaults to all expirations. Otherwise, only entries matching the filter will be returned|
        |strike_price|sp|string|True|The strike price to apply. If nil, this defaults to all strike prices. Otherwise, only entries matching the filter will be returned|
        |limit|l|number|True|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|True|The cursor to indicate when to start the query from|
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
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": ["1697788800000000000"],
            "strike_price": ["65000.0"],
            "limit": 500,
            "cursor": "Qw0918="
        }
        ```
        ```json
        {
            "sa": "2927361400114782",
            "k": ["PERPETUAL"],
            "u": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "e": ["1697788800000000000"],
            "sp": ["65000.0"],
            "l": 500,
            "c": "Qw0918="
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiOrderHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |total|t|number|True|The total number of orders matching the request filter|
        |next|n|string|True|The cursor to indicate when to start the query from|
        |orders|o|Order|True|The Open Orders matching the request filter|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>            GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>            This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>            Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br>            <br>            All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>            This minimizes the amount of trust users have to offer to GRVT<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|True|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id|sa|string|True|The subaccount initiating the order|
            |is_market|im|boolean|True|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force|ti|TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |taker_fee_percentage_cap|tf|number|True|The taker fee percentage cap signed by the order.<br>This is the maximum taker fee percentage the order sender is willing to pay for the order.<br>Expressed in 1/100th of a basis point. Eg. 100 = 1bps, 10,000 = 1%<br>|
            |maker_fee_percentage_cap|mf|number|True|Same as TakerFeePercentageCap, but for the maker fee. Negative for maker rebates|
            |post_only|po|boolean|True|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only|ro|boolean|True|If True, Order must reduce the position size, or be cancelled|
            |legs|l|OrderLeg|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature|s|Signature|True|The signature approving this order|
            |metadata|m|OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state|s1|OrderState|True|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
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
                |limit_price|lp|string|True|The limit price of the order leg, expressed in `9` decimals.<br>This is the total amount of base currency to pay/receive for all legs.|
                |oco_limit_price|ol|string|True|If a OCO order is specified, this must contain the other limit price<br>User must sign both limit prices. Depending on which trigger condition is activated, a different limit price is used<br>The smart contract will always validate both limit prices, by arranging them in ascending order|
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
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>                Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |client_order_id|co|string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time|ct|string|True|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |status|s|OrderStatus|True|The status of the order|
                |reject_reason|rr|OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size|bs|string|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size|ts|string|True|The total number of assets traded. Sorted in same order as Order.Legs|
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
    !!! example
        ```json
        {
            "total": 500,
            "next": "Qw0918=",
            "orders": {
                "order_id": "2927361400114782",
                "sub_account_id": "2927361400114782",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "taker_fee_percentage_cap": "0.05",
                "maker_fee_percentage_cap": "0.03",
                "post_only": false,
                "reduce_only": false,
                "legs": {
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "oco_limit_price": "63038.01",
                    "is_buying_asset": true
                },
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/order_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": ["1697788800000000000"],
            "strike_price": ["65000.0"],
            "limit": 500,
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/order_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": ["1697788800000000000"],
            "strike_price": ["65000.0"],
            "limit": 500,
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/order_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": ["1697788800000000000"],
            "strike_price": ["65000.0"],
            "limit": 500,
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/order_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": ["1697788800000000000"],
            "strike_price": ["65000.0"],
            "limit": 500,
            "cursor": "Qw0918="
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
        Query for all historical trades made by a single account. A single order can be matched multiple times, hence there is no real way to uniquely identify a trade.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The sub account ID to request for|
        |kind|k|Kind|True|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|Currency|True|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|Currency|True|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
        |expiration|e|string|True|The expiration time to apply in unix nanoseconds. If nil, this defaults to all expirations. Otherwise, only entries matching the filter will be returned|
        |strike_price|sp|string|True|The strike price to apply. If nil, this defaults to all strike prices. Otherwise, only entries matching the filter will be returned|
        |limit|l|number|True|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|True|The cursor to indicate when to start the query from|
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
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "limit": 500,
            "cursor": "Qw0918="
        }
        ```
        ```json
        {
            "sa": "2927361400114782",
            "k": ["PERPETUAL"],
            "u": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "e": "1697788800000000000",
            "sp": 65000.0,
            "l": 500,
            "c": "Qw0918="
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPrivateTradeHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |total|t|number|True|The total number of private trades matching the request filter|
        |next|n|string|True|The cursor to indicate when to start the query from|
        |results|r|PrivateTrade|True|The private trades matching the request asset|
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
    !!! example
        ```json
        {
            "total": 52,
            "next": "Qw0918=",
            "results": {
                "event_time": "1697788800000000000",
                "sub_account_id": "2927361400114782",
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
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/trade_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "limit": 500,
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/trade_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "limit": 500,
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/trade_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "limit": 500,
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/trade_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "limit": 500,
            "cursor": "Qw0918="
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
        |kind|k|Kind|True|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|Currency|True|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|Currency|True|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
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
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        ```
        ```json
        {
            "sa": "2927361400114782",
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
        |results|r|Positions|True|The positions matching the request filter|
        ??? info "Positions"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |sub_account_id|sa|string|True|The sub account ID that participated in the trade|
            |instrument|i|string|True|The instrument being represented|
            |balance|b|string|True|The balance of the position, expressed in underlying asset decimal units. Negative for short positions|
            |value|v|string|True|The value of the position, negative for short assets, expressed in quote asset decimal units|
            |entry_price|ep|string|True|The entry price of the position, expressed in `9` decimals<br>Whenever increasing the balance of a position, the entry price is updated to the new average entry price<br>newEntryPrice = (oldEntryPrice * oldBalance + tradePrice * tradeBalance) / (oldBalance + tradeBalance)|
            |exit_price|ep1|string|True|The exit price of the position, expressed in `9` decimals<br>Whenever decreasing the balance of a position, the exit price is updated to the new average exit price<br>newExitPrice = (oldExitPrice * oldExitBalance + tradePrice * tradeBalance) / (oldExitBalance + tradeBalance)|
            |mark_price|mp|string|True|The mark price of the position, expressed in `9` decimals|
            |unrealized_pnl|up|string|True|The unrealized PnL of the position, expressed in quote asset decimal units<br>unrealizedPnl = (markPrice - entryPrice) * balance|
            |realized_pnl|rp|string|True|The realized PnL of the position, expressed in quote asset decimal units<br>realizedPnl = (exitPrice - entryPrice) * exitBalance|
            |pnl|p|string|True|The total PnL of the position, expressed in quote asset decimal units<br>totalPnl = realizedPnl + unrealizedPnl|
            |roi|r|string|True|The ROI of the position, expressed as a percentage<br>roi = (pnl / (entryPrice * balance)) * 100|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "results": {
                "event_time": "1697788800000000000",
                "sub_account_id": "2927361400114782",
                "instrument": "BTC_USDT_Perp",
                "balance": "2635000.50",
                "value": "2635000.50",
                "entry_price": "65038.01",
                "exit_price": "65038.01",
                "mark_price": "65038.01",
                "unrealized_pnl": "135000.50",
                "realized_pnl": "-35000.30",
                "pnl": "100000.20",
                "roi": "10.20"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/positions' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/positions' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/positions' \
        --data '{
            "sub_account_id": "2927361400114782",
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/positions' \
        --data '{
            "sub_account_id": "2927361400114782",
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
        GRVT runs on a ZKSync Hyperchain which settles directly onto Ethereum.<br>        To Deposit funds from your L1 wallet into a GRVT SubAccount, you will be required to submit a deposit transaction directly to Ethereum.<br>        GRVT's bridge verifier will scan Ethereum from time to time. Once it receives proof that your deposit has been confirmed on Ethereum, it will initiate the deposit process.<br>        <br>        This current payload is used for alpha testing only.<br>

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
    !!! example
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
    !!! example
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/deposit' \
        --data '{
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0"
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/deposit' \
        --data '{
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0"
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/deposit' \
        --data '{
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "token_currency": "USDT",
            "num_tokens": "1500.0"
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/deposit' \
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
        The request to get the historical deposits of an account<br>        The history is returned in reverse chronological order<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |limit|l|number|True|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|True|The cursor to indicate when to start the next query from|
        |token_currency|tc|Currency|True|The token currency to query for, if nil or empty, return all deposits. Otherwise, only entries matching the filter will be returned|
        |start_time|st|string|True|The start time to query for in unix nanoseconds|
        |end_time|et|string|True|The end time to query for in unix nanoseconds|
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
    !!! example
        ```json
        {
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        ```
        ```json
        {
            "l": 500,
            "c": "Qw0918=",
            "tc": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiDepositHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |total|t|number|True|The total number of deposits matching the request account|
        |next|n|string|True|The cursor to indicate when to start the next query from|
        |results|r|DepositHistory|True|The deposit history matching the request account|
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
    !!! example
        ```json
        {
            "total": 52,
            "next": "Qw0918=",
            "results": {
                "tx_id": "1028403",
                "tx_hash": "0x10000101000203040506",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "token_currency": "USDT",
                "num_tokens": "1500.0",
                "event_time": "1697788800000000000"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/deposit_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/deposit_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/deposit_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/deposit_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
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
        This API allows you to transfer funds in multiple different ways<ul><br>        <li>Between SubAccounts within your Main Account</li><br>        <li>Between your MainAccount and your SubAccounts</li><br>        <li>To other MainAccounts that you have previously allowlisted</li><br>        </ul><br>

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
    !!! example
        ```json
        {
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "2927361400114782",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "2927361400114782",
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
            "fs": "2927361400114782",
            "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "ts": "2927361400114782",
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
    !!! example
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/transfer' \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "2927361400114782",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "2927361400114782",
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
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/transfer' \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "2927361400114782",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "2927361400114782",
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
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/transfer' \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "2927361400114782",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "2927361400114782",
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
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/transfer' \
        --data '{
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "2927361400114782",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "2927361400114782",
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
        The request to get the historical transfers of an account<br>        The history is returned in reverse chronological order<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |limit|l|number|True|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|True|The cursor to indicate when to start the next query from|
        |token_currency|tc|Currency|True|The token currency to query for, if nil or empty, return all transfers. Otherwise, only entries matching the filter will be returned|
        |start_time|st|string|True|The start time to query for in unix nanoseconds|
        |end_time|et|string|True|The end time to query for in unix nanoseconds|
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
    !!! example
        ```json
        {
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        ```
        ```json
        {
            "l": 500,
            "c": "Qw0918=",
            "tc": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTransferHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |total|t|number|True|The total number of transfers matching the request account|
        |next|n|string|True|The cursor to indicate when to start the next query from|
        |results|r|TransferHistory|True|The transfer history matching the request account|
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
    !!! example
        ```json
        {
            "total": 52,
            "next": "Qw0918=",
            "results": {
                "tx_id": "1028403",
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "2927361400114782",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "2927361400114782",
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
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/transfer_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/transfer_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/transfer_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/transfer_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
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
        Leverage this API to initialize a withdrawal from GRVT's Hyperchain onto Ethereum.<br>        Do take note that the bridging process does take time. The GRVT UI will help you keep track of bridging progress, and notify you once its complete.<br>        <br>        If not withdrawing the entirety of your balance, there is a minimum withdrawal amount. Currently that amount is ~25 USDT.<br>        Withdrawal fees also apply to cover the cost of the Ethereum transaction.<br>        Note that your funds will always remain in self-custory throughout the withdrawal process. At no stage does GRVT gain control over your funds.<br>

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
    !!! example
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
    !!! example
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/withdrawal' \
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
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/withdrawal' \
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
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/withdrawal' \
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
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/withdrawal' \
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
        The request to get the historical withdrawals of an account<br>        The history is returned in reverse chronological order<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |limit|l|number|True|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|True|The cursor to indicate when to start the next query from|
        |token_currency|tc|Currency|True|The token currency to query for, if nil or empty, return all withdrawals. Otherwise, only entries matching the filter will be returned|
        |start_time|st|string|True|The start time to query for in unix nanoseconds|
        |end_time|et|string|True|The end time to query for in unix nanoseconds|
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
    !!! example
        ```json
        {
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        ```
        ```json
        {
            "l": 500,
            "c": "Qw0918=",
            "tc": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiWithdrawalHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |total|t|number|True|The total number of withdrawals matching the request account|
        |next|n|string|True|The cursor to indicate when to start the next query from|
        |results|r|WithdrawalHistory|True|The withdrawals history matching the request account|
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
    !!! example
        ```json
        {
            "total": 52,
            "next": "Qw0918=",
            "results": {
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
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/withdrawal_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/withdrawal_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/withdrawal_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/withdrawal_history' \
        --data '{
            "limit": 500,
            "cursor": "Qw0918=",
            "token_currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000"
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
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782"
        }
        ```
        ```json
        {
            "sa": "2927361400114782"
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
            |quote_currency|qc|Currency|True|The Quote Currency that this Sub Account is denominated in<br>This subaccount can only open derivative positions denominated in this quote currency<br>All other assets are converted to this quote currency for the purpose of calculating margin<br>In the future, when users select a Multi-Currency Margin Type, this will be USD|
            |unrealized_pnl|up|string|True|The total unrealized PnL of all positions owned by this subaccount, denominated in quote currency decimal units|
            |total_value|tv|string|True|The total value across all spot assets, or in other words, the current margin |
            |initial_margin|im|string|True|The initial margin requirement of all positions owned by this vault, denominated in quote currency decimal units|
            |maintanence_margin|mm|string|True|The maintanence margin requirement of all positions owned by this vault, denominated in quote currency decimal units|
            |available_margin|am|string|True|The margin available for withdrawal, denominated in quote currency decimal units|
            |spot_balances|sb|SpotBalance|True|The list of spot assets owned by this sub account, and their balances|
            |positions|p|Positions|True|The list of positions owned by this sub account|
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
                |balance|b|string|True|The balance of the asset, expressed in underlying asset decimal units<br>Must take into account the value of all positions with this quote asset<br>ie. for USDT denominated subaccounts, this is is identical to total balance|
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
                |balance|b|string|True|The balance of the position, expressed in underlying asset decimal units. Negative for short positions|
                |value|v|string|True|The value of the position, negative for short assets, expressed in quote asset decimal units|
                |entry_price|ep|string|True|The entry price of the position, expressed in `9` decimals<br>Whenever increasing the balance of a position, the entry price is updated to the new average entry price<br>newEntryPrice = (oldEntryPrice * oldBalance + tradePrice * tradeBalance) / (oldBalance + tradeBalance)|
                |exit_price|ep1|string|True|The exit price of the position, expressed in `9` decimals<br>Whenever decreasing the balance of a position, the exit price is updated to the new average exit price<br>newExitPrice = (oldExitPrice * oldExitBalance + tradePrice * tradeBalance) / (oldExitBalance + tradeBalance)|
                |mark_price|mp|string|True|The mark price of the position, expressed in `9` decimals|
                |unrealized_pnl|up|string|True|The unrealized PnL of the position, expressed in quote asset decimal units<br>unrealizedPnl = (markPrice - entryPrice) * balance|
                |realized_pnl|rp|string|True|The realized PnL of the position, expressed in quote asset decimal units<br>realizedPnl = (exitPrice - entryPrice) * exitBalance|
                |pnl|p|string|True|The total PnL of the position, expressed in quote asset decimal units<br>totalPnl = realizedPnl + unrealizedPnl|
                |roi|r|string|True|The ROI of the position, expressed as a percentage<br>roi = (pnl / (entryPrice * balance)) * 100|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "results": {
                "event_time": "1697788800000000000",
                "sub_account_id": "2927361400114782",
                "margin_type": "SIMPLE_CROSS_MARGIN",
                "quote_currency": "USDT",
                "unrealized_pnl": "123456.78",
                "total_value": "123456.78",
                "initial_margin": "123456.78",
                "maintanence_margin": "123456.78",
                "available_margin": "123456.78",
                "spot_balances": {
                    "currency": "USDT",
                    "balance": "123456.78"
                },
                "positions": {
                    "event_time": "1697788800000000000",
                    "sub_account_id": "2927361400114782",
                    "instrument": "BTC_USDT_Perp",
                    "balance": "2635000.50",
                    "value": "2635000.50",
                    "entry_price": "65038.01",
                    "exit_price": "65038.01",
                    "mark_price": "65038.01",
                    "unrealized_pnl": "135000.50",
                    "realized_pnl": "-35000.30",
                    "pnl": "100000.20",
                    "roi": "10.20"
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/account_summary' \
        --data '{
            "sub_account_id": "2927361400114782"
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/account_summary' \
        --data '{
            "sub_account_id": "2927361400114782"
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/account_summary' \
        --data '{
            "sub_account_id": "2927361400114782"
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/account_summary' \
        --data '{
            "sub_account_id": "2927361400114782"
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
        The request to get the history of a sub account<br>        SubAccount Summary values are snapshotted once every hour<br>        No snapshots are taken if the sub account has no activity in the hourly window<br>        The history is returned in reverse chronological order<br>        History is preserved only for the last 30 days<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The sub account ID to request for|
        |start_time|st|string|True|Start time of sub account history in unix nanoseconds|
        |end_time|et|string|True|End time of sub account history in unix nanoseconds|
        |cursor|c|string|True|The cursor to indicate when to start the next query from|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "sub_account_id": "2927361400114782",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "cursor": "Qw0918="
        }
        ```
        ```json
        {
            "sa": "2927361400114782",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "c": "Qw0918="
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiSubAccountHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |total|t|number|True|The total number of sub account snapshots matching the request filter|
        |next|n|string|True|The cursor to indicate when to start the next query from|
        |results|r|SubAccount|True|The sub account history matching the request sub account|
        ??? info "SubAccount"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |sub_account_id|sa|string|True|The sub account ID this entry refers to|
            |margin_type|mt|MarginType|True|The type of margin algorithm this subaccount uses|
            |quote_currency|qc|Currency|True|The Quote Currency that this Sub Account is denominated in<br>This subaccount can only open derivative positions denominated in this quote currency<br>All other assets are converted to this quote currency for the purpose of calculating margin<br>In the future, when users select a Multi-Currency Margin Type, this will be USD|
            |unrealized_pnl|up|string|True|The total unrealized PnL of all positions owned by this subaccount, denominated in quote currency decimal units|
            |total_value|tv|string|True|The total value across all spot assets, or in other words, the current margin |
            |initial_margin|im|string|True|The initial margin requirement of all positions owned by this vault, denominated in quote currency decimal units|
            |maintanence_margin|mm|string|True|The maintanence margin requirement of all positions owned by this vault, denominated in quote currency decimal units|
            |available_margin|am|string|True|The margin available for withdrawal, denominated in quote currency decimal units|
            |spot_balances|sb|SpotBalance|True|The list of spot assets owned by this sub account, and their balances|
            |positions|p|Positions|True|The list of positions owned by this sub account|
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
                |balance|b|string|True|The balance of the asset, expressed in underlying asset decimal units<br>Must take into account the value of all positions with this quote asset<br>ie. for USDT denominated subaccounts, this is is identical to total balance|
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
                |balance|b|string|True|The balance of the position, expressed in underlying asset decimal units. Negative for short positions|
                |value|v|string|True|The value of the position, negative for short assets, expressed in quote asset decimal units|
                |entry_price|ep|string|True|The entry price of the position, expressed in `9` decimals<br>Whenever increasing the balance of a position, the entry price is updated to the new average entry price<br>newEntryPrice = (oldEntryPrice * oldBalance + tradePrice * tradeBalance) / (oldBalance + tradeBalance)|
                |exit_price|ep1|string|True|The exit price of the position, expressed in `9` decimals<br>Whenever decreasing the balance of a position, the exit price is updated to the new average exit price<br>newExitPrice = (oldExitPrice * oldExitBalance + tradePrice * tradeBalance) / (oldExitBalance + tradeBalance)|
                |mark_price|mp|string|True|The mark price of the position, expressed in `9` decimals|
                |unrealized_pnl|up|string|True|The unrealized PnL of the position, expressed in quote asset decimal units<br>unrealizedPnl = (markPrice - entryPrice) * balance|
                |realized_pnl|rp|string|True|The realized PnL of the position, expressed in quote asset decimal units<br>realizedPnl = (exitPrice - entryPrice) * exitBalance|
                |pnl|p|string|True|The total PnL of the position, expressed in quote asset decimal units<br>totalPnl = realizedPnl + unrealizedPnl|
                |roi|r|string|True|The ROI of the position, expressed as a percentage<br>roi = (pnl / (entryPrice * balance)) * 100|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "total": 52,
            "next": "Qw0918=",
            "results": {
                "event_time": "1697788800000000000",
                "sub_account_id": "2927361400114782",
                "margin_type": "SIMPLE_CROSS_MARGIN",
                "quote_currency": "USDT",
                "unrealized_pnl": "123456.78",
                "total_value": "123456.78",
                "initial_margin": "123456.78",
                "maintanence_margin": "123456.78",
                "available_margin": "123456.78",
                "spot_balances": {
                    "currency": "USDT",
                    "balance": "123456.78"
                },
                "positions": {
                    "event_time": "1697788800000000000",
                    "sub_account_id": "2927361400114782",
                    "instrument": "BTC_USDT_Perp",
                    "balance": "2635000.50",
                    "value": "2635000.50",
                    "entry_price": "65038.01",
                    "exit_price": "65038.01",
                    "mark_price": "65038.01",
                    "unrealized_pnl": "135000.50",
                    "realized_pnl": "-35000.30",
                    "pnl": "100000.20",
                    "roi": "10.20"
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
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/account_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/account_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/account_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "cursor": "Qw0918="
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/account_history' \
        --data '{
            "sub_account_id": "2927361400114782",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "cursor": "Qw0918="
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
    !!! example
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
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |main_account_id|ma|string|True|The main account ID of the account to which the summary belongs|
        |total_equity|te|string|True|Total equity of the account, denominated in USD|
        |spot_balances|sb|SpotBalance|True|The list of spot assets owned by this sub account, and their balances|
        |mark_prices|mp|MarkPrice|True|The list of mark prices for the assets owned by this account|
        ??? info "SpotBalance"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |currency|c|Currency|True|The currency you hold a spot balance in|
            |balance|b|string|True|The balance of the asset, expressed in underlying asset decimal units<br>Must take into account the value of all positions with this quote asset<br>ie. for USDT denominated subaccounts, this is is identical to total balance|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
        ??? info "MarkPrice"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |currency|c|Currency|True|The currency you hold a spot balance in|
            |mark_price|mp|string|True|The mark price of the asset, expressed in `9` decimals|
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
    !!! example
        ```json
        {
            "main_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "total_equity": "3945034.23",
            "spot_balances": {
                "currency": "USDT",
                "balance": "123456.78"
            },
            "mark_prices": {
                "currency": "USDT",
                "mark_price": 65000.1
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/aggregated_account_summary' \
        --data '{
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/aggregated_account_summary' \
        --data '{
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/aggregated_account_summary' \
        --data '{
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/aggregated_account_summary' \
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
    !!! example
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
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |main_account_id|ma|string|True|The main account ID of the account to which the summary belongs|
        |total_equity|te|string|True|Total equity of the account, denominated in USD|
        |spot_balances|sb|SpotBalance|True|The list of spot assets owned by this account, and their balances|
        |mark_prices|mp|MarkPrice|True|The list of mark prices for the assets owned by this account|
        ??? info "SpotBalance"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |currency|c|Currency|True|The currency you hold a spot balance in|
            |balance|b|string|True|The balance of the asset, expressed in underlying asset decimal units<br>Must take into account the value of all positions with this quote asset<br>ie. for USDT denominated subaccounts, this is is identical to total balance|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
        ??? info "MarkPrice"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |currency|c|Currency|True|The currency you hold a spot balance in|
            |mark_price|mp|string|True|The mark price of the asset, expressed in `9` decimals|
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
    !!! example
        ```json
        {
            "main_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "total_equity": "3945034.23",
            "spot_balances": {
                "currency": "USDT",
                "balance": "123456.78"
            },
            "mark_prices": {
                "currency": "USDT",
                "mark_price": 65000.1
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|InternalServerErr|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        {
            "code":1001,
            "message":"InternalServerErr",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        curl --location 'https://trades.dev.gravitymarkets.io/full/v1/funding_account_summary' \
        --data '{
        }
        '
        ```
    !!! info "stg"
        ```bash
        curl --location 'https://trades.stg.gravitymarkets.io/full/v1/funding_account_summary' \
        --data '{
        }
        '
        ```
    !!! info "testnet"
        ```bash
        curl --location 'https://trades.testnet.grvt.io/full/v1/funding_account_summary' \
        --data '{
        }
        '
        ```
    !!! info "prod"
        ```bash
        curl --location 'https://trades.grvt.io/full/v1/funding_account_summary' \
        --data '{
        }
        '
        ```
<hr class="solid">