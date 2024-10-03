# MarketData Websocket Streams

## Ticker
### Mini Ticker Snap
```
STREAM: v1.mini.s
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSMiniTickerFeedSelectorV1](/../../schemas/ws_mini_ticker_feed_selector_v1)"
        Subscribes to a mini ticker feed for a single instrument. The `mini.s` channel offers simpler integration. To experience higher publishing rates, please use the `mini.d` channel.<br>Unlike the `mini.d` channel which publishes an initial snapshot, then only streams deltas after, the `mini.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the mini ticker.</li><li>After the snapshot, the server will only send deltas of the mini ticker.</li><li>The server will send a delta if any of the fields in the mini ticker have changed.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |rate<br>`r` |number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (0 - `raw`, 50, 100, 200, 500, 1000, 5000)<br>Snapshot (200, 500, 1000, 5000)|
    ??? info "[WSRequestV1](/../../schemas/ws_request_v1)"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "[WSResponseV1](/../../schemas/ws_response_v1)"
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
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSMiniTickerFeedDataV1](/../../schemas/ws_mini_ticker_feed_data_v1)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |MiniTicker|True|A mini ticker matching the request filter|
        ??? info "[MiniTicker](/../../schemas/mini_ticker)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|False<br>`None`|Time at which the event was emitted in unix nanoseconds|
            |instrument<br>`i` |string|False<br>`None`|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |mark_price<br>`mp` |string|False<br>`None`|The mark price of the instrument, expressed in `9` decimals|
            |index_price<br>`ip` |string|False<br>`None`|The index price of the instrument, expressed in `9` decimals|
            |last_price<br>`lp` |string|False<br>`None`|The last traded price of the instrument (also close price), expressed in `9` decimals|
            |last_size<br>`ls` |string|False<br>`None`|The number of assets traded in the last trade, expressed in base asset decimal units|
            |mid_price<br>`mp1` |string|False<br>`None`|The mid price of the instrument, expressed in `9` decimals|
            |best_bid_price<br>`bb` |string|False<br>`None`|The best bid price of the instrument, expressed in `9` decimals|
            |best_bid_size<br>`bb1` |string|False<br>`None`|The number of assets offered on the best bid price of the instrument, expressed in base asset decimal units|
            |best_ask_price<br>`ba` |string|False<br>`None`|The best ask price of the instrument, expressed in `9` decimals|
            |best_ask_size<br>`ba1` |string|False<br>`None`|The number of assets offered on the best ask price of the instrument, expressed in base asset decimal units|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "stream": "v1.mini.s",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "event_time": "1697788800000000000",
                "instrument": "BTC_USDT_Perp",
                "mark_price": "65038.01",
                "index_price": "65038.01",
                "last_price": "65038.01",
                "last_size": "123456.78",
                "mid_price": "65038.01",
                "best_bid_price": "65038.01",
                "best_bid_size": "123456.78",
                "best_ask_price": "65038.01",
                "best_ask_size": "123456.78"
            }
        }
        ```
        ``` { .json .copy }
        {
            "s": "v1.mini.s",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "i": "BTC_USDT_Perp",
                "mp": "65038.01",
                "ip": "65038.01",
                "lp": "65038.01",
                "ls": "123456.78",
                "mp1": "65038.01",
                "bb": "65038.01",
                "bb1": "123456.78",
                "ba": "65038.01",
                "ba1": "123456.78"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1004|404|Data Not Found|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3030|400|Feed rate is invalid|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .copy }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
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
            "code":3030,
            "message":"Feed rate is invalid",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
