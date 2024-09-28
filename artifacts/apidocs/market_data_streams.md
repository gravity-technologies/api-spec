# MarketData Websocket Streams

## Ticker
### Mini Ticker Snap
```
STREAM: v1.mini.s
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSMiniTickerFeedSelectorV1"
        Subscribes to a mini ticker feed for a single instrument. The `mini.s` channel offers simpler integration. To experience higher publishing rates, please use the `mini.d` channel.<br>Unlike the `mini.d` channel which publishes an initial snapshot, then only streams deltas after, the `mini.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the mini ticker.</li><li>After the snapshot, the server will only send deltas of the mini ticker.</li><li>The server will send a delta if any of the fields in the mini ticker have changed.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |rate|r|number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (raw, 50, 100, 200, 500, 1000, 5000)<br>Snapshot (200, 500, 1000, 5000)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.mini.s",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSMiniTickerFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |selector|s1|string|True|Primary selector|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|MiniTicker|True|A mini ticker matching the request filter|
        ??? info "MiniTicker"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|False|Time at which the event was emitted in unix nanoseconds|
            |instrument|i|string|False|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |mark_price|mp|string|False|The mark price of the instrument, expressed in `9` decimals|
            |index_price|ip|string|False|The index price of the instrument, expressed in `9` decimals|
            |last_price|lp|string|False|The last traded price of the instrument (also close price), expressed in `9` decimals|
            |last_size|ls|string|False|The number of assets traded in the last trade, expressed in underlying asset decimal units|
            |mid_price|mp1|string|False|The mid price of the instrument, expressed in `9` decimals|
            |best_bid_price|bb|string|False|The best bid price of the instrument, expressed in `9` decimals|
            |best_bid_size|bb1|string|False|The number of assets offered on the best bid price of the instrument, expressed in underlying asset decimal units|
            |best_ask_price|ba|string|False|The best ask price of the instrument, expressed in `9` decimals|
            |best_ask_size|ba1|string|False|The number of assets offered on the best ask price of the instrument, expressed in underlying asset decimal units|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
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
        ```json
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        ```
    </section>
=== "Try it out"
    !!! example "dev"
        ```bash
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "stg"
        ```bash
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "testnet"
        ```bash
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "prod"
        ```bash
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "stream":"v1.mini.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
### Mini Ticker Delta
```
STREAM: v1.mini.d
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSMiniTickerFeedSelectorV1"
        Subscribes to a mini ticker feed for a single instrument. The `mini.s` channel offers simpler integration. To experience higher publishing rates, please use the `mini.d` channel.<br>Unlike the `mini.d` channel which publishes an initial snapshot, then only streams deltas after, the `mini.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the mini ticker.</li><li>After the snapshot, the server will only send deltas of the mini ticker.</li><li>The server will send a delta if any of the fields in the mini ticker have changed.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |rate|r|number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (raw, 50, 100, 200, 500, 1000, 5000)<br>Snapshot (200, 500, 1000, 5000)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.mini.d",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSMiniTickerFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |selector|s1|string|True|Primary selector|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|MiniTicker|True|A mini ticker matching the request filter|
        ??? info "MiniTicker"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|False|Time at which the event was emitted in unix nanoseconds|
            |instrument|i|string|False|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |mark_price|mp|string|False|The mark price of the instrument, expressed in `9` decimals|
            |index_price|ip|string|False|The index price of the instrument, expressed in `9` decimals|
            |last_price|lp|string|False|The last traded price of the instrument (also close price), expressed in `9` decimals|
            |last_size|ls|string|False|The number of assets traded in the last trade, expressed in underlying asset decimal units|
            |mid_price|mp1|string|False|The mid price of the instrument, expressed in `9` decimals|
            |best_bid_price|bb|string|False|The best bid price of the instrument, expressed in `9` decimals|
            |best_bid_size|bb1|string|False|The number of assets offered on the best bid price of the instrument, expressed in underlying asset decimal units|
            |best_ask_price|ba|string|False|The best ask price of the instrument, expressed in `9` decimals|
            |best_ask_size|ba1|string|False|The number of assets offered on the best ask price of the instrument, expressed in underlying asset decimal units|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
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
        ```json
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        ```
    </section>
