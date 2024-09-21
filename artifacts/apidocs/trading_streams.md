# Trading Websocket Streams

## Order
### Order
```
STREAM: v1.order
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderFeedSelectorV1"
        Subscribes to a feed of order updates pertaining to orders made by your account.<br>        Each Order can be uniquely identified by its `order_id` or `client_order_id` (if client designs well).<br>        Use `stateFilter = c` to only receive create events, `stateFilter = u` to only receive update events, and `stateFilter = a` to receive both.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
        |kind|k|Kind|True|The kind filter to apply.|
        |underlying|u|Currency|True|The underlying filter to apply.|
        |quote|q|Currency|True|The quote filter to apply.|
        |state_filter|sf|OrderStateFilter|True|create only, update only, all|
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
        ??? info "OrderStateFilter"
            |Value| Description |
            |-|-|
            |`C` = 1|create only filter|
            |`U` = 2|update only filter|
            |`A` = 3|create and update filter|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.order",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.order",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.order",
            "subs":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|Order|True|The order object being created or updated|
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
            "stream": "v1.order",
            "sequence_number": "872634876",
            "feed": {
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
            "s": "v1.order",
            "sn": "872634876",
            "f": {
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
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.order",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "stg"
        ```bash
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.order",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "testnet"
        ```bash
        wscat -c "wss://trades.testnet.grvt.io/ws" -x '
        {
            "stream":"v1.order",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "prod"
        ```bash
        wscat -c "wss://trades.grvt.io/ws" -x '
        {
            "stream":"v1.order",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">

### Order State
```
STREAM: v1.state
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderStateFeedSelectorV1"
        Subscribes to a feed of order updates pertaining to orders made by your account.<br>        Unlike the Order Stream, this only streams state updates, drastically improving throughput, and latency.<br>        Each Order can be uniquely identified by its `order_id` or `client_order_id` (if client designs well).<br>        Use `stateFilter = c` to only receive create events, `stateFilter = u` to only receive update events, and `stateFilter = a` to receive both.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
        |kind|k|Kind|True|The kind filter to apply.|
        |underlying|u|Currency|True|The underlying filter to apply.|
        |quote|q|Currency|True|The quote filter to apply.|
        |state_filter|sf|OrderStateFilter|True|create only, update only, all|
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
        ??? info "OrderStateFilter"
            |Value| Description |
            |-|-|
            |`C` = 1|create only filter|
            |`U` = 2|update only filter|
            |`A` = 3|create and update filter|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.state",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.state",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.state",
            "subs":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderStateFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|OrderStateFeed|True|The Order State Feed|
        ??? info "OrderStateFeed"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |order_id|oi|string|True|A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |order_state|os|OrderState|True|The order state object being created or updated|
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
            "stream": "v1.state",
            "sequence_number": "872634876",
            "feed": {
                "order_id": "10000101000203040506",
                "order_state": {
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
            "s": "v1.state",
            "sn": "872634876",
            "f": {
                "oi": "10000101000203040506",
                "os": {
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
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.state",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "stg"
        ```bash
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.state",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "testnet"
        ```bash
        wscat -c "wss://trades.testnet.grvt.io/ws" -x '
        {
            "stream":"v1.state",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "prod"
        ```bash
        wscat -c "wss://trades.grvt.io/ws" -x '
        {
            "stream":"v1.state",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT@C"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">

## Trade
### Private Trade
```
STREAM: v1.trade
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSPrivateTradeFeedSelectorV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The sub account ID to request for|
        |kind|k|Kind|True|The kind filter to apply.|
        |underlying|u|Currency|True|The underlying filter to apply.|
        |quote|q|Currency|True|The quote filter to apply.|
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
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.trade",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.trade",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.trade",
            "subs":["2927361400114782-PERPETUAL-BTC-USDT"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSPrivateTradeFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|The websocket channel to which the response is sent|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|PrivateTrade|True|A private trade matching the request filter|
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
            "stream": "v1.trade",
            "sequence_number": "872634876",
            "feed": {
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
        ```json
        {
            "s": "v1.trade",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "sa": "2927361400114782",
                "i": "BTC_USDT_Perp",
                "ib": true,
                "it": true,
                "s": "0.30",
                "p": "65038.01",
                "mp": "65038.01",
                "ip": "65038.01",
                "ir": 0.0003,
                "fp": "65038.01",
                "rp": "2400.50",
                "f": "9.75",
                "fr": 0.0003,
                "ti": "209358",
                "oi": "0x10000101000203040506",
                "v": "ORDERBOOK",
                "co": "23042"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.trade",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "stg"
        ```bash
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.trade",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "testnet"
        ```bash
        wscat -c "wss://trades.testnet.grvt.io/ws" -x '
        {
            "stream":"v1.trade",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "prod"
        ```bash
        wscat -c "wss://trades.grvt.io/ws" -x '
        {
            "stream":"v1.trade",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">

### Positions
```
STREAM: v1.position
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSPositionsFeedSelectorV1"
        Subscribes to a feed of position updates. This happens when a trade is executed.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |sub_account_id|sa|string|True|The subaccount ID to filter by|
        |kind|k|Kind|True|The kind filter to apply.|
        |underlying|u|Currency|True|The underlying filter to apply.|
        |quote|q|Currency|True|The quote filter to apply.|
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
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.position",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.position",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.position",
            "subs":["2927361400114782-PERPETUAL-BTC-USDT"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSPositionsFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|Positions|True|A Position being created or updated matching the request filter|
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
            "stream": "v1.position",
            "sequence_number": "872634876",
            "feed": {
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
        ```json
        {
            "s": "v1.position",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "sa": "2927361400114782",
                "i": "BTC_USDT_Perp",
                "b": "2635000.50",
                "v": "2635000.50",
                "ep": "65038.01",
                "ep1": "65038.01",
                "mp": "65038.01",
                "up": "135000.50",
                "rp": "-35000.30",
                "p": "100000.20",
                "r": "10.20"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.position",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "stg"
        ```bash
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.position",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "testnet"
        ```bash
        wscat -c "wss://trades.testnet.grvt.io/ws" -x '
        {
            "stream":"v1.position",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "prod"
        ```bash
        wscat -c "wss://trades.grvt.io/ws" -x '
        {
            "stream":"v1.position",
            "feed":["2927361400114782-PERPETUAL-BTC-USDT"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">

## Transfer
### Deposit
```
STREAM: v1.deposit
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "EmptyRequest"
        Used for requests that do not require any parameters<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.deposit",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.deposit",
            "feed":[""],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.deposit",
            "subs":[""],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSDepositFeedDataV1"
        Subscribes to a feed of deposit updates.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|The websocket channel to which the response is sent|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|Deposit|True|The Deposit object|
        ??? info "Deposit"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |tx_hash|th|string|True|The hash of the bridgemint event producing the deposit|
            |to_account_id|ta|string|True|The account to deposit into|
            |token_currency|tc|Currency|True|The token currency to deposit|
            |num_tokens|nt|string|True|The number of tokens to deposit|
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
            "stream": "v1.deposit",
            "sequence_number": "872634876",
            "feed": {
                "tx_hash": "0x1234567890123456789012345678901234567890123456789012345678901234",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "token_currency": "USDT",
                "num_tokens": "10.50"
            }
        }
        ```
        ```json
        {
            "s": "v1.deposit",
            "sn": "872634876",
            "f": {
                "th": "0x1234567890123456789012345678901234567890123456789012345678901234",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "tc": "USDT",
                "nt": "10.50"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.deposit",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "stg"
        ```bash
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.deposit",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "testnet"
        ```bash
        wscat -c "wss://trades.testnet.grvt.io/ws" -x '
        {
            "stream":"v1.deposit",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "prod"
        ```bash
        wscat -c "wss://trades.grvt.io/ws" -x '
        {
            "stream":"v1.deposit",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">

### Transfer
```
STREAM: v1.transfer
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "EmptyRequest"
        Used for requests that do not require any parameters<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.transfer",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.transfer",
            "feed":[""],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.transfer",
            "subs":[""],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSTransferFeedDataV1"
        Subscribes to a feed of transfer updates.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|The websocket channel to which the response is sent|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|Transfer|True|The Transfer object|
        ??? info "Transfer"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |from_account_id|fa|string|True|The account to transfer from|
            |from_sub_account_id|fs|string|True|The subaccount to transfer from (0 if transferring from main account)|
            |to_account_id|ta|string|True|The account to deposit into|
            |to_sub_account_id|ts|string|True|The subaccount to transfer to (0 if transferring to main account)|
            |token_currency|tc|Currency|True|The token currency to transfer|
            |num_tokens|nt|string|True|The number of tokens to transfer|
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
            "stream": "v1.transfer",
            "sequence_number": "872634876",
            "feed": {
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "2927361400114782",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "2927361400114782",
                "token_currency": "USDT",
                "num_tokens": "10.50",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                }
            }
        }
        ```
        ```json
        {
            "s": "v1.transfer",
            "sn": "872634876",
            "f": {
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "fs": "2927361400114782",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "ts": "2927361400114782",
                "tc": "USDT",
                "nt": "10.50",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "e": "1697788800000000000",
                    "n": "1234567890"
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.transfer",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "stg"
        ```bash
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.transfer",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "testnet"
        ```bash
        wscat -c "wss://trades.testnet.grvt.io/ws" -x '
        {
            "stream":"v1.transfer",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "prod"
        ```bash
        wscat -c "wss://trades.grvt.io/ws" -x '
        {
            "stream":"v1.transfer",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">

### Withdrawal
```
STREAM: v1.withdrawal
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "EmptyRequest"
        Used for requests that do not require any parameters<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.withdrawal",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.withdrawal",
            "feed":[""],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.withdrawal",
            "subs":[""],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSWithdrawalFeedDataV1"
        Subscribes to a feed of withdrawal updates.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|The websocket channel to which the response is sent|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|Withdrawal|True|The Withdrawal object|
        ??? info "Withdrawal"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |from_account_id|fa|string|True|The subaccount to withdraw from|
            |to_eth_address|te|string|True|The ethereum address to withdraw to|
            |token_currency|tc|Currency|True|The token currency to withdraw|
            |num_tokens|nt|string|True|The number of tokens to withdraw|
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
            "stream": "v1.withdrawal",
            "sequence_number": "872634876",
            "feed": {
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "token_currency": "USDT",
                "num_tokens": "10.50",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "expiration": "1697788800000000000",
                    "nonce": "1234567890"
                }
            }
        }
        ```
        ```json
        {
            "s": "v1.withdrawal",
            "sn": "872634876",
            "f": {
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "tc": "USDT",
                "nt": "10.50",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": "28",
                    "e": "1697788800000000000",
                    "n": "1234567890"
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! example
        ```json
        ```
    </section>
=== "Try it out"
    !!! info "dev"
        ```bash
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.withdrawal",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "stg"
        ```bash
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" -x '
        {
            "stream":"v1.withdrawal",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "testnet"
        ```bash
        wscat -c "wss://trades.testnet.grvt.io/ws" -x '
        {
            "stream":"v1.withdrawal",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! info "prod"
        ```bash
        wscat -c "wss://trades.grvt.io/ws" -x '
        {
            "stream":"v1.withdrawal",
            "feed":[""],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