### Mini Ticker Delta
```
STREAM: v1.mini.d
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSMiniTickerFeedSelectorV1](/../../schemas/ws_mini_ticker_feed_selector_v1)"
        Subscribes to a mini ticker feed for a single instrument. The `mini.s` channel offers simpler integration. To experience higher publishing rates, please use the `mini.d` channel.<br>Unlike the `mini.d` channel which publishes an initial snapshot, then only streams deltas after, the `mini.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the mini ticker.</li><li>After the snapshot, the server will only send deltas of the mini ticker.</li><li>The server will send a delta if any of the fields in the mini ticker have changed.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |rate<br>`r` |number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (0 - `raw`, 50, 100, 200, 500, 1000, 5000)<br>Snapshot (200, 500, 1000, 5000)|
    ??? info "[WSRequestV1](/../../schemas/ws_request_v1)"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "[WSResponseV1](/../../schemas/ws_response_v1)"
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
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSMiniTickerFeedDataV1](/../../schemas/ws_mini_ticker_feed_data_v1)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |MiniTicker|True|A mini ticker matching the request filter|
        ??? info "[MiniTicker](/../../schemas/mini_ticker)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|False<br>`None`|Time at which the event was emitted in unix nanoseconds|
            |instrument<br>`i` |string|False<br>`None`|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |mark_price<br>`mp` |string|False<br>`None`|The mark price of the instrument, expressed in `9` decimals|
            |index_price<br>`ip` |string|False<br>`None`|The index price of the instrument, expressed in `9` decimals|
            |last_price<br>`lp` |string|False<br>`None`|The last traded price of the instrument (also close price), expressed in `9` decimals|
            |last_size<br>`ls` |string|False<br>`None`|The number of assets traded in the last trade, expressed in base asset decimal units|
            |mid_price<br>`mp1` |string|False<br>`None`|The mid price of the instrument, expressed in `9` decimals|
            |best_bid_price<br>`bb` |string|False<br>`None`|The best bid price of the instrument, expressed in `9` decimals|
            |best_bid_size<br>`bb1` |string|False<br>`None`|The number of assets offered on the best bid price of the instrument, expressed in base asset decimal units|
            |best_ask_price<br>`ba` |string|False<br>`None`|The best ask price of the instrument, expressed in `9` decimals|
            |best_ask_size<br>`ba1` |string|False<br>`None`|The number of assets offered on the best ask price of the instrument, expressed in base asset decimal units|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "stream": "v1.mini.s",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "event_time": "1697788800000000000",
                "instrument": "BTC_USDT_Perp",
                "mark_price": "65038.01",
                "index_price": "65038.01",
                "last_price": "65038.01",
                "last_size": "123456.78",
                "mid_price": "65038.01",
                "best_bid_price": "65038.01",
                "best_bid_size": "123456.78",
                "best_ask_price": "65038.01",
                "best_ask_size": "123456.78"
            }
        }
        ```
        ``` { .json .copy }
        {
            "s": "v1.mini.s",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "i": "BTC_USDT_Perp",
                "mp": "65038.01",
                "ip": "65038.01",
                "lp": "65038.01",
                "ls": "123456.78",
                "mp1": "65038.01",
                "bb": "65038.01",
                "bb1": "123456.78",
                "ba": "65038.01",
                "ba1": "123456.78"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1004|404|Data Not Found|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3030|400|Feed rate is invalid|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .copy }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
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
            "code":3030,
            "message":"Feed rate is invalid",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