=== "Try it out"
    !!! example "dev"
        ```bash
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "stg"
        ```bash
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "testnet"
        ```bash
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "prod"
        ```bash
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "stream":"v1.mini.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
### Ticker Snap
```
STREAM: v1.ticker.s
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSTickerFeedSelectorV1"
        Subscribes to a ticker feed for a single instrument. The `ticker.s` channel offers simpler integration. To experience higher publishing rates, please use the `ticker.d` channel.<br>Unlike the `ticker.d` channel which publishes an initial snapshot, then only streams deltas after, the `ticker.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the ticker.</li><li>After the snapshot, the server will only send deltas of the ticker.</li><li>The server will send a delta if any of the fields in the ticker have changed.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |rate|r|number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (100, 200, 500, 1000, 5000)<br>Snapshot (500, 1000, 5000)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.ticker.s",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSTickerFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |selector|s1|string|True|Primary selector|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|Ticker|True|A ticker matching the request filter|
        ??? info "Ticker"
            Derived data such as the below, will not be included by default:<br>  - 24 hour volume (`buyVolume + sellVolume`)<br>  - 24 hour taker buy/sell ratio (`buyVolume / sellVolume`)<br>  - 24 hour average trade price (`volumeQ / volumeU`)<br>  - 24 hour average trade volume (`volume / trades`)<br>  - 24 hour percentage change (`24hStatChange / 24hStat`)<br>  - 48 hour statistics (`2 * 24hStat - 24hStatChange`)<br><br>To query for an extended ticker payload, leverage the `greeks` and the `derived` flags.<br>Ticker extensions are currently under design to offer you more convenience.<br>These flags are only supported on the `Ticker Snapshot` WS endpoint, and on the `Ticker` API endpoint.<br><br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|False|Time at which the event was emitted in unix nanoseconds|
            |instrument|i|string|False|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |mark_price|mp|string|False|The mark price of the instrument, expressed in `9` decimals|
            |index_price|ip|string|False|The index price of the instrument, expressed in `9` decimals|
            |last_price|lp|string|False|The last traded price of the instrument (also close price), expressed in `9` decimals|
            |last_size|ls|string|False|The number of assets traded in the last trade, expressed in underlying asset decimal units|
            |mid_price|mp1|string|False|The mid price of the instrument, expressed in `9` decimals|
            |best_bid_price|bb|string|False|The best bid price of the instrument, expressed in `9` decimals|
            |best_bid_size|bb1|string|False|The number of assets offered on the best bid price of the instrument, expressed in underlying asset decimal units|
            |best_ask_price|ba|string|False|The best ask price of the instrument, expressed in `9` decimals|
            |best_ask_size|ba1|string|False|The number of assets offered on the best ask price of the instrument, expressed in underlying asset decimal units|
            |funding_rate_8_h_curr|fr|string|False|The current funding rate of the instrument, expressed in centibeeps (1/100th of a basis point)|
            |funding_rate_8_h_avg|fr1|string|False|The average funding rate of the instrument (over last 8h), expressed in centibeeps (1/100th of a basis point)|
            |interest_rate|ir|string|False|The interest rate of the underlying, expressed in centibeeps (1/100th of a basis point)|
            |forward_price|fp|string|False|[Options] The forward price of the option, expressed in `9` decimals|
            |buy_volume_24_h_u|bv|string|False|The 24 hour taker buy volume of the instrument, expressed in underlying asset decimal units|
            |sell_volume_24_h_u|sv|string|False|The 24 hour taker sell volume of the instrument, expressed in underlying asset decimal units|
            |buy_volume_24_h_q|bv1|string|False|The 24 hour taker buy volume of the instrument, expressed in quote asset decimal units|
            |sell_volume_24_h_q|sv1|string|False|The 24 hour taker sell volume of the instrument, expressed in quote asset decimal units|
            |high_price|hp|string|False|The 24 hour highest traded price of the instrument, expressed in `9` decimals|
            |low_price|lp1|string|False|The 24 hour lowest traded price of the instrument, expressed in `9` decimals|
            |open_price|op|string|False|The 24 hour first traded price of the instrument, expressed in `9` decimals|
            |open_interest|oi|string|False|The open interest in the instrument, expressed in underlying asset decimal units|
            |long_short_ratio|ls1|string|False|The ratio of accounts that are net long vs net short on this instrument|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
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
                "funding_rate_8_h_curr": 0.0003,
                "funding_rate_8_h_avg": 0.0003,
                "interest_rate": 0.0003,
                "forward_price": "65038.01",
                "buy_volume_24_h_u": "123456.78",
                "sell_volume_24_h_u": "123456.78",
                "buy_volume_24_h_q": "123456.78",
                "sell_volume_24_h_q": "123456.78",
                "high_price": "65038.01",
                "low_price": "65038.01",
                "open_price": "65038.01",
                "open_interest": "123456.78",
                "long_short_ratio": "0.5"
            }
        }
        ```
        ```json
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        ```
    </section>
=== "Try it out"
    !!! example "dev"
        ```bash
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "stg"
        ```bash
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "testnet"
        ```bash
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "prod"
        ```bash
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "stream":"v1.ticker.s",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
### Ticker Delta
```
STREAM: v1.ticker.d
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSTickerFeedSelectorV1"
        Subscribes to a ticker feed for a single instrument. The `ticker.s` channel offers simpler integration. To experience higher publishing rates, please use the `ticker.d` channel.<br>Unlike the `ticker.d` channel which publishes an initial snapshot, then only streams deltas after, the `ticker.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the ticker.</li><li>After the snapshot, the server will only send deltas of the ticker.</li><li>The server will send a delta if any of the fields in the ticker have changed.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |rate|r|number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (100, 200, 500, 1000, 5000)<br>Snapshot (500, 1000, 5000)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.ticker.d",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSTickerFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |selector|s1|string|True|Primary selector|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|Ticker|True|A ticker matching the request filter|
        ??? info "Ticker"
            Derived data such as the below, will not be included by default:<br>  - 24 hour volume (`buyVolume + sellVolume`)<br>  - 24 hour taker buy/sell ratio (`buyVolume / sellVolume`)<br>  - 24 hour average trade price (`volumeQ / volumeU`)<br>  - 24 hour average trade volume (`volume / trades`)<br>  - 24 hour percentage change (`24hStatChange / 24hStat`)<br>  - 48 hour statistics (`2 * 24hStat - 24hStatChange`)<br><br>To query for an extended ticker payload, leverage the `greeks` and the `derived` flags.<br>Ticker extensions are currently under design to offer you more convenience.<br>These flags are only supported on the `Ticker Snapshot` WS endpoint, and on the `Ticker` API endpoint.<br><br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|False|Time at which the event was emitted in unix nanoseconds|
            |instrument|i|string|False|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |mark_price|mp|string|False|The mark price of the instrument, expressed in `9` decimals|
            |index_price|ip|string|False|The index price of the instrument, expressed in `9` decimals|
            |last_price|lp|string|False|The last traded price of the instrument (also close price), expressed in `9` decimals|
            |last_size|ls|string|False|The number of assets traded in the last trade, expressed in underlying asset decimal units|
            |mid_price|mp1|string|False|The mid price of the instrument, expressed in `9` decimals|
            |best_bid_price|bb|string|False|The best bid price of the instrument, expressed in `9` decimals|
            |best_bid_size|bb1|string|False|The number of assets offered on the best bid price of the instrument, expressed in underlying asset decimal units|
            |best_ask_price|ba|string|False|The best ask price of the instrument, expressed in `9` decimals|
            |best_ask_size|ba1|string|False|The number of assets offered on the best ask price of the instrument, expressed in underlying asset decimal units|
            |funding_rate_8_h_curr|fr|string|False|The current funding rate of the instrument, expressed in centibeeps (1/100th of a basis point)|
            |funding_rate_8_h_avg|fr1|string|False|The average funding rate of the instrument (over last 8h), expressed in centibeeps (1/100th of a basis point)|
            |interest_rate|ir|string|False|The interest rate of the underlying, expressed in centibeeps (1/100th of a basis point)|
            |forward_price|fp|string|False|[Options] The forward price of the option, expressed in `9` decimals|
            |buy_volume_24_h_u|bv|string|False|The 24 hour taker buy volume of the instrument, expressed in underlying asset decimal units|
            |sell_volume_24_h_u|sv|string|False|The 24 hour taker sell volume of the instrument, expressed in underlying asset decimal units|
            |buy_volume_24_h_q|bv1|string|False|The 24 hour taker buy volume of the instrument, expressed in quote asset decimal units|
            |sell_volume_24_h_q|sv1|string|False|The 24 hour taker sell volume of the instrument, expressed in quote asset decimal units|
            |high_price|hp|string|False|The 24 hour highest traded price of the instrument, expressed in `9` decimals|
            |low_price|lp1|string|False|The 24 hour lowest traded price of the instrument, expressed in `9` decimals|
            |open_price|op|string|False|The 24 hour first traded price of the instrument, expressed in `9` decimals|
            |open_interest|oi|string|False|The open interest in the instrument, expressed in underlying asset decimal units|
            |long_short_ratio|ls1|string|False|The ratio of accounts that are net long vs net short on this instrument|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
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
                "funding_rate_8_h_curr": 0.0003,
                "funding_rate_8_h_avg": 0.0003,
                "interest_rate": 0.0003,
                "forward_price": "65038.01",
                "buy_volume_24_h_u": "123456.78",
                "sell_volume_24_h_u": "123456.78",
                "buy_volume_24_h_q": "123456.78",
                "sell_volume_24_h_q": "123456.78",
                "high_price": "65038.01",
                "low_price": "65038.01",
                "open_price": "65038.01",
                "open_interest": "123456.78",
                "long_short_ratio": "0.5"
            }
        }
        ```
        ```json
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        ```
    </section>
