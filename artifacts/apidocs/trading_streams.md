# Trading Websocket Streams

## Order
### Order
```
STREAM: v1.order
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderFeedSelectorV1"
        Subscribes to a feed of order updates pertaining to orders made by your account.<br>Each Order can be uniquely identified by its `order_id` or `client_order_id`.<br>To subscribe to all orders, specify an empty `instrument` (eg. `2345123`).<br>Otherwise, specify the `instrument` to only receive orders for that instrument (eg. `2345123-BTC_USDT_Perp`).<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
        |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
    ??? info "WSRequestV1"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "WSResponseV1"
        All V1 Websocket Responses are housed in this wrapper. It returns a confirmation of the JSON RPC subscribe request.<br>If a `request_id` is supplied in the JSON RPC request, it will be propagated back in this JSON RPC response.<br>To ensure you always know if you have missed any payloads, GRVT servers apply the following heuristics to sequence numbers:<ul><li>All snapshot payloads will have a sequence number of `0`. All delta payloads will have a sequence number of `1+`. So its easy to distinguish between snapshots, and deltas</li><li>Num snapshots returned in Response (per stream): You can ensure that you received the right number of snapshots</li><li>First sequence number returned in Response (per stream): You can ensure that you received the first stream, without gaps from snapshots</li><li>Sequence numbers should always monotonically increase by `1`. If it decreases, or increases by more than `1`. Please reconnect</li><li>Duplicate sequence numbers are possible due to network retries. If you receive a duplicate, please ignore it, or idempotently re-update it.</li></ul><br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |subs<br>`s1` |[string]|True|The list of feeds subscribed to|
        |unsubs<br>`u` |[string]|True|The list of feeds unsubscribed from|
        |num_snapshots<br>`ns` |[number]|True|The number of snapshot payloads to expect for each subscribed feed. Returned in same order as `subs`|
        |first_sequence_number<br>`fs` |[string]|True|The first sequence number to expect for each subscribed feed. Returned in same order as `subs`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.order",
            "subs":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderFeedDataV1"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Order|True|The order object being created or updated|
        ??? info "Order"
            Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.<br>GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.<br>This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.<br>Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.<br><br>All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.<br>This minimizes the amount of trust users have to offer to GRVT<br>

            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |order_id<br>`oi` |string|False<br>`0`|[Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |sub_account_id<br>`sa` |string|True|The subaccount initiating the order|
            |is_market<br>`im` |boolean|False<br>`false`|If the order is a market order<br>Market Orders do not have a limit price, and are always executed according to the maker order price.<br>Market Orders must always be taker orders|
            |time_in_force<br>`ti` |TimeInForce|True|Four supported types of orders: GTT, IOC, AON, FOK:<ul><br><li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li><br><li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li><br><li>TAKER ONLY = IOC / FOK - only allows taker orders</li><br><li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li><br></ul>Exchange only supports (GTT, IOC, FOK)<br>RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)|
            |post_only<br>`po` |boolean|False<br>`false`|If True, Order must be a maker order. It has to fill the orderbook instead of match it.<br>If False, Order can be either a maker or taker order.<br><br>|               | Must Fill All | Can Fill Partial |<br>| -             | -             | -                |<br>| Must Be Taker | FOK + False   | IOC + False      |<br>| Can Be Either | AON + False   | GTC + False      |<br>| Must Be Maker | AON + True    | GTC + True       |<br>|
            |reduce_only<br>`ro` |boolean|False<br>`false`|If True, Order must reduce the position size, or be cancelled|
            |legs<br>`l` |[OrderLeg]|True|The legs present in this order<br>The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice|
            |signature<br>`s` |Signature|True|The signature approving this order|
            |metadata<br>`m` |OrderMetadata|True|Order Metadata, ignored by the smart contract, and unsigned by the client|
            |state<br>`s1` |OrderState|False<br>`''`|[Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client|
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
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |instrument<br>`i` |string|True|The instrument to trade in this leg|
                |size<br>`s` |string|True|The total number of assets to trade in this leg, expressed in base asset decimal units.|
                |limit_price<br>`lp` |string|False<br>`0`|The limit price of the order leg, expressed in `9` decimals.<br>This is the number of quote currency units to pay/receive for this leg.<br>This should be `null/0` if the order is a market order|
                |is_buying_asset<br>`ib` |boolean|True|Specifies if the order leg is a buy or sell|
            ??? info "Signature"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |signer<br>`s` |string|True|The address (public key) of the wallet signing the payload|
                |r<br>`r` |string|True|Signature R|
                |s<br>`s1` |string|True|Signature S|
                |v<br>`v` |number|True|Signature V|
                |expiration<br>`e` |string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce<br>`n` |number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
            ??? info "OrderMetadata"
                Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |client_order_id<br>`co` |string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
                |create_time<br>`ct` |string|False<br>`0`|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
            ??? info "OrderState"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |status<br>`s` |OrderStatus|True|The status of the order|
                |reject_reason<br>`rr` |OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size<br>`bs` |[string]|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size<br>`ts` |[string]|True|The total number of assets traded. Sorted in same order as Order.Legs|
                |update_time<br>`ut` |string|True|Time at which the order was updated by GRVT, expressed in unix nanoseconds|
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .linenums="1" .copy }
        {
            "stream": "v1.order",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
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
        ``` { .json .linenums="1" .copy }
        {
            "s": "v1.order",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
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
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3020|400|Sub account ID must be an uint64 integer|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .linenums="1" .copy }
        {
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        {
            "code":1001,
            "message":"You are not authorized to access this functionality",
            "status":403
        }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1101,
            "message":"Feed Format must be in the format of <primary>@<secondary>",
            "status":400
        }
        {
            "code":1102,
            "message":"Wrong number of primary selectors",
            "status":400
        }
        {
            "code":1103,
            "message":"Wrong number of secondary selectors",
            "status":400
        }
        {
            "code":3000,
            "message":"Instrument is invalid",
            "status":400
        }
        {
            "code":3020,
            "message":"Sub account ID must be an uint64 integer",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.order",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
### Order State
```
STREAM: v1.state
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderStateFeedSelectorV1"
        Subscribes to a feed of order updates pertaining to orders made by your account.<br>Unlike the Order Stream, this only streams state updates, drastically improving throughput, and latency.<br>Each Order can be uniquely identified by its `order_id` or `client_order_id`.<br>To subscribe to all orders, specify an empty `instrument` (eg. `2345123`).<br>Otherwise, specify the `instrument` to only receive orders for that instrument (eg. `2345123-BTC_USDT_Perp`).<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
        |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
    ??? info "WSRequestV1"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "WSResponseV1"
        All V1 Websocket Responses are housed in this wrapper. It returns a confirmation of the JSON RPC subscribe request.<br>If a `request_id` is supplied in the JSON RPC request, it will be propagated back in this JSON RPC response.<br>To ensure you always know if you have missed any payloads, GRVT servers apply the following heuristics to sequence numbers:<ul><li>All snapshot payloads will have a sequence number of `0`. All delta payloads will have a sequence number of `1+`. So its easy to distinguish between snapshots, and deltas</li><li>Num snapshots returned in Response (per stream): You can ensure that you received the right number of snapshots</li><li>First sequence number returned in Response (per stream): You can ensure that you received the first stream, without gaps from snapshots</li><li>Sequence numbers should always monotonically increase by `1`. If it decreases, or increases by more than `1`. Please reconnect</li><li>Duplicate sequence numbers are possible due to network retries. If you receive a duplicate, please ignore it, or idempotently re-update it.</li></ul><br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |subs<br>`s1` |[string]|True|The list of feeds subscribed to|
        |unsubs<br>`u` |[string]|True|The list of feeds unsubscribed from|
        |num_snapshots<br>`ns` |[number]|True|The number of snapshot payloads to expect for each subscribed feed. Returned in same order as `subs`|
        |first_sequence_number<br>`fs` |[string]|True|The first sequence number to expect for each subscribed feed. Returned in same order as `subs`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.state",
            "subs":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderStateFeedDataV1"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |OrderStateFeed|True|The Order State Feed|
        ??? info "OrderStateFeed"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |order_id<br>`oi` |string|True|A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
            |client_order_id<br>`co` |string|True|A unique identifier for the active order within a subaccount, specified by the client|
            |order_state<br>`os` |OrderState|True|The order state object being created or updated|
            ??? info "OrderState"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |status<br>`s` |OrderStatus|True|The status of the order|
                |reject_reason<br>`rr` |OrderRejectReason|True|The reason for rejection or cancellation|
                |book_size<br>`bs` |[string]|True|The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs|
                |traded_size<br>`ts` |[string]|True|The total number of assets traded. Sorted in same order as Order.Legs|
                |update_time<br>`ut` |string|True|Time at which the order was updated by GRVT, expressed in unix nanoseconds|
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .linenums="1" .copy }
        {
            "stream": "v1.state",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "order_id": "10000101000203040506",
                "client_order_id": "23042",
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
        ``` { .json .linenums="1" .copy }
        {
            "s": "v1.state",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "oi": "10000101000203040506",
                "co": "23042",
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
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3020|400|Sub account ID must be an uint64 integer|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .linenums="1" .copy }
        {
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        {
            "code":1001,
            "message":"You are not authorized to access this functionality",
            "status":403
        }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1101,
            "message":"Feed Format must be in the format of <primary>@<secondary>",
            "status":400
        }
        {
            "code":1102,
            "message":"Wrong number of primary selectors",
            "status":400
        }
        {
            "code":1103,
            "message":"Wrong number of secondary selectors",
            "status":400
        }
        {
            "code":3000,
            "message":"Instrument is invalid",
            "status":400
        }
        {
            "code":3020,
            "message":"Sub account ID must be an uint64 integer",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.state",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
## Execution
### Fill
```
STREAM: v1.fill
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSFillFeedSelectorV1"
        Subscribes to a feed of private trade updates. This happens when a trade is executed.<br>To subscribe to all private trades, specify an empty `instrument` (eg. `2345123`).<br>Otherwise, specify the `instrument` to only receive private trades for that instrument (eg. `2345123-BTC_USDT_Perp`).<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |sub_account_id<br>`sa` |string|True|The sub account ID to request for|
        |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
    ??? info "WSRequestV1"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "WSResponseV1"
        All V1 Websocket Responses are housed in this wrapper. It returns a confirmation of the JSON RPC subscribe request.<br>If a `request_id` is supplied in the JSON RPC request, it will be propagated back in this JSON RPC response.<br>To ensure you always know if you have missed any payloads, GRVT servers apply the following heuristics to sequence numbers:<ul><li>All snapshot payloads will have a sequence number of `0`. All delta payloads will have a sequence number of `1+`. So its easy to distinguish between snapshots, and deltas</li><li>Num snapshots returned in Response (per stream): You can ensure that you received the right number of snapshots</li><li>First sequence number returned in Response (per stream): You can ensure that you received the first stream, without gaps from snapshots</li><li>Sequence numbers should always monotonically increase by `1`. If it decreases, or increases by more than `1`. Please reconnect</li><li>Duplicate sequence numbers are possible due to network retries. If you receive a duplicate, please ignore it, or idempotently re-update it.</li></ul><br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |subs<br>`s1` |[string]|True|The list of feeds subscribed to|
        |unsubs<br>`u` |[string]|True|The list of feeds unsubscribed from|
        |num_snapshots<br>`ns` |[number]|True|The number of snapshot payloads to expect for each subscribed feed. Returned in same order as `subs`|
        |first_sequence_number<br>`fs` |[string]|True|The first sequence number to expect for each subscribed feed. Returned in same order as `subs`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.fill",
            "subs":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSFillFeedDataV1"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|The websocket channel to which the response is sent|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Fill|True|A private trade matching the request filter|
        ??? info "Fill"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
            |sub_account_id<br>`sa` |string|True|The sub account ID that participated in the trade|
            |instrument<br>`i` |string|True|The instrument being represented|
            |is_buyer<br>`ib` |boolean|True|The side that the subaccount took on the trade|
            |is_taker<br>`it` |boolean|True|The role that the subaccount took on the trade|
            |size<br>`s` |string|True|The number of assets being traded, expressed in base asset decimal units|
            |price<br>`p` |string|True|The traded price, expressed in `9` decimals|
            |mark_price<br>`mp` |string|True|The mark price of the instrument at point of trade, expressed in `9` decimals|
            |index_price<br>`ip` |string|True|The index price of the instrument at point of trade, expressed in `9` decimals|
            |interest_rate<br>`ir` |string|True|The interest rate of the underlying at point of trade, expressed in centibeeps (1/100th of a basis point)|
            |forward_price<br>`fp` |string|True|[Options] The forward price of the option at point of trade, expressed in `9` decimals|
            |realized_pnl<br>`rp` |string|True|The realized PnL of the trade, expressed in quote asset decimal units (0 if increasing position size)|
            |fee<br>`f` |string|True|The fees paid on the trade, expressed in quote asset decimal unit (negative if maker rebate applied)|
            |fee_rate<br>`fr` |string|True|The fee rate paid on the trade|
            |trade_id<br>`ti` |string|True|A trade identifier, globally unique, and monotonically increasing (not by `1`).<br>All trades sharing a single taker execution share the same first component (before `:`), and `event_time`.<br>`trade_id` is guaranteed to be consistent across MarketData `Trade` and Trading `Fill`.|
            |order_id<br>`oi` |string|True|An order identifier|
            |venue<br>`v` |Venue|True|The venue where the trade occurred|
            |client_order_id<br>`co` |string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
            ??? info "Venue"
                The list of Trading Venues that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`ORDERBOOK` = 1|the trade is cleared on the orderbook venue|
                |`RFQ` = 2|the trade is cleared on the RFQ venue|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .linenums="1" .copy }
        {
            "stream": "v1.fill",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
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
                "trade_id": "209358:2",
                "order_id": "0x10000101000203040506",
                "venue": "ORDERBOOK",
                "client_order_id": "23042"
            }
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "s": "v1.fill",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
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
                "ti": "209358:2",
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
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3020|400|Sub account ID must be an uint64 integer|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .linenums="1" .copy }
        {
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        {
            "code":1001,
            "message":"You are not authorized to access this functionality",
            "status":403
        }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1101,
            "message":"Feed Format must be in the format of <primary>@<secondary>",
            "status":400
        }
        {
            "code":1102,
            "message":"Wrong number of primary selectors",
            "status":400
        }
        {
            "code":1103,
            "message":"Wrong number of secondary selectors",
            "status":400
        }
        {
            "code":3000,
            "message":"Instrument is invalid",
            "status":400
        }
        {
            "code":3020,
            "message":"Sub account ID must be an uint64 integer",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.fill",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
### Positions
```
STREAM: v1.position
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSPositionsFeedSelectorV1"
        Subscribes to a feed of position updates. This happens when a trade is executed.<br>To subscribe to all positions, specify an empty `instrument` (eg. `2345123`).<br>Otherwise, specify the `instrument` to only receive positions for that instrument (eg. `2345123-BTC_USDT_Perp`).<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
        |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
    ??? info "WSRequestV1"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "WSResponseV1"
        All V1 Websocket Responses are housed in this wrapper. It returns a confirmation of the JSON RPC subscribe request.<br>If a `request_id` is supplied in the JSON RPC request, it will be propagated back in this JSON RPC response.<br>To ensure you always know if you have missed any payloads, GRVT servers apply the following heuristics to sequence numbers:<ul><li>All snapshot payloads will have a sequence number of `0`. All delta payloads will have a sequence number of `1+`. So its easy to distinguish between snapshots, and deltas</li><li>Num snapshots returned in Response (per stream): You can ensure that you received the right number of snapshots</li><li>First sequence number returned in Response (per stream): You can ensure that you received the first stream, without gaps from snapshots</li><li>Sequence numbers should always monotonically increase by `1`. If it decreases, or increases by more than `1`. Please reconnect</li><li>Duplicate sequence numbers are possible due to network retries. If you receive a duplicate, please ignore it, or idempotently re-update it.</li></ul><br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |subs<br>`s1` |[string]|True|The list of feeds subscribed to|
        |unsubs<br>`u` |[string]|True|The list of feeds unsubscribed from|
        |num_snapshots<br>`ns` |[number]|True|The number of snapshot payloads to expect for each subscribed feed. Returned in same order as `subs`|
        |first_sequence_number<br>`fs` |[string]|True|The first sequence number to expect for each subscribed feed. Returned in same order as `subs`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.position",
            "subs":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSPositionsFeedDataV1"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Positions|True|A Position being created or updated matching the request filter|
        ??? info "Positions"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
            |sub_account_id<br>`sa` |string|True|The sub account ID that participated in the trade|
            |instrument<br>`i` |string|True|The instrument being represented|
            |size<br>`s` |string|True|The size of the position, expressed in base asset decimal units. Negative for short positions|
            |notional<br>`n` |string|True|The notional value of the position, negative for short assets, expressed in quote asset decimal units|
            |entry_price<br>`ep` |string|True|The entry price of the position, expressed in `9` decimals<br>Whenever increasing the size of a position, the entry price is updated to the new average entry price<br>`new_entry_price = (old_entry_price * old_size + trade_price * trade_size) / (old_size + trade_size)`|
            |exit_price<br>`ep1` |string|True|The exit price of the position, expressed in `9` decimals<br>Whenever decreasing the size of a position, the exit price is updated to the new average exit price<br>`new_exit_price = (old_exit_price * old_exit_trade_size + trade_price * trade_size) / (old_exit_trade_size + trade_size)`|
            |mark_price<br>`mp` |string|True|The mark price of the position, expressed in `9` decimals|
            |unrealized_pnl<br>`up` |string|True|The unrealized PnL of the position, expressed in quote asset decimal units<br>`unrealized_pnl = (mark_price - entry_price) * size`|
            |realized_pnl<br>`rp` |string|True|The realized PnL of the position, expressed in quote asset decimal units<br>`realized_pnl = (exit_price - entry_price) * exit_trade_size`|
            |total_pnl<br>`tp` |string|True|The total PnL of the position, expressed in quote asset decimal units<br>`total_pnl = realized_pnl + unrealized_pnl`|
            |roi<br>`r` |string|True|The ROI of the position, expressed as a percentage<br>`roi = (total_pnl / (entry_price * abs(size))) * 100^`|
            |quote_index_price<br>`qi` |string|True|The index price of the quote currency. (reported in `USD`)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .linenums="1" .copy }
        {
            "stream": "v1.position",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
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
            }
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "s": "v1.position",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "i": "BTC_USDT_Perp",
                "s": "2635000.50",
                "n": "2635000.50",
                "ep": "65038.01",
                "ep1": "65038.01",
                "mp": "65038.01",
                "up": "135000.50",
                "rp": "-35000.30",
                "tp": "100000.20",
                "r": "10.20",
                "qi": "1.0000102"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3020|400|Sub account ID must be an uint64 integer|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .linenums="1" .copy }
        {
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        {
            "code":1001,
            "message":"You are not authorized to access this functionality",
            "status":403
        }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1101,
            "message":"Feed Format must be in the format of <primary>@<secondary>",
            "status":400
        }
        {
            "code":1102,
            "message":"Wrong number of primary selectors",
            "status":400
        }
        {
            "code":1103,
            "message":"Wrong number of secondary selectors",
            "status":400
        }
        {
            "code":3000,
            "message":"Instrument is invalid",
            "status":400
        }
        {
            "code":3020,
            "message":"Sub account ID must be an uint64 integer",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.position",
            "feed":["'$GRVT_SUB_ACCOUNT_ID'-BTC_USDT_Perp"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
## Transfer
### Deposit
```
STREAM: v1.deposit
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSDepositFeedSelectorV1"
        Subscribes to a feed of deposits. This will execute when there is any deposit to selected account.<br>To subscribe to a main account, specify the account ID (eg. `0x9fe3758b67ce7a2875ee4b452f01a5282d84ed8a`).<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |main_account_id<br>`ma` |string|True|The main account ID to request for|
    ??? info "WSRequestV1"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "WSResponseV1"
        All V1 Websocket Responses are housed in this wrapper. It returns a confirmation of the JSON RPC subscribe request.<br>If a `request_id` is supplied in the JSON RPC request, it will be propagated back in this JSON RPC response.<br>To ensure you always know if you have missed any payloads, GRVT servers apply the following heuristics to sequence numbers:<ul><li>All snapshot payloads will have a sequence number of `0`. All delta payloads will have a sequence number of `1+`. So its easy to distinguish between snapshots, and deltas</li><li>Num snapshots returned in Response (per stream): You can ensure that you received the right number of snapshots</li><li>First sequence number returned in Response (per stream): You can ensure that you received the first stream, without gaps from snapshots</li><li>Sequence numbers should always monotonically increase by `1`. If it decreases, or increases by more than `1`. Please reconnect</li><li>Duplicate sequence numbers are possible due to network retries. If you receive a duplicate, please ignore it, or idempotently re-update it.</li></ul><br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |subs<br>`s1` |[string]|True|The list of feeds subscribed to|
        |unsubs<br>`u` |[string]|True|The list of feeds unsubscribed from|
        |num_snapshots<br>`ns` |[number]|True|The number of snapshot payloads to expect for each subscribed feed. Returned in same order as `subs`|
        |first_sequence_number<br>`fs` |[string]|True|The first sequence number to expect for each subscribed feed. Returned in same order as `subs`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.deposit",
            "subs":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSDepositFeedDataV1"
        Subscribes to a feed of deposit updates.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|The websocket channel to which the response is sent|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Deposit|True|The Deposit object|
        ??? info "Deposit"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |tx_hash<br>`th` |string|True|The hash of the bridgemint event producing the deposit|
            |to_account_id<br>`ta` |string|True|The account to deposit into|
            |currency<br>`c` |Currency|True|The token currency to deposit|
            |num_tokens<br>`nt` |string|True|The number of tokens to deposit|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .linenums="1" .copy }
        {
            "stream": "v1.deposit",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "tx_hash": "0x1234567890123456789012345678901234567890123456789012345678901234",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "10.50"
            }
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "s": "v1.deposit",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "th": "0x1234567890123456789012345678901234567890123456789012345678901234",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
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
        |1001|403|You are not authorized to access this functionality|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .linenums="1" .copy }
        {
            "code":1001,
            "message":"You are not authorized to access this functionality",
            "status":403
        }
        {
            "code":1101,
            "message":"Feed Format must be in the format of <primary>@<secondary>",
            "status":400
        }
        {
            "code":1102,
            "message":"Wrong number of primary selectors",
            "status":400
        }
        {
            "code":1103,
            "message":"Wrong number of secondary selectors",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.deposit",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
### Transfer
```
STREAM: v1.transfer
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSTransferFeedSelectorV1"
        Subscribes to a feed of transfers. This will execute when there is any transfer to or from the selected account.<br>To subscribe to a main account, specify the account ID (eg. `0x9fe3758b67ce7a2875ee4b452f01a5282d84ed8a`).<br>To subscribe to a sub account, specify the main account and the sub account dash separated (eg. `0x9fe3758b67ce7a2875ee4b452f01a5282d84ed8a-1920109784202388`).<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |main_account_id<br>`ma` |string|True|The main account ID to request for|
        |sub_account_id<br>`sa` |string|False<br>`'0'`|The sub account ID to request for|
    ??? info "WSRequestV1"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "WSResponseV1"
        All V1 Websocket Responses are housed in this wrapper. It returns a confirmation of the JSON RPC subscribe request.<br>If a `request_id` is supplied in the JSON RPC request, it will be propagated back in this JSON RPC response.<br>To ensure you always know if you have missed any payloads, GRVT servers apply the following heuristics to sequence numbers:<ul><li>All snapshot payloads will have a sequence number of `0`. All delta payloads will have a sequence number of `1+`. So its easy to distinguish between snapshots, and deltas</li><li>Num snapshots returned in Response (per stream): You can ensure that you received the right number of snapshots</li><li>First sequence number returned in Response (per stream): You can ensure that you received the first stream, without gaps from snapshots</li><li>Sequence numbers should always monotonically increase by `1`. If it decreases, or increases by more than `1`. Please reconnect</li><li>Duplicate sequence numbers are possible due to network retries. If you receive a duplicate, please ignore it, or idempotently re-update it.</li></ul><br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |subs<br>`s1` |[string]|True|The list of feeds subscribed to|
        |unsubs<br>`u` |[string]|True|The list of feeds unsubscribed from|
        |num_snapshots<br>`ns` |[number]|True|The number of snapshot payloads to expect for each subscribed feed. Returned in same order as `subs`|
        |first_sequence_number<br>`fs` |[string]|True|The first sequence number to expect for each subscribed feed. Returned in same order as `subs`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.transfer",
            "subs":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSTransferFeedDataV1"
        Subscribes to a feed of transfer updates.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|The websocket channel to which the response is sent|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Transfer|True|The Transfer object|
        ??? info "Transfer"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |from_account_id<br>`fa` |string|True|The account to transfer from|
            |from_sub_account_id<br>`fs` |string|True|The subaccount to transfer from (0 if transferring from main account)|
            |to_account_id<br>`ta` |string|True|The account to deposit into|
            |to_sub_account_id<br>`ts` |string|True|The subaccount to transfer to (0 if transferring to main account)|
            |currency<br>`c` |Currency|True|The token currency to transfer|
            |num_tokens<br>`nt` |string|True|The number of tokens to transfer|
            |signature<br>`s` |Signature|True|The signature of the transfer|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "Signature"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |signer<br>`s` |string|True|The address (public key) of the wallet signing the payload|
                |r<br>`r` |string|True|Signature R|
                |s<br>`s1` |string|True|Signature S|
                |v<br>`v` |number|True|Signature V|
                |expiration<br>`e` |string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce<br>`n` |number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .linenums="1" .copy }
        {
            "stream": "v1.transfer",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "currency": "USDT",
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
        ``` { .json .linenums="1" .copy }
        {
            "s": "v1.transfer",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                "c": "USDT",
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
        |1001|403|You are not authorized to access this functionality|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3020|400|Sub account ID must be an uint64 integer|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .linenums="1" .copy }
        {
            "code":1001,
            "message":"You are not authorized to access this functionality",
            "status":403
        }
        {
            "code":1101,
            "message":"Feed Format must be in the format of <primary>@<secondary>",
            "status":400
        }
        {
            "code":1102,
            "message":"Wrong number of primary selectors",
            "status":400
        }
        {
            "code":1103,
            "message":"Wrong number of secondary selectors",
            "status":400
        }
        {
            "code":3020,
            "message":"Sub account ID must be an uint64 integer",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.transfer",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'-'$GRVT_SUB_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
### Withdrawal
```
STREAM: v1.withdrawal
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSWithdrawalFeedSelectorV1"
        Subscribes to a feed of withdrawals. This will execute when there is any withdrawal from the selected account.<br>To subscribe to a main account, specify the account ID (eg. `0x9fe3758b67ce7a2875ee4b452f01a5282d84ed8a`).<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |main_account_id<br>`ma` |string|True|The main account ID to request for|
    ??? info "WSRequestV1"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "WSResponseV1"
        All V1 Websocket Responses are housed in this wrapper. It returns a confirmation of the JSON RPC subscribe request.<br>If a `request_id` is supplied in the JSON RPC request, it will be propagated back in this JSON RPC response.<br>To ensure you always know if you have missed any payloads, GRVT servers apply the following heuristics to sequence numbers:<ul><li>All snapshot payloads will have a sequence number of `0`. All delta payloads will have a sequence number of `1+`. So its easy to distinguish between snapshots, and deltas</li><li>Num snapshots returned in Response (per stream): You can ensure that you received the right number of snapshots</li><li>First sequence number returned in Response (per stream): You can ensure that you received the first stream, without gaps from snapshots</li><li>Sequence numbers should always monotonically increase by `1`. If it decreases, or increases by more than `1`. Please reconnect</li><li>Duplicate sequence numbers are possible due to network retries. If you receive a duplicate, please ignore it, or idempotently re-update it.</li></ul><br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |subs<br>`s1` |[string]|True|The list of feeds subscribed to|
        |unsubs<br>`u` |[string]|True|The list of feeds unsubscribed from|
        |num_snapshots<br>`ns` |[number]|True|The number of snapshot payloads to expect for each subscribed feed. Returned in same order as `subs`|
        |first_sequence_number<br>`fs` |[string]|True|The first sequence number to expect for each subscribed feed. Returned in same order as `subs`|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .linenums="1" .copy }
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "subs":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSWithdrawalFeedDataV1"
        Subscribes to a feed of withdrawal updates.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|The websocket channel to which the response is sent|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Withdrawal|True|The Withdrawal object|
        ??? info "Withdrawal"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |from_account_id<br>`fa` |string|True|The subaccount to withdraw from|
            |to_eth_address<br>`te` |string|True|The ethereum address to withdraw to|
            |currency<br>`c` |Currency|True|The token currency to withdraw|
            |num_tokens<br>`nt` |string|True|The number of tokens to withdraw|
            |signature<br>`s` |Signature|True|The signature of the withdrawal|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "Signature"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |signer<br>`s` |string|True|The address (public key) of the wallet signing the payload|
                |r<br>`r` |string|True|Signature R|
                |s<br>`s1` |string|True|Signature S|
                |v<br>`v` |number|True|Signature V|
                |expiration<br>`e` |string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
                |nonce<br>`n` |number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .linenums="1" .copy }
        {
            "stream": "v1.withdrawal",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
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
        ``` { .json .linenums="1" .copy }
        {
            "s": "v1.withdrawal",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
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
        |1001|403|You are not authorized to access this functionality|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .linenums="1" .copy }
        {
            "code":1001,
            "message":"You are not authorized to access this functionality",
            "status":403
        }
        {
            "code":1101,
            "message":"Feed Format must be in the format of <primary>@<secondary>",
            "status":400
        }
        {
            "code":1102,
            "message":"Wrong number of primary selectors",
            "status":400
        }
        {
            "code":1103,
            "message":"Wrong number of secondary selectors",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth.md"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.dev.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.stg.gravitymarkets.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.testnet.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .linenums="1" .copy }
        wscat -c "wss://trades.grvt.io/ws" \
        -H "Cookie: $GRVT_COOKIE" \
        -x '
        {
            "request_id":1,
            "stream":"v1.withdrawal",
            "feed":["'$GRVT_MAIN_ACCOUNT_ID'"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