### Ticker Snap
```
STREAM: v1.ticker.s
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSTickerFeedSelectorV1](/../../schemas/ws_ticker_feed_selector_v1)"
        Subscribes to a ticker feed for a single instrument. The `ticker.s` channel offers simpler integration. To experience higher publishing rates, please use the `ticker.d` channel.<br>Unlike the `ticker.d` channel which publishes an initial snapshot, then only streams deltas after, the `ticker.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the ticker.</li><li>After the snapshot, the server will only send deltas of the ticker.</li><li>The server will send a delta if any of the fields in the ticker have changed.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |rate<br>`r` |number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (100, 200, 500, 1000, 5000)<br>Snapshot (500, 1000, 5000)|
    ??? info "[WSRequestV1](/../../schemas/ws_request_v1)"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "[WSResponseV1](/../../schemas/ws_response_v1)"
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
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSTickerFeedDataV1](/../../schemas/ws_ticker_feed_data_v1)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Ticker|True|A ticker matching the request filter|
        ??? info "[Ticker](/../../schemas/ticker)"
            Derived data such as the below, will not be included by default:<br>  - 24 hour volume (`buyVolume + sellVolume`)<br>  - 24 hour taker buy/sell ratio (`buyVolume / sellVolume`)<br>  - 24 hour average trade price (`volumeQ / volumeU`)<br>  - 24 hour average trade volume (`volume / trades`)<br>  - 24 hour percentage change (`24hStatChange / 24hStat`)<br>  - 48 hour statistics (`2 * 24hStat - 24hStatChange`)<br><br>To query for an extended ticker payload, leverage the `greeks` and the `derived` flags.<br>Ticker extensions are currently under design to offer you more convenience.<br>These flags are only supported on the `Ticker Snapshot` WS endpoint, and on the `Ticker` API endpoint.<br><br>

            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|False<br>`None`|Time at which the event was emitted in unix nanoseconds|
            |instrument<br>`i` |string|False<br>`None`|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |mark_price<br>`mp` |string|False<br>`None`|The mark price of the instrument, expressed in `9` decimals|
            |index_price<br>`ip` |string|False<br>`None`|The index price of the instrument, expressed in `9` decimals|
            |last_price<br>`lp` |string|False<br>`None`|The last traded price of the instrument (also close price), expressed in `9` decimals|
            |last_size<br>`ls` |string|False<br>`None`|The number of assets traded in the last trade, expressed in base asset decimal units|
            |mid_price<br>`mp1` |string|False<br>`None`|The mid price of the instrument, expressed in `9` decimals|
            |best_bid_price<br>`bb` |string|False<br>`None`|The best bid price of the instrument, expressed in `9` decimals|
            |best_bid_size<br>`bb1` |string|False<br>`None`|The number of assets offered on the best bid price of the instrument, expressed in base asset decimal units|
            |best_ask_price<br>`ba` |string|False<br>`None`|The best ask price of the instrument, expressed in `9` decimals|
            |best_ask_size<br>`ba1` |string|False<br>`None`|The number of assets offered on the best ask price of the instrument, expressed in base asset decimal units|
            |funding_rate_8h_curr<br>`fr` |string|False<br>`None`|The current funding rate of the instrument, expressed in centibeeps (1/100th of a basis point)|
            |funding_rate_8h_avg<br>`fr1` |string|False<br>`None`|The average funding rate of the instrument (over last 8h), expressed in centibeeps (1/100th of a basis point)|
            |interest_rate<br>`ir` |string|False<br>`None`|The interest rate of the underlying, expressed in centibeeps (1/100th of a basis point)|
            |forward_price<br>`fp` |string|False<br>`None`|[Options] The forward price of the option, expressed in `9` decimals|
            |buy_volume_24h_b<br>`bv` |string|False<br>`None`|The 24 hour taker buy volume of the instrument, expressed in base asset decimal units|
            |sell_volume_24h_b<br>`sv` |string|False<br>`None`|The 24 hour taker sell volume of the instrument, expressed in base asset decimal units|
            |buy_volume_24h_q<br>`bv1` |string|False<br>`None`|The 24 hour taker buy volume of the instrument, expressed in quote asset decimal units|
            |sell_volume_24h_q<br>`sv1` |string|False<br>`None`|The 24 hour taker sell volume of the instrument, expressed in quote asset decimal units|
            |high_price<br>`hp` |string|False<br>`None`|The 24 hour highest traded price of the instrument, expressed in `9` decimals|
            |low_price<br>`lp1` |string|False<br>`None`|The 24 hour lowest traded price of the instrument, expressed in `9` decimals|
            |open_price<br>`op` |string|False<br>`None`|The 24 hour first traded price of the instrument, expressed in `9` decimals|
            |open_interest<br>`oi` |string|False<br>`None`|The open interest in the instrument, expressed in base asset decimal units|
            |long_short_ratio<br>`ls1` |string|False<br>`None`|The ratio of accounts that are net long vs net short on this instrument|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "stream": "v1.ticker.s",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "event_time": "1697788800000000000",
                "instrument": "BTC_USDT_Perp",
                "mark_price": "65038.01",
                "index_price": "65038.01",
                "last_price": "65038.01",
                "last_size": "123456.78",
                "mid_price": "65038.01",
                "best_bid_price": "65038.01",
                "best_bid_size": "123456.78",
                "best_ask_price": "65038.01",
                "best_ask_size": "123456.78",
                "funding_rate_8h_curr": 0.0003,
                "funding_rate_8h_avg": 0.0003,
                "interest_rate": 0.0003,
                "forward_price": "65038.01",
                "buy_volume_24h_b": "123456.78",
                "sell_volume_24h_b": "123456.78",
                "buy_volume_24h_q": "123456.78",
                "sell_volume_24h_q": "123456.78",
                "high_price": "65038.01",
                "low_price": "65038.01",
                "open_price": "65038.01",
                "open_interest": "123456.78",
                "long_short_ratio": "0.5"
            }
        }
        ```
        ``` { .json .copy }
        {
            "s": "v1.ticker.s",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "i": "BTC_USDT_Perp",
                "mp": "65038.01",
                "ip": "65038.01",
                "lp": "65038.01",
                "ls": "123456.78",
                "mp1": "65038.01",
                "bb": "65038.01",
                "bb1": "123456.78",
                "ba": "65038.01",
                "ba1": "123456.78",
                "fr": 0.0003,
                "fr1": 0.0003,
                "ir": 0.0003,
                "fp": "65038.01",
                "bv": "123456.78",
                "sv": "123456.78",
                "bv1": "123456.78",
                "sv1": "123456.78",
                "hp": "65038.01",
                "lp1": "65038.01",
                "op": "65038.01",
                "oi": "123456.78",
                "ls1": "0.5"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1004|404|Data Not Found|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3030|400|Feed rate is invalid|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .copy }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
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
            "code":3030,
            "message":"Feed rate is invalid",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