=== "Try it out"
    !!! example "dev"
        ```bash
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "stg"
        ```bash
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "testnet"
        ```bash
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "prod"
        ```bash
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "stream":"v1.ticker.d",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
## Orderbook
### Orderbook Snap
```
STREAM: v1.book.s
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderbookLevelsFeedSelectorV1"
        Subscribes to aggregated orderbook updates for a single instrument. The `book.s` channel offers simpler integration. To experience higher publishing rates, please use the `book.d` channel.<br>Unlike the `book.d` channel which publishes an initial snapshot, then only streams deltas after, the `book.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of all levels of the Orderbook.</li><li>After the snapshot, the server will only send levels that have changed in value.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a level is not updated, level not published</li><li>If a level is updated, {size: '123'}</li><li>If a level is set to zero, {size: '0'}</li><li>Incoming levels will be published as soon as price moves</li><li>Outgoing levels will be published with `size = 0`</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |rate|r|number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (100, 200, 500, 1000, 5000)<br>Snapshot (500, 1000, 5000)|
        |depth|d|number|True|Depth of the order book to be retrieved (API/Snapshot max is 100, Delta max is 1000)|
        |aggregate|a|number|True|The number of levels to aggregate into one level (1 = no aggregation, 10/100/1000 = aggregate 10/100/1000 levels into 1)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.book.s",
            "subs":["BTC_USDT_Perp@500-100-10"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderbookLevelsFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |selector|s1|string|True|Primary selector|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|OrderbookLevels|True|An orderbook levels object matching the request filter|
        ??? info "OrderbookLevels"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |bids|b|[OrderbookLevel]|True|The list of best bids up till query depth|
            |asks|a|[OrderbookLevel]|True|The list of best asks up till query depth|
            ??? info "OrderbookLevel"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |price|p|string|True|The price of the level, expressed in `9` decimals|
                |size|s|string|True|The number of assets offered, expressed in underlying asset decimal units|
                |num_orders|no|number|True|The number of open orders at this level|
            ??? info "OrderbookLevel"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |price|p|string|True|The price of the level, expressed in `9` decimals|
                |size|s|string|True|The number of assets offered, expressed in underlying asset decimal units|
                |num_orders|no|number|True|The number of open orders at this level|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
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
        ```json
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        ```
    </section>
=== "Try it out"
    !!! example "dev"
        ```bash
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "stg"
        ```bash
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "testnet"
        ```bash
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "prod"
        ```bash
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "stream":"v1.book.s",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
### Orderbook Delta
```
STREAM: v1.book.d
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderbookLevelsFeedSelectorV1"
        Subscribes to aggregated orderbook updates for a single instrument. The `book.s` channel offers simpler integration. To experience higher publishing rates, please use the `book.d` channel.<br>Unlike the `book.d` channel which publishes an initial snapshot, then only streams deltas after, the `book.s` channel publishes full snapshots at each feed.<br><br>The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of all levels of the Orderbook.</li><li>After the snapshot, the server will only send levels that have changed in value.</li></ul><br><br>Field Semantics:<ul><li>[DeltaOnly] If a level is not updated, level not published</li><li>If a level is updated, {size: '123'}</li><li>If a level is set to zero, {size: '0'}</li><li>Incoming levels will be published as soon as price moves</li><li>Outgoing levels will be published with `size = 0`</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |rate|r|number|True|The minimal rate at which we publish feeds (in milliseconds)<br>Delta (100, 200, 500, 1000, 5000)<br>Snapshot (500, 1000, 5000)|
        |depth|d|number|True|Depth of the order book to be retrieved (API/Snapshot max is 100, Delta max is 1000)|
        |aggregate|a|number|True|The number of levels to aggregate into one level (1 = no aggregation, 10/100/1000 = aggregate 10/100/1000 levels into 1)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.book.d",
            "subs":["BTC_USDT_Perp@500-100-10"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSOrderbookLevelsFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |selector|s1|string|True|Primary selector|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|OrderbookLevels|True|An orderbook levels object matching the request filter|
        ??? info "OrderbookLevels"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |bids|b|[OrderbookLevel]|True|The list of best bids up till query depth|
            |asks|a|[OrderbookLevel]|True|The list of best asks up till query depth|
            ??? info "OrderbookLevel"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |price|p|string|True|The price of the level, expressed in `9` decimals|
                |size|s|string|True|The number of assets offered, expressed in underlying asset decimal units|
                |num_orders|no|number|True|The number of open orders at this level|
            ??? info "OrderbookLevel"
                |Name|Lite|Type|Required| Description |
                |-|-|-|-|-|
                |price|p|string|True|The price of the level, expressed in `9` decimals|
                |size|s|string|True|The number of assets offered, expressed in underlying asset decimal units|
                |num_orders|no|number|True|The number of open orders at this level|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
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
        ```json
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        ```
    </section>
=== "Try it out"
    !!! example "dev"
        ```bash
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "stg"
        ```bash
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "testnet"
        ```bash
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "prod"
        ```bash
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "stream":"v1.book.d",
            "feed":["BTC_USDT_Perp@500-100-10"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
## Trade
### Public Trades
```
STREAM: v1.trade
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSPublicTradesFeedSelectorV1"
        Subscribes to a stream of Public Trades for an instrument.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |limit|l|number|True|The limit to query for. Defaults to 500; Max 1000|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.trade",
            "subs":["BTC_USDT_Perp@500"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSPublicTradesFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |selector|s1|string|True|Primary selector|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|PublicTrade|True|A public trade matching the request filter|
        ??? info "PublicTrade"
            All private RFQs and Private AXEs will be filtered out from the responses<br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |event_time|et|string|True|Time at which the event was emitted in unix nanoseconds|
            |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |is_taker_buyer|it|boolean|True|If taker was the buyer on the trade|
            |size|s|string|True|The number of assets being traded, expressed in underlying asset decimal units|
            |price|p|string|True|The traded price, expressed in `9` decimals|
            |mark_price|mp|string|True|The mark price of the instrument at point of trade, expressed in `9` decimals|
            |index_price|ip|string|True|The index price of the instrument at point of trade, expressed in `9` decimals|
            |interest_rate|ir|string|True|The interest rate of the underlying at point of trade, expressed in centibeeps (1/100th of a basis point)|
            |forward_price|fp|string|True|[Options] The forward price of the option at point of trade, expressed in `9` decimals|
            |trade_id|ti|string|True|A trade identifier|
            |venue|v|Venue|True|The venue where the trade occurred|
            |is_liquidation|il|boolean|True|If the trade was a liquidation|
            |trade_index|ti1|number|True|A trade index|
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
                "trade_id": "1234567890",
                "venue": "ORDERBOOK",
                "is_liquidation": false,
                "trade_index": "2"
            }
        }
        ```
        ```json
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
                "ti": "1234567890",
                "v": "ORDERBOOK",
                "il": false,
                "ti1": "2"
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
    !!! failure
        ```json
        ```
    </section>
