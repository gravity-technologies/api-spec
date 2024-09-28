# MarketData APIs
All requests should be made using the `POST` HTTP method.

## Instrument
### Get Instrument
```
FULL ENDPOINT: full/v1/instrument
LITE ENDPOINT: lite/v1/instrument
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetInstrumentRequest"
        Fetch a single instrument by supplying the asset or instrument name<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "instrument": "BTC_USDT_Perp"
        }
        ```
        ```json
        {
            "i": "BTC_USDT_Perp"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetInstrumentResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|Instrument|True|The instrument matching the request asset|
        ??? info "Instrument"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |asset_id|ai|string|True|The asset ID used for instrument signing.|
            |underlying|u|Currency|True|The underlying currency|
            |quote|q|Currency|True|The quote currency|
            |kind|k|Kind|True|The kind of instrument|
            |expiry|e|string|False|The expiry time of the instrument in unix nanoseconds|
            |strike_price|sp|string|False|The strike price of the instrument, expressed in `9` decimals|
            |venues|v|[Venue]|True|Venues that this instrument can be traded at|
            |settlement_period|sp1|InstrumentSettlementPeriod|True|The settlement period of the instrument|
            |underlying_decimals|ud|number|True|The smallest denomination of the underlying asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |quote_decimals|qd|number|True|The smallest denomination of the quote asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |tick_size|ts|string|True|The size of a single tick, expressed in quote asset decimal units|
            |min_size|ms|string|True|The minimum contract size, expressed in underlying asset decimal units|
            |min_block_trade_size|mb|string|True|The minimum block trade size, expressed in underlying asset decimal units|
            |create_time|ct|string|True|Creation time in unix nanoseconds|
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
            ??? info "Kind"
                The list of asset kinds that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`PERPETUAL` = 1|the perpetual asset kind|
                |`FUTURE` = 2|the future asset kind|
                |`CALL` = 3|the call option asset kind|
                |`PUT` = 4|the put option asset kind|
            ??? info "Venue"
                The list of Trading Venues that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`ORDERBOOK` = 1|the trade is cleared on the orderbook venue|
            ??? info "InstrumentSettlementPeriod"
                |Value| Description |
                |-|-|
                |`PERPETUAL` = 1|Instrument settles through perpetual funding cycles|
                |`DAILY` = 2|Instrument settles at an expiry date, marked as a daily instrument|
                |`WEEKLY` = 3|Instrument settles at an expiry date, marked as a weekly instrument|
                |`MONTHLY` = 4|Instrument settles at an expiry date, marked as a monthly instrument|
                |`QUARTERLY` = 5|Instrument settles at an expiry date, marked as a quarterly instrument|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": {
                "instrument": "BTC_USDT_Perp",
                "asset_id": "0x030501",
                "underlying": "BTC",
                "quote": "USDT",
                "kind": "PERPETUAL",
                "expiry": "1697788800000000000",
                "strike_price": "65038.01",
                "venues": ["ORDERBOOK"],
                "settlement_period": "PERPETUAL",
                "underlying_decimals": 3,
                "quote_decimals": 3,
                "tick_size": "0.01",
                "min_size": "0.01",
                "min_block_trade_size": "5.0",
                "create_time": "1697788800000000000"
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
        |1003|404|Data Not Found|
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
            "code":1003,
            "message":"Data Not Found",
            "status":404
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/instrument' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/instrument' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/instrument' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/instrument' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
<hr class="solid">
### Get All Instruments
```
FULL ENDPOINT: full/v1/all_instruments
LITE ENDPOINT: lite/v1/all_instruments
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetAllInstrumentsRequest"
        Fetch all instruments<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |is_active|ia|boolean|False|Fetch only active instruments|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "is_active": true
        }
        ```
        ```json
        {
            "ia": true
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetAllInstrumentsResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[Instrument]|True|List of instruments|
        ??? info "Instrument"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |asset_id|ai|string|True|The asset ID used for instrument signing.|
            |underlying|u|Currency|True|The underlying currency|
            |quote|q|Currency|True|The quote currency|
            |kind|k|Kind|True|The kind of instrument|
            |expiry|e|string|False|The expiry time of the instrument in unix nanoseconds|
            |strike_price|sp|string|False|The strike price of the instrument, expressed in `9` decimals|
            |venues|v|[Venue]|True|Venues that this instrument can be traded at|
            |settlement_period|sp1|InstrumentSettlementPeriod|True|The settlement period of the instrument|
            |underlying_decimals|ud|number|True|The smallest denomination of the underlying asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |quote_decimals|qd|number|True|The smallest denomination of the quote asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |tick_size|ts|string|True|The size of a single tick, expressed in quote asset decimal units|
            |min_size|ms|string|True|The minimum contract size, expressed in underlying asset decimal units|
            |min_block_trade_size|mb|string|True|The minimum block trade size, expressed in underlying asset decimal units|
            |create_time|ct|string|True|Creation time in unix nanoseconds|
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
            ??? info "Kind"
                The list of asset kinds that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`PERPETUAL` = 1|the perpetual asset kind|
                |`FUTURE` = 2|the future asset kind|
                |`CALL` = 3|the call option asset kind|
                |`PUT` = 4|the put option asset kind|
            ??? info "Venue"
                The list of Trading Venues that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`ORDERBOOK` = 1|the trade is cleared on the orderbook venue|
            ??? info "InstrumentSettlementPeriod"
                |Value| Description |
                |-|-|
                |`PERPETUAL` = 1|Instrument settles through perpetual funding cycles|
                |`DAILY` = 2|Instrument settles at an expiry date, marked as a daily instrument|
                |`WEEKLY` = 3|Instrument settles at an expiry date, marked as a weekly instrument|
                |`MONTHLY` = 4|Instrument settles at an expiry date, marked as a monthly instrument|
                |`QUARTERLY` = 5|Instrument settles at an expiry date, marked as a quarterly instrument|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "instrument": "BTC_USDT_Perp",
                "asset_id": "0x030501",
                "underlying": "BTC",
                "quote": "USDT",
                "kind": "PERPETUAL",
                "expiry": "1697788800000000000",
                "strike_price": "65038.01",
                "venues": ["ORDERBOOK"],
                "settlement_period": "PERPETUAL",
                "underlying_decimals": 3,
                "quote_decimals": 3,
                "tick_size": "0.01",
                "min_size": "0.01",
                "min_block_trade_size": "5.0",
                "create_time": "1697788800000000000"
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/all_instruments' \
        --data '{
            "is_active": true
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/all_instruments' \
        --data '{
            "is_active": true
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/all_instruments' \
        --data '{
            "is_active": true
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/all_instruments' \
        --data '{
            "is_active": true
        }
        '
        ```
<hr class="solid">
### Get Filtered Instruments
```
FULL ENDPOINT: full/v1/instruments
LITE ENDPOINT: lite/v1/instruments
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetFilteredInstrumentsRequest"
        Fetch a list of instruments based on the filters provided<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |kind|k|[Kind]|False|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |underlying|u|[Currency]|False|The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned|
        |quote|q|[Currency]|False|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
        |is_active|ia|boolean|False|Request for active instruments only|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 100000|
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
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        ```
        ```json
        {
            "k": ["PERPETUAL"],
            "u": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "ia": true,
            "l": 500
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetFilteredInstrumentsResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[Instrument]|True|The instruments matching the request filter|
        ??? info "Instrument"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |asset_id|ai|string|True|The asset ID used for instrument signing.|
            |underlying|u|Currency|True|The underlying currency|
            |quote|q|Currency|True|The quote currency|
            |kind|k|Kind|True|The kind of instrument|
            |expiry|e|string|False|The expiry time of the instrument in unix nanoseconds|
            |strike_price|sp|string|False|The strike price of the instrument, expressed in `9` decimals|
            |venues|v|[Venue]|True|Venues that this instrument can be traded at|
            |settlement_period|sp1|InstrumentSettlementPeriod|True|The settlement period of the instrument|
            |underlying_decimals|ud|number|True|The smallest denomination of the underlying asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |quote_decimals|qd|number|True|The smallest denomination of the quote asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |tick_size|ts|string|True|The size of a single tick, expressed in quote asset decimal units|
            |min_size|ms|string|True|The minimum contract size, expressed in underlying asset decimal units|
            |min_block_trade_size|mb|string|True|The minimum block trade size, expressed in underlying asset decimal units|
            |create_time|ct|string|True|Creation time in unix nanoseconds|
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
            ??? info "Kind"
                The list of asset kinds that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`PERPETUAL` = 1|the perpetual asset kind|
                |`FUTURE` = 2|the future asset kind|
                |`CALL` = 3|the call option asset kind|
                |`PUT` = 4|the put option asset kind|
            ??? info "Venue"
                The list of Trading Venues that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`ORDERBOOK` = 1|the trade is cleared on the orderbook venue|
            ??? info "InstrumentSettlementPeriod"
                |Value| Description |
                |-|-|
                |`PERPETUAL` = 1|Instrument settles through perpetual funding cycles|
                |`DAILY` = 2|Instrument settles at an expiry date, marked as a daily instrument|
                |`WEEKLY` = 3|Instrument settles at an expiry date, marked as a weekly instrument|
                |`MONTHLY` = 4|Instrument settles at an expiry date, marked as a monthly instrument|
                |`QUARTERLY` = 5|Instrument settles at an expiry date, marked as a quarterly instrument|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "instrument": "BTC_USDT_Perp",
                "asset_id": "0x030501",
                "underlying": "BTC",
                "quote": "USDT",
                "kind": "PERPETUAL",
                "expiry": "1697788800000000000",
                "strike_price": "65038.01",
                "venues": ["ORDERBOOK"],
                "settlement_period": "PERPETUAL",
                "underlying_decimals": 3,
                "quote_decimals": 3,
                "tick_size": "0.01",
                "min_size": "0.01",
                "min_block_trade_size": "5.0",
                "create_time": "1697788800000000000"
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/instruments' \
        --data '{
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/instruments' \
        --data '{
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/instruments' \
        --data '{
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/instruments' \
        --data '{
            "kind": ["PERPETUAL"],
            "underlying": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        '
        ```
<hr class="solid">
## Ticker
### Mini Ticker
```
FULL ENDPOINT: full/v1/mini
LITE ENDPOINT: lite/v1/mini
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiMiniTickerRequest"
        Retrieves a single mini ticker value for a single instrument. Please do not use this to repeatedly poll for data -- a websocket subscription is much more performant, and useful.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "instrument": "BTC_USDT_Perp"
        }
        ```
        ```json
        {
            "i": "BTC_USDT_Perp"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiMiniTickerResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|MiniTicker|True|The mini ticker matching the request asset|
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
            "results": {
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
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/mini' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/mini' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/mini' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/mini' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
<hr class="solid">
### Ticker
```
FULL ENDPOINT: full/v1/ticker
LITE ENDPOINT: lite/v1/ticker
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTickerRequest"
        Retrieves a single ticker value for a single instrument. Please do not use this to repeatedly poll for data -- a websocket subscription is much more performant, and useful.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "instrument": "BTC_USDT_Perp"
        }
        ```
        ```json
        {
            "i": "BTC_USDT_Perp"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTickerResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|Ticker|True|The mini ticker matching the request asset|
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
            "results": {
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
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/ticker' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/ticker' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/ticker' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/ticker' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
<hr class="solid">
## Orderbook
### Orderbook Levels
```
FULL ENDPOINT: full/v1/book
LITE ENDPOINT: lite/v1/book
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiOrderbookLevelsRequest"
        Retrieves aggregated price depth for a single instrument, with a maximum depth of 10 levels. Do not use this to poll for data -- a websocket subscription is much more performant, and useful.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |depth|d|number|True|Depth of the order book to be retrieved (API/Snapshot max is 100, Delta max is 1000)|
        |aggregate|a|number|True|The number of levels to aggregate into one level (1 = no aggregation, 10/100/1000 = aggregate 10/100/1000 levels into 1)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "instrument": "BTC_USDT_Perp",
            "depth": 100,
            "aggregate": 10
        }
        ```
        ```json
        {
            "i": "BTC_USDT_Perp",
            "d": 100,
            "a": 10
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiOrderbookLevelsResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|OrderbookLevels|True|The orderbook levels objects matching the request asset|
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
            "results": {
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
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1001|500|Internal Server Error|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/book' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "depth": 100,
            "aggregate": 10
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/book' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "depth": 100,
            "aggregate": 10
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/book' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "depth": 100,
            "aggregate": 10
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/book' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "depth": 100,
            "aggregate": 10
        }
        '
        ```
<hr class="solid">
## Trade
### Public Trades
```
FULL ENDPOINT: full/v1/trades
LITE ENDPOINT: lite/v1/trades
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPublicTradesRequest"
        Retrieves up to 1000 of the most recent public trades in any given instrument. Do not use this to poll for data -- a websocket subscription is much more performant, and useful.<br>This endpoint offers public trading data, use the Trading APIs instead to query for your personalized trade tape.<br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |limit|l|number|True|The limit to query for. Defaults to 500; Max 1000|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        ```
        ```json
        {
            "i": "BTC_USDT_Perp",
            "l": 500
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPublicTradesResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[PublicTrade]|True|The public trades matching the request asset|
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
            "results": [{
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/trades' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/trades' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/trades' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/trades' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        '
        ```
<hr class="solid">
### Public Trade History
```
FULL ENDPOINT: full/v1/trade_history
LITE ENDPOINT: lite/v1/trade_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPublicTradeHistoryRequest"
        Perform historical lookup of public trades in any given instrument.<br>This endpoint offers public trading data, use the Trading APIs instead to query for your personalized trade tape.<br>Only data from the last three months will be retained.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |start_time|st|string|False|The start time to apply in nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned|
        |end_time|et|string|False|The end time to apply in nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the query from|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "instrument": "BTC_USDT_Perp",
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "i": "BTC_USDT_Perp",
            "st": 1697788800000000000,
            "et": 1697788800000000000,
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiPublicTradeHistoryResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[PublicTrade]|True|The public trades matching the request asset|
        |next|n|string|False|The cursor to indicate when to start the next query from|
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
            "results": [{
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/trade_history' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/trade_history' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/trade_history' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/trade_history' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": 1697788800000000000,
            "end_time": 1697788800000000000,
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
## Candlestick
### Candlestick
```
FULL ENDPOINT: full/v1/kline
LITE ENDPOINT: lite/v1/kline
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiCandlestickRequest"
        Kline/Candlestick bars for an instrument. Klines are uniquely identified by their instrument, type, interval, and open time.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |interval|i1|CandlestickInterval|True|The interval of each candlestick|
        |type|t|CandlestickType|True|The type of candlestick data to retrieve|
        |start_time|st|string|False|Start time of kline data in unix nanoseconds|
        |end_time|et|string|False|End time of kline data in unix nanoseconds|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the query from|
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
        ```json
        {
            "instrument": "BTC_USDT_Perp",
            "interval": "CI_1_M",
            "type": "TRADE",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "i": "BTC_USDT_Perp",
            "i1": "CI_1_M",
            "t": "TRADE",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiCandlestickResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[Candlestick]|True|The candlestick result set for given interval|
        |next|n|string|False|The cursor to indicate when to start the next query from|
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
            "results": [{
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/kline' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "interval": "CI_1_M",
            "type": "TRADE",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/kline' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "interval": "CI_1_M",
            "type": "TRADE",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/kline' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "interval": "CI_1_M",
            "type": "TRADE",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/kline' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "interval": "CI_1_M",
            "type": "TRADE",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
## Settlement
### Funding Rate
```
FULL ENDPOINT: full/v1/funding
LITE ENDPOINT: lite/v1/funding
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiFundingRateRequest"
        Lookup the historical funding rate of various pairs.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
        |start_time|st|string|False|Start time of funding rate in unix nanoseconds|
        |end_time|et|string|False|End time of funding rate in unix nanoseconds|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the query from|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ```json
        {
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        ```json
        {
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiFundingRateResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[FundingRate]|True|The funding rate result set for given interval|
        |next|n|string|False|The cursor to indicate when to start the next query from|
        ??? info "FundingRate"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |instrument|i|string|True|The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]<br>For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]<br>For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]<br>For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]|
            |funding_rate|fr|number|True|The funding rate of the instrument, expressed in centibeeps|
            |funding_time|ft|string|True|The funding timestamp of the funding rate, expressed in unix nanoseconds|
            |mark_price|mp|string|True|The mark price of the instrument at funding timestamp, expressed in `9` decimals|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ```json
        {
            "results": [{
                "instrument": "BTC_USDT_Perp",
                "funding_rate": "6.78",
                "funding_time": "1697788800000000000",
                "mark_price": "65038.01"
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/funding' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/funding' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/funding' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/funding' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
### Settlement Price
```
FULL ENDPOINT: full/v1/settlement
LITE ENDPOINT: lite/v1/settlement
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiSettlementPriceRequest"
        Lookup the historical settlement price of various pairs.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |underlying|u|Currency|True|The underlying currency to select|
        |quote|q|Currency|True|The quote currency to select|
        |expiration|e|string|True|The expiration time to select in unix nanoseconds|
        |strike_price|sp|string|True|The strike price to select|
        |start_time|st|string|False|Start time of kline data in unix nanoseconds|
        |end_time|et|string|False|End time of kline data in unix nanoseconds|
        |limit|l|number|False|The limit to query for. Defaults to 500; Max 1000|
        |cursor|c|string|False|The cursor to indicate when to start the query from|
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
            "underlying": "BTC",
            "quote": "USDT",
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 20,
            "cursor": ""
        }
        ```
        ```json
        {
            "u": "BTC",
            "q": "USDT",
            "e": "1697788800000000000",
            "sp": 65000.0,
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 20,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiSettlementPriceResponse"
        |Name|Lite|Type|Required| Description |
        |-|-|-|-|-|
        |results|r|[APISettlementPrice]|True|The funding rate result set for given interval|
        |next|n|string|False|The cursor to indicate when to start the next query from|
        ??? info "APISettlementPrice"
            |Name|Lite|Type|Required| Description |
            |-|-|-|-|-|
            |underlying|u|Currency|True|The underlying currency of the settlement price|
            |quote|q|Currency|True|The quote currency of the settlement price|
            |settlement_time|st|string|True|The settlement timestamp of the settlement price, expressed in unix nanoseconds|
            |settlement_price|sp|string|True|The settlement price, expressed in `9` decimals|
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
    !!! success
        ```json
        {
            "results": [{
                "underlying": "BTC",
                "quote": "USDT",
                "settlement_time": "1697788800000000000",
                "settlement_price": "65038.01"
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
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        ```json
        {
            "code":1001,
            "message":"Internal Server Error",
            "status":500
        }
        ```
    </section>
=== "Try it out"
    !!! example "Try DEV"
        ```bash
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/settlement' \
        --data '{
            "underlying": "BTC",
            "quote": "USDT",
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 20,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG"
        ```bash
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/settlement' \
        --data '{
            "underlying": "BTC",
            "quote": "USDT",
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 20,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET"
        ```bash
        curl --location 'https://market-data.testnet.grvt.io/full/v1/settlement' \
        --data '{
            "underlying": "BTC",
            "quote": "USDT",
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 20,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD"
        ```bash
        curl --location 'https://market-data.grvt.io/full/v1/settlement' \
        --data '{
            "underlying": "BTC",
            "quote": "USDT",
            "expiration": "1697788800000000000",
            "strike_price": 65000.0,
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 20,
            "cursor": ""
        }
        '
        ```
<hr class="solid">