### Ticker Delta
```
STREAM: v1.ticker.d
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSTickerFeedSelectorV1](/../../schemas/ws_ticker_feed_selector_v1)"
        Subscribes to a ticker feed for a single instrument. The `ticker.s` channel offers simpler integration. To experience higher publishing rates, please use the `ticker.d` channel.<br>Unlike the `ticker.d` channel which publishes an initial snapshot, then only streams deltas after, the `ticker.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the ticker.</li><li>After the snapshot, the server will only send deltas of the ticker.</li><li>The server will send a delta if any of the fields in the ticker have changed.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |rate<br>`r` |number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (100, 200, 500, 1000, 5000)<br>Snapshot (500, 1000, 5000)|
    ??? info "[WSRequestV1](/../../schemas/ws_request_v1)"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "[WSResponseV1](/../../schemas/ws_response_v1)"
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
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSTickerFeedDataV1](/../../schemas/ws_ticker_feed_data_v1)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Ticker|True|A ticker matching the request filter|
        ??? info "[Ticker](/../../schemas/ticker)"
            Derived data such as the below, will not be included by default:<br>  - 24 hour volume (`buyVolume + sellVolume`)<br>  - 24 hour taker buy/sell ratio (`buyVolume / sellVolume`)<br>  - 24 hour average trade price (`volumeQ / volumeU`)<br>  - 24 hour average trade volume (`volume / trades`)<br>  - 24 hour percentage change (`24hStatChange / 24hStat`)<br>  - 48 hour statistics (`2 * 24hStat - 24hStatChange`)<br><br>To query for an extended ticker payload, leverage the `greeks` and the `derived` flags.<br>Ticker extensions are currently under design to offer you more convenience.<br>These flags are only supported on the `Ticker Snapshot` WS endpoint, and on the `Ticker` API endpoint.<br><br>

            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|False<br>`None`|Time at which the event was emitted in unix nanoseconds|
            |instrument<br>`i` |string|False<br>`None`|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |mark_price<br>`mp` |string|False<br>`None`|The mark price of the instrument, expressed in `9` decimals|
            |index_price<br>`ip` |string|False<br>`None`|The index price of the instrument, expressed in `9` decimals|
            |last_price<br>`lp` |string|False<br>`None`|The last traded price of the instrument (also close price), expressed in `9` decimals|
            |last_size<br>`ls` |string|False<br>`None`|The number of assets traded in the last trade, expressed in base asset decimal units|
            |mid_price<br>`mp1` |string|False<br>`None`|The mid price of the instrument, expressed in `9` decimals|
            |best_bid_price<br>`bb` |string|False<br>`None`|The best bid price of the instrument, expressed in `9` decimals|
            |best_bid_size<br>`bb1` |string|False<br>`None`|The number of assets offered on the best bid price of the instrument, expressed in base asset decimal units|
            |best_ask_price<br>`ba` |string|False<br>`None`|The best ask price of the instrument, expressed in `9` decimals|
            |best_ask_size<br>`ba1` |string|False<br>`None`|The number of assets offered on the best ask price of the instrument, expressed in base asset decimal units|
            |funding_rate_8h_curr<br>`fr` |string|False<br>`None`|The current funding rate of the instrument, expressed in centibeeps (1/100th of a basis point)|
            |funding_rate_8h_avg<br>`fr1` |string|False<br>`None`|The average funding rate of the instrument (over last 8h), expressed in centibeeps (1/100th of a basis point)|
            |interest_rate<br>`ir` |string|False<br>`None`|The interest rate of the underlying, expressed in centibeeps (1/100th of a basis point)|
            |forward_price<br>`fp` |string|False<br>`None`|[Options] The forward price of the option, expressed in `9` decimals|
            |buy_volume_24h_b<br>`bv` |string|False<br>`None`|The 24 hour taker buy volume of the instrument, expressed in base asset decimal units|
            |sell_volume_24h_b<br>`sv` |string|False<br>`None`|The 24 hour taker sell volume of the instrument, expressed in base asset decimal units|
            |buy_volume_24h_q<br>`bv1` |string|False<br>`None`|The 24 hour taker buy volume of the instrument, expressed in quote asset decimal units|
            |sell_volume_24h_q<br>`sv1` |string|False<br>`None`|The 24 hour taker sell volume of the instrument, expressed in quote asset decimal units|
            |high_price<br>`hp` |string|False<br>`None`|The 24 hour highest traded price of the instrument, expressed in `9` decimals|
            |low_price<br>`lp1` |string|False<br>`None`|The 24 hour lowest traded price of the instrument, expressed in `9` decimals|
            |open_price<br>`op` |string|False<br>`None`|The 24 hour first traded price of the instrument, expressed in `9` decimals|
            |open_interest<br>`oi` |string|False<br>`None`|The open interest in the instrument, expressed in base asset decimal units|
            |long_short_ratio<br>`ls1` |string|False<br>`None`|The ratio of accounts that are net long vs net short on this instrument|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "stream": "v1.ticker.s",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "event_time": "1697788800000000000",
                "instrument": "BTC_USDT_Perp",
                "mark_price": "65038.01",
                "index_price": "65038.01",
                "last_price": "65038.01",
                "last_size": "123456.78",
                "mid_price": "65038.01",
                "best_bid_price": "65038.01",
                "best_bid_size": "123456.78",
                "best_ask_price": "65038.01",
                "best_ask_size": "123456.78",
                "funding_rate_8h_curr": 0.0003,
                "funding_rate_8h_avg": 0.0003,
                "interest_rate": 0.0003,
                "forward_price": "65038.01",
                "buy_volume_24h_b": "123456.78",
                "sell_volume_24h_b": "123456.78",
                "buy_volume_24h_q": "123456.78",
                "sell_volume_24h_q": "123456.78",
                "high_price": "65038.01",
                "low_price": "65038.01",
                "open_price": "65038.01",
                "open_interest": "123456.78",
                "long_short_ratio": "0.5"
            }
        }
        ```
        ``` { .json .copy }
        {
            "s": "v1.ticker.s",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "i": "BTC_USDT_Perp",
                "mp": "65038.01",
                "ip": "65038.01",
                "lp": "65038.01",
                "ls": "123456.78",
                "mp1": "65038.01",
                "bb": "65038.01",
                "bb1": "123456.78",
                "ba": "65038.01",
                "ba1": "123456.78",
                "fr": 0.0003,
                "fr1": 0.0003,
                "ir": 0.0003,
                "fp": "65038.01",
                "bv": "123456.78",
                "sv": "123456.78",
                "bv1": "123456.78",
                "sv1": "123456.78",
                "hp": "65038.01",
                "lp1": "65038.01",
                "op": "65038.01",
                "oi": "123456.78",
                "ls1": "0.5"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1004|404|Data Not Found|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3030|400|Feed rate is invalid|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .copy }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
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
            "code":3030,
            "message":"Feed rate is invalid",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