=== "Try it out"
    !!! example "dev"
        ```bash
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "stg"
        ```bash
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "testnet"
        ```bash
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "prod"
        ```bash
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "stream":"v1.trade",
            "feed":["BTC_USDT_Perp@500"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
## Candlestick
### Candlestick
```
STREAM: v1.candle
```

=== "Feed Selector"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSCandlestickFeedSelectorV1"
        Subscribes to a stream of Kline/Candlestick updates for an instrument. A Kline is uniquely identified by its open time.<br>A new Kline is published every interval (if it exists). Upon subscription, the server will send the 5 most recent Kline for the requested interval.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |interval|i1|CandlestickInterval|True|The interval of each candlestick|
        |type|t|CandlestickType|True|The type of candlestick data to retrieve|
        ??? info "CandlestickInterval"
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
        ??? info "CandlestickType"
            |Value| Description |
            |-|-|
            |`TRADE` = 1|Tracks traded prices|
            |`MARK` = 2|Tracks mark prices|
            |`INDEX` = 3|Tracks index prices|
            |`MID` = 4|Tracks book mid prices|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **JSON RPC Request**
        ```json
        {
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ```
        ```json
        {
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":false
        }
        ```
        **JSON RPC Response**
        ```json
        {
            "stream":"v1.candle",
            "subs":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "unsubs":[]
        }
        ```
    </section>
=== "Feed Data"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "WSCandlestickFeedDataV1"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |stream|s|string|True|Stream name|
        |selector|s1|string|True|Primary selector|
        |sequence_number|sn|string|True|A running sequence number that determines global message order within the specific stream|
        |feed|f|Candlestick|True|A candlestick entry matching the request filters|
        ??? info "Candlestick"
            <br>

            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |open_time|ot|string|True|Open time of kline bar in unix nanoseconds|
            |close_time|ct|string|True|Close time of kline bar in unix nanosecond|
            |open|o|string|True|The open price, expressed in underlying currency resolution units|
            |close|c|string|True|The close price, expressed in underlying currency resolution units|
            |high|h|string|True|The high price, expressed in underlying currency resolution units|
            |low|l|string|True|The low price, expressed in underlying currency resolution units|
            |volume_u|vu|string|True|The underlying volume transacted, expressed in underlying asset decimal units|
            |volume_q|vq|string|True|The quote volume transacted, expressed in quote asset decimal units|
            |trades|t|number|True|The number of trades transacted|
            |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
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
                "volume_u": "123456.78",
                "volume_q": "123456.78",
                "trades": 123456,
                "instrument": "BTC_USDT_Perp"
            }
        }
        ```
        ```json
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
                "vu": "123456.78",
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        ```
    </section>
=== "Try it out"
    !!! example "dev"
        ```bash
        wscat -c "wss://market-data.dev.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "stg"
        ```bash
        wscat -c "wss://market-data.stg.gravitymarkets.io/ws" \
        -x '
        {
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "testnet"
        ```bash
        wscat -c "wss://market-data.testnet.grvt.io/ws" \
        -x '
        {
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
    !!! example "prod"
        ```bash
        wscat -c "wss://market-data.grvt.io/ws" \
        -x '
        {
            "stream":"v1.candle",
            "feed":["BTC_USDT_Perp@CI_1_M-TRADE"],
            "method":"subscribe",
            "is_full":true
        }
        ' -w 360
        ```
<hr class="solid">