## Orderbook
### Orderbook Snap
```
STREAM: v1.book.s
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSOrderbookLevelsFeedSelectorV1](/../../schemas/ws_orderbook_levels_feed_selector_v1)"
        Subscribes to aggregated orderbook updates for a single instrument. The `book.s` channel offers simpler integration. To experience higher publishing rates, please use the `book.d` channel.<br>Unlike the `book.d` channel which publishes an initial snapshot, then only streams deltas after, the `book.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of all levels of the Orderbook.</li><li>After the snapshot, the server will only send levels that have changed in value.</li></ul><br><br>Subscription Pattern:<ul><li>Delta - `instrument@rate`</li><li>Snapshot - `instrument@rate-depth`</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a level is not updated, level not published</li><li>If a level is updated, {size: '123'}</li><li>If a level is set to zero, {size: '0'}</li><li>Incoming levels will be published as soon as price moves</li><li>Outgoing levels will be published with `size = 0`</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |rate<br>`r` |number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (50, 100, 500, 1000)<br>Snapshot (500, 1000)|
        |depth<br>`d` |number|False<br>`'0'`|Depth of the order book to be retrieved<br>Delta(0 - `unlimited`)<br>Snapshot(10, 50, 100, 500)|
    ??? info "[WSRequestV1](/../../schemas/ws_request_v1)"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "[WSResponseV1](/../../schemas/ws_response_v1)"
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
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.book.s",
            "subs":["BTC_USDT_Perp@500-50"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSOrderbookLevelsFeedDataV1](/../../schemas/ws_orderbook_levels_feed_data_v1)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |OrderbookLevels|True|An orderbook levels object matching the request filter|
        ??? info "[OrderbookLevels](/../../schemas/orderbook_levels)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |bids<br>`b` |[OrderbookLevel]|True|The list of best bids up till query depth|
            |asks<br>`a` |[OrderbookLevel]|True|The list of best asks up till query depth|
            ??? info "[OrderbookLevel](/../../schemas/orderbook_level)"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |price<br>`p` |string|True|The price of the level, expressed in `9` decimals|
                |size<br>`s` |string|True|The number of assets offered, expressed in base asset decimal units|
                |num_orders<br>`no` |number|True|The number of open orders at this level|
            ??? info "[OrderbookLevel](/../../schemas/orderbook_level)"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |price<br>`p` |string|True|The price of the level, expressed in `9` decimals|
                |size<br>`s` |string|True|The number of assets offered, expressed in base asset decimal units|
                |num_orders<br>`no` |number|True|The number of open orders at this level|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "stream": "v1.book.s",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "event_time": "1697788800000000000",
                "instrument": "BTC_USDT_Perp",
                "bids": [{
                    "price": "65038.01",
                    "size": "3456.78",
                    "num_orders": "123"
                }],
                "asks": [{
                    "price": "65038.01",
                    "size": "3456.78",
                    "num_orders": "123"
                }]
            }
        }
        ```
        ``` { .json .copy }
        {
            "s": "v1.book.s",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "i": "BTC_USDT_Perp",
                "b": [{
                    "p": "65038.01",
                    "s": "3456.78",
                    "no": "123"
                }],
                "a": [{
                    "p": "65038.01",
                    "s": "3456.78",
                    "no": "123"
                }]
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1004|404|Data Not Found|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3030|400|Feed rate is invalid|
        |3031|400|Depth is invalid|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .copy }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
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
            "code":3030,
            "message":"Feed rate is invalid",
            "status":400
        }
        {
            "code":3031,
            "message":"Depth is invalid",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
### Orderbook Delta
```
STREAM: v1.book.d
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSOrderbookLevelsFeedSelectorV1](/../../schemas/ws_orderbook_levels_feed_selector_v1)"
        Subscribes to aggregated orderbook updates for a single instrument. The `book.s` channel offers simpler integration. To experience higher publishing rates, please use the `book.d` channel.<br>Unlike the `book.d` channel which publishes an initial snapshot, then only streams deltas after, the `book.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of all levels of the Orderbook.</li><li>After the snapshot, the server will only send levels that have changed in value.</li></ul><br><br>Subscription Pattern:<ul><li>Delta - `instrument@rate`</li><li>Snapshot - `instrument@rate-depth`</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a level is not updated, level not published</li><li>If a level is updated, {size: '123'}</li><li>If a level is set to zero, {size: '0'}</li><li>Incoming levels will be published as soon as price moves</li><li>Outgoing levels will be published with `size = 0`</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |rate<br>`r` |number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (50, 100, 500, 1000)<br>Snapshot (500, 1000)|
        |depth<br>`d` |number|False<br>`'0'`|Depth of the order book to be retrieved<br>Delta(0 - `unlimited`)<br>Snapshot(10, 50, 100, 500)|
    ??? info "[WSRequestV1](/../../schemas/ws_request_v1)"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "[WSResponseV1](/../../schemas/ws_response_v1)"
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
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.book.d",
            "subs":["BTC_USDT_Perp@500-50"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSOrderbookLevelsFeedDataV1](/../../schemas/ws_orderbook_levels_feed_data_v1)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |OrderbookLevels|True|An orderbook levels object matching the request filter|
        ??? info "[OrderbookLevels](/../../schemas/orderbook_levels)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |bids<br>`b` |[OrderbookLevel]|True|The list of best bids up till query depth|
            |asks<br>`a` |[OrderbookLevel]|True|The list of best asks up till query depth|
            ??? info "[OrderbookLevel](/../../schemas/orderbook_level)"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |price<br>`p` |string|True|The price of the level, expressed in `9` decimals|
                |size<br>`s` |string|True|The number of assets offered, expressed in base asset decimal units|
                |num_orders<br>`no` |number|True|The number of open orders at this level|
            ??? info "[OrderbookLevel](/../../schemas/orderbook_level)"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |price<br>`p` |string|True|The price of the level, expressed in `9` decimals|
                |size<br>`s` |string|True|The number of assets offered, expressed in base asset decimal units|
                |num_orders<br>`no` |number|True|The number of open orders at this level|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "stream": "v1.book.s",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "event_time": "1697788800000000000",
                "instrument": "BTC_USDT_Perp",
                "bids": [{
                    "price": "65038.01",
                    "size": "3456.78",
                    "num_orders": "123"
                }],
                "asks": [{
                    "price": "65038.01",
                    "size": "3456.78",
                    "num_orders": "123"
                }]
            }
        }
        ```
        ``` { .json .copy }
        {
            "s": "v1.book.s",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "i": "BTC_USDT_Perp",
                "b": [{
                    "p": "65038.01",
                    "s": "3456.78",
                    "no": "123"
                }],
                "a": [{
                    "p": "65038.01",
                    "s": "3456.78",
                    "no": "123"
                }]
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1004|404|Data Not Found|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3030|400|Feed rate is invalid|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .copy }
        {
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
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
            "code":3030,
            "message":"Feed rate is invalid",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-50"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
## Trade
### Trade
```
STREAM: v1.trade
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSTradeFeedSelectorV1](/../../schemas/ws_trade_feed_selector_v1)"
        Subscribes to a stream of Public Trades for an instrument.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |limit<br>`l` |number|True|The limit to query for. Defaults to 500; Max 1000|
    ??? info "[WSRequestV1](/../../schemas/ws_request_v1)"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "[WSResponseV1](/../../schemas/ws_response_v1)"
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
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.trade",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSTradeFeedDataV1](/../../schemas/ws_trade_feed_data_v1)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Trade|True|A public trade matching the request filter|
        ??? info "[Trade](/../../schemas/trade)"
            All private RFQs and Private AXEs will be filtered out from the responses<br>

            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |is_taker_buyer<br>`it` |boolean|True|If taker was the buyer on the trade|
            |size<br>`s` |string|True|The number of assets being traded, expressed in base asset decimal units|
            |price<br>`p` |string|True|The traded price, expressed in `9` decimals|
            |mark_price<br>`mp` |string|True|The mark price of the instrument at point of trade, expressed in `9` decimals|
            |index_price<br>`ip` |string|True|The index price of the instrument at point of trade, expressed in `9` decimals|
            |interest_rate<br>`ir` |string|True|The interest rate of the underlying at point of trade, expressed in centibeeps (1/100th of a basis point)|
            |forward_price<br>`fp` |string|True|[Options] The forward price of the option at point of trade, expressed in `9` decimals|
            |trade_id<br>`ti` |string|True|A trade identifier, globally unique, and monotonically increasing (not by `1`).<br>All trades sharing a single taker execution share the same first component (before `:`), and `event_time`.<br>`trade_id` is guaranteed to be consistent across MarketData `Trade` and Trading `Fill`.|
            |venue<br>`v` |Venue|True|The venue where the trade occurred|
            ??? info "[Venue](/../../schemas/venue)"
                The list of Trading Venues that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`ORDERBOOK` = 1|the trade is cleared on the orderbook venue|
                |`RFQ` = 2|the trade is cleared on the RFQ venue|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "stream": "v1.trade",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "event_time": "1697788800000000000",
                "instrument": "BTC_USDT_Perp",
                "is_taker_buyer": true,
                "size": "123456.78",
                "price": "65038.01",
                "mark_price": "65038.01",
                "index_price": "65038.01",
                "interest_rate": 0.0003,
                "forward_price": "65038.01",
                "trade_id": "209358:2",
                "venue": "ORDERBOOK"
            }
        }
        ```
        ``` { .json .copy }
        {
            "s": "v1.trade",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "et": "1697788800000000000",
                "i": "BTC_USDT_Perp",
                "it": true,
                "s": "123456.78",
                "p": "65038.01",
                "mp": "65038.01",
                "ip": "65038.01",
                "ir": 0.0003,
                "fp": "65038.01",
                "ti": "209358:2",
                "v": "ORDERBOOK"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3011|400|Limit exceeds min or max value|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .copy }
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
            "code":3011,
            "message":"Limit exceeds min or max value",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
## Candlestick
### Candlestick
```
STREAM: v1.candle
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSCandlestickFeedSelectorV1](/../../schemas/ws_candlestick_feed_selector_v1)"
        Subscribes to a stream of Kline/Candlestick updates for an instrument. A Kline is uniquely identified by its open time.<br>A new Kline is published every interval (if it exists). Upon subscription, the server will send the 5 most recent Kline for the requested interval.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |interval<br>`i1` |CandlestickInterval|True|The interval of each candlestick|
        |type<br>`t` |CandlestickType|True|The type of candlestick data to retrieve|
        ??? info "[CandlestickInterval](/../../schemas/candlestick_interval)"
            |Value| Description |
            |-|-|
            |`CI_1_M` = 1|1 minute|
            |`CI_3_M` = 2|3 minutes|
            |`CI_5_M` = 3|5 minutes|
            |`CI_15_M` = 4|15 minutes|
            |`CI_30_M` = 5|30 minutes|
            |`CI_1_H` = 6|1 hour|
            |`CI_2_H` = 7|2 hour|
            |`CI_4_H` = 8|4 hour|
            |`CI_6_H` = 9|6 hour|
            |`CI_8_H` = 10|8 hour|
            |`CI_12_H` = 11|12 hour|
            |`CI_1_D` = 12|1 day|
            |`CI_3_D` = 13|3 days|
            |`CI_5_D` = 14|5 days|
            |`CI_1_W` = 15|1 week|
            |`CI_2_W` = 16|2 weeks|
            |`CI_3_W` = 17|3 weeks|
            |`CI_4_W` = 18|4 weeks|
        ??? info "[CandlestickType](/../../schemas/candlestick_type)"
            |Value| Description |
            |-|-|
            |`TRADE` = 1|Tracks traded prices|
            |`MARK` = 2|Tracks mark prices|
            |`INDEX` = 3|Tracks index prices|
            |`MID` = 4|Tracks book mid prices|
    ??? info "[WSRequestV1](/../../schemas/ws_request_v1)"
        All V1 Websocket Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>If a `request_id` is supplied in this JSON RPC request, it will be propagated back to any relevant JSON RPC responses (including error).<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_id<br>`ri` |number|False<br>`0`|Optional Field which is used to match the response by the client.<br>If not passed, this field will not be returned|
        |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
        |feed<br>`f` |[string]|True|The list of feeds to subscribe to|
        |method<br>`m` |string|True|The method to use for the request (eg: subscribe / unsubscribe)|
        |is_full<br>`if` |boolean|False<br>`false`|Whether the request is for full data or lite data|
    ??? info "[WSResponseV1](/../../schemas/ws_response_v1)"
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
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "stream":"v1.candle",
            "subs":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "unsubs":[],
            "num_snapshots":[1],
            "first_sequence_number":[2813]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "[WSCandlestickFeedDataV1](/../../schemas/ws_candlestick_feed_data_v1)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |stream<br>`s` |string|True|Stream name|
        |selector<br>`s1` |string|True|Primary selector|
        |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
        |feed<br>`f` |Candlestick|True|A candlestick entry matching the request filters|
        ??? info "[Candlestick](/../../schemas/candlestick)"
            <br>

            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |open_time<br>`ot` |string|True|Open time of kline bar in unix nanoseconds|
            |close_time<br>`ct` |string|True|Close time of kline bar in unix nanosecond|
            |open<br>`o` |string|True|The open price, expressed in underlying currency resolution units|
            |close<br>`c` |string|True|The close price, expressed in underlying currency resolution units|
            |high<br>`h` |string|True|The high price, expressed in underlying currency resolution units|
            |low<br>`l` |string|True|The low price, expressed in underlying currency resolution units|
            |volume_b<br>`vb` |string|True|The underlying volume transacted, expressed in base asset decimal units|
            |volume_q<br>`vq` |string|True|The quote volume transacted, expressed in quote asset decimal units|
            |trades<br>`t` |number|True|The number of trades transacted|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "stream": "v1.candle",
            "selector": "BTC_USDT_Perp",
            "sequence_number": "872634876",
            "feed": {
                "open_time": "1697788800000000000",
                "close_time": "1697788800000000000",
                "open": "123456.78",
                "close": "123456.78",
                "high": "123456.78",
                "low": "123456.78",
                "volume_b": "123456.78",
                "volume_q": "123456.78",
                "trades": 123456,
                "instrument": "BTC_USDT_Perp"
            }
        }
        ```
        ``` { .json .copy }
        {
            "s": "v1.candle",
            "s1": "BTC_USDT_Perp",
            "sn": "872634876",
            "f": {
                "ot": "1697788800000000000",
                "ct": "1697788800000000000",
                "o": "123456.78",
                "c": "123456.78",
                "h": "123456.78",
                "l": "123456.78",
                "vb": "123456.78",
                "vq": "123456.78",
                "t": 123456,
                "i": "BTC_USDT_Perp"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1101|400|Feed Format must be in the format of <primary>@<secondary>|
        |1102|400|Wrong number of primary selectors|
        |1103|400|Wrong number of secondary selectors|
        |3000|400|Instrument is invalid|
        |3040|400|Candlestick interval is invalid|
        |3041|400|Candlestick type is invalid|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ``` { .json .copy }
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
            "code":3040,
            "message":"Candlestick interval is invalid",
            "status":400
        }
        {
            "code":3041,
            "message":"Candlestick type is invalid",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "request_id":1,
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":false
        }
        ' -w 360
        ```
    </section>
<hr class="solid">
