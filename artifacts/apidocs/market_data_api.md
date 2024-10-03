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

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ``` { .json .copy }
        {
            "instrument": "BTC_USDT_Perp"
        }
        ```
        ``` { .json .copy }
        {
            "i": "BTC_USDT_Perp"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetInstrumentResponse"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |Instrument|True|The instrument matching the request asset|
        ??? info "Instrument"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |instrument_hash<br>`ih` |string|True|The asset ID used for instrument signing.|
            |base<br>`b` |Currency|True|The base currency|
            |quote<br>`q` |Currency|True|The quote currency|
            |kind<br>`k` |Kind|True|The kind of instrument|
            |venues<br>`v` |[Venue]|True|Venues that this instrument can be traded at|
            |settlement_period<br>`sp1` |InstrumentSettlementPeriod|True|The settlement period of the instrument|
            |base_decimals<br>`bd` |number|True|The smallest denomination of the base asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |quote_decimals<br>`qd` |number|True|The smallest denomination of the quote asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |tick_size<br>`ts` |string|True|The size of a single tick, expressed in quote asset decimal units|
            |min_size<br>`ms` |string|True|The minimum contract size, expressed in base asset decimal units|
            |create_time<br>`ct` |string|True|Creation time in unix nanoseconds|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
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
                |`RFQ` = 2|the trade is cleared on the RFQ venue|
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
        ``` { .json .copy }
        {
            "result": {
                "instrument": "BTC_USDT_Perp",
                "instrument_hash": "0x030501",
                "base": "BTC",
                "quote": "USDT",
                "kind": "PERPETUAL",
                "venues": ["ORDERBOOK"],
                "settlement_period": "PERPETUAL",
                "base_decimals": 3,
                "quote_decimals": 3,
                "tick_size": "0.01",
                "min_size": "0.01",
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
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
        |1004|404|Data Not Found|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/instrument' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/instrument' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/full/v1/instrument' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/full/v1/instrument' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/instrument' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/instrument' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/instrument' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/instrument' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    </section>
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

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |is_active<br>`ia` |boolean|False<br>`false`|Fetch only active instruments|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ``` { .json .copy }
        {
            "is_active": true
        }
        ```
        ``` { .json .copy }
        {
            "ia": true
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetAllInstrumentsResponse"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |[Instrument]|True|List of instruments|
        ??? info "Instrument"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |instrument_hash<br>`ih` |string|True|The asset ID used for instrument signing.|
            |base<br>`b` |Currency|True|The base currency|
            |quote<br>`q` |Currency|True|The quote currency|
            |kind<br>`k` |Kind|True|The kind of instrument|
            |venues<br>`v` |[Venue]|True|Venues that this instrument can be traded at|
            |settlement_period<br>`sp1` |InstrumentSettlementPeriod|True|The settlement period of the instrument|
            |base_decimals<br>`bd` |number|True|The smallest denomination of the base asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |quote_decimals<br>`qd` |number|True|The smallest denomination of the quote asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |tick_size<br>`ts` |string|True|The size of a single tick, expressed in quote asset decimal units|
            |min_size<br>`ms` |string|True|The minimum contract size, expressed in base asset decimal units|
            |create_time<br>`ct` |string|True|Creation time in unix nanoseconds|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
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
                |`RFQ` = 2|the trade is cleared on the RFQ venue|
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
        ``` { .json .copy }
        {
            "result": [{
                "instrument": "BTC_USDT_Perp",
                "instrument_hash": "0x030501",
                "base": "BTC",
                "quote": "USDT",
                "kind": "PERPETUAL",
                "venues": ["ORDERBOOK"],
                "settlement_period": "PERPETUAL",
                "base_decimals": 3,
                "quote_decimals": 3,
                "tick_size": "0.01",
                "min_size": "0.01",
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
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/all_instruments' \
        --data '{
            "is_active": true
        }
        '
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/all_instruments' \
        --data '{
            "is_active": true
        }
        '
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/full/v1/all_instruments' \
        --data '{
            "is_active": true
        }
        '
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/full/v1/all_instruments' \
        --data '{
            "is_active": true
        }
        '
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/all_instruments' \
        --data '{
            "ia": true
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/all_instruments' \
        --data '{
            "ia": true
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/all_instruments' \
        --data '{
            "ia": true
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/all_instruments' \
        --data '{
            "ia": true
        }
        '
        ```
    </section>
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

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |kind<br>`k` |[Kind]|False<br>`all`|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
        |base<br>`b` |[Currency]|False<br>`all`|The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned|
        |quote<br>`q` |[Currency]|False<br>`all`|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
        |is_active<br>`ia` |boolean|False<br>`false`|Request for active instruments only|
        |limit<br>`l` |number|False<br>`500`|The limit to query for. Defaults to 500; Max 100000|
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
            |`USD` = 1|the USD fiat currency|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
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
    !!! question "Query"
        ``` { .json .copy }
        {
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        ```
        ``` { .json .copy }
        {
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "ia": true,
            "l": 500
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiGetFilteredInstrumentsResponse"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |[Instrument]|True|The instruments matching the request filter|
        ??? info "Instrument"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |instrument_hash<br>`ih` |string|True|The asset ID used for instrument signing.|
            |base<br>`b` |Currency|True|The base currency|
            |quote<br>`q` |Currency|True|The quote currency|
            |kind<br>`k` |Kind|True|The kind of instrument|
            |venues<br>`v` |[Venue]|True|Venues that this instrument can be traded at|
            |settlement_period<br>`sp1` |InstrumentSettlementPeriod|True|The settlement period of the instrument|
            |base_decimals<br>`bd` |number|True|The smallest denomination of the base asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |quote_decimals<br>`qd` |number|True|The smallest denomination of the quote asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
            |tick_size<br>`ts` |string|True|The size of a single tick, expressed in quote asset decimal units|
            |min_size<br>`ms` |string|True|The minimum contract size, expressed in base asset decimal units|
            |create_time<br>`ct` |string|True|Creation time in unix nanoseconds|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
            ??? info "Currency"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
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
                |`RFQ` = 2|the trade is cleared on the RFQ venue|
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
        ``` { .json .copy }
        {
            "result": [{
                "instrument": "BTC_USDT_Perp",
                "instrument_hash": "0x030501",
                "base": "BTC",
                "quote": "USDT",
                "kind": "PERPETUAL",
                "venues": ["ORDERBOOK"],
                "settlement_period": "PERPETUAL",
                "base_decimals": 3,
                "quote_decimals": 3,
                "tick_size": "0.01",
                "min_size": "0.01",
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
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/instruments' \
        --data '{
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        '
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/instruments' \
        --data '{
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        '
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/full/v1/instruments' \
        --data '{
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        '
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/full/v1/instruments' \
        --data '{
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "is_active": true,
            "limit": 500
        }
        '
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/instruments' \
        --data '{
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "ia": true,
            "l": 500
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/instruments' \
        --data '{
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "ia": true,
            "l": 500
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/instruments' \
        --data '{
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "ia": true,
            "l": 500
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/instruments' \
        --data '{
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "ia": true,
            "l": 500
        }
        '
        ```
    </section>
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

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ``` { .json .copy }
        {
            "instrument": "BTC_USDT_Perp"
        }
        ```
        ``` { .json .copy }
        {
            "i": "BTC_USDT_Perp"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiMiniTickerResponse"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |MiniTicker|True|The mini ticker matching the request asset|
        ??? info "MiniTicker"
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
            "result": {
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
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
        |1004|404|Data Not Found|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/mini' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/mini' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/full/v1/mini' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/full/v1/mini' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/mini' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/mini' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/mini' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/mini' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    </section>
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

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ``` { .json .copy }
        {
            "instrument": "BTC_USDT_Perp"
        }
        ```
        ``` { .json .copy }
        {
            "i": "BTC_USDT_Perp"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTickerResponse"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |Ticker|True|The mini ticker matching the request asset|
        ??? info "Ticker"
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
            "result": {
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
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
        |1004|404|Data Not Found|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/ticker' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/ticker' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/full/v1/ticker' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/full/v1/ticker' \
        --data '{
            "instrument": "BTC_USDT_Perp"
        }
        '
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/ticker' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/ticker' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/ticker' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/ticker' \
        --data '{
            "i": "BTC_USDT_Perp"
        }
        '
        ```
    </section>
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

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |depth<br>`d` |number|True|Depth of the order book to be retrieved (10, 50, 100, 500)|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ``` { .json .copy }
        {
            "instrument": "BTC_USDT_Perp",
            "depth": 50
        }
        ```
        ``` { .json .copy }
        {
            "i": "BTC_USDT_Perp",
            "d": 50
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiOrderbookLevelsResponse"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |OrderbookLevels|True|The orderbook levels objects matching the request asset|
        ??? info "OrderbookLevels"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |bids<br>`b` |[OrderbookLevel]|True|The list of best bids up till query depth|
            |asks<br>`a` |[OrderbookLevel]|True|The list of best asks up till query depth|
            ??? info "OrderbookLevel"
                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |price<br>`p` |string|True|The price of the level, expressed in `9` decimals|
                |size<br>`s` |string|True|The number of assets offered, expressed in base asset decimal units|
                |num_orders<br>`no` |number|True|The number of open orders at this level|
            ??? info "OrderbookLevel"
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
            "result": {
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
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
        |1004|404|Data Not Found|
        |3000|400|Instrument is invalid|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        {
            "code":1004,
            "message":"Data Not Found",
            "status":404
        }
        {
            "code":3000,
            "message":"Instrument is invalid",
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
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/book' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "depth": 50
        }
        '
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/book' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "depth": 50
        }
        '
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/full/v1/book' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "depth": 50
        }
        '
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/full/v1/book' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "depth": 50
        }
        '
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/book' \
        --data '{
            "i": "BTC_USDT_Perp",
            "d": 50
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/book' \
        --data '{
            "i": "BTC_USDT_Perp",
            "d": 50
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/book' \
        --data '{
            "i": "BTC_USDT_Perp",
            "d": 50
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/book' \
        --data '{
            "i": "BTC_USDT_Perp",
            "d": 50
        }
        '
        ```
    </section>
<hr class="solid">
## Trade
### Trade
```
FULL ENDPOINT: full/v1/trade
LITE ENDPOINT: lite/v1/trade
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTradeRequest"
        Retrieves up to 1000 of the most recent trades in any given instrument. Do not use this to poll for data -- a websocket subscription is much more performant, and useful.<br>This endpoint offers public trading data, use the Trading APIs instead to query for your personalized trade tape.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |limit<br>`l` |number|True|The limit to query for. Defaults to 500; Max 1000|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ``` { .json .copy }
        {
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        ```
        ``` { .json .copy }
        {
            "i": "BTC_USDT_Perp",
            "l": 500
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTradeResponse"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |[Trade]|True|The public trades matching the request asset|
        ??? info "Trade"
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
            ??? info "Venue"
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
            "result": [{
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
            }]
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/trade' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        '
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/trade' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        '
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/full/v1/trade' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        '
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/full/v1/trade' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "limit": 500
        }
        '
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/trade' \
        --data '{
            "i": "BTC_USDT_Perp",
            "l": 500
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/trade' \
        --data '{
            "i": "BTC_USDT_Perp",
            "l": 500
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/trade' \
        --data '{
            "i": "BTC_USDT_Perp",
            "l": 500
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/trade' \
        --data '{
            "i": "BTC_USDT_Perp",
            "l": 500
        }
        '
        ```
    </section>
<hr class="solid">
### Trade History
```
FULL ENDPOINT: full/v1/trade_history
LITE ENDPOINT: lite/v1/trade_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "ApiTradeHistoryRequest"
        Perform historical lookup of public trades in any given instrument.<br>This endpoint offers public trading data, use the Trading APIs instead to query for your personalized trade tape.<br>Only data from the last three months will be retained.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |start_time<br>`st` |string|False<br>`0`|The start time to apply in nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned|
        |end_time<br>`et` |string|False<br>`now()`|The end time to apply in nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned|
        |limit<br>`l` |number|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
        |cursor<br>`c` |string|False<br>`''`|The cursor to indicate when to start the query from|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ``` { .json .copy }
        {
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        ``` { .json .copy }
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
    !!! info "ApiTradeHistoryResponse"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |[Trade]|True|The public trades matching the request asset|
        |next<br>`n` |string|False<br>`''`|The cursor to indicate when to start the next query from|
        ??? info "Trade"
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
            ??? info "Venue"
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
            "result": [{
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
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/full/v1/trade_history' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try STG Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/full/v1/trade_history' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/full/v1/trade_history' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    !!! example "Try PROD Full"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/full/v1/trade_history' \
        --data '{
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        '
        ```
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/trade_history' \
        --data '{
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/trade_history' \
        --data '{
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/trade_history' \
        --data '{
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/trade_history' \
        --data '{
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    </section>
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

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |interval<br>`i1` |CandlestickInterval|True|The interval of each candlestick|
        |type<br>`t` |CandlestickType|True|The type of candlestick data to retrieve|
        |start_time<br>`st` |string|False<br>`0`|Start time of kline data in unix nanoseconds|
        |end_time<br>`et` |string|False<br>`now()`|End time of kline data in unix nanoseconds|
        |limit<br>`l` |number|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
        |cursor<br>`c` |string|False<br>`''`|The cursor to indicate when to start the query from|
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
        ``` { .json .copy }
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
        ``` { .json .copy }
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
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |[Candlestick]|True|The candlestick result set for given interval|
        |next<br>`n` |string|False<br>`''`|The cursor to indicate when to start the next query from|
        ??? info "Candlestick"
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
            "result": [{
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
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
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
    !!! example "Try STG Full"
        ``` { .bash .copy }
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
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
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
    !!! example "Try PROD Full"
        ``` { .bash .copy }
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
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/kline' \
        --data '{
            "i": "BTC_USDT_Perp",
            "i1": "CI_1_M",
            "t": "TRADE",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/kline' \
        --data '{
            "i": "BTC_USDT_Perp",
            "i1": "CI_1_M",
            "t": "TRADE",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/kline' \
        --data '{
            "i": "BTC_USDT_Perp",
            "i1": "CI_1_M",
            "t": "TRADE",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/kline' \
        --data '{
            "i": "BTC_USDT_Perp",
            "i1": "CI_1_M",
            "t": "TRADE",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    </section>
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
        Lookup the historical funding rate of a perpetual future.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |start_time<br>`st` |string|False<br>`0`|Start time of funding rate in unix nanoseconds|
        |end_time<br>`et` |string|False<br>`now()`|End time of funding rate in unix nanoseconds|
        |limit<br>`l` |number|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
        |cursor<br>`c` |string|False<br>`''`|The cursor to indicate when to start the query from|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        ``` { .json .copy }
        {
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        ``` { .json .copy }
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
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |result<br>`r` |[FundingRate]|True|The funding rate result set for given interval|
        |next<br>`n` |string|False<br>`''`|The cursor to indicate when to start the next query from|
        ??? info "FundingRate"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
            |funding_rate<br>`fr` |number|True|The funding rate of the instrument, expressed in centibeeps|
            |funding_time<br>`ft` |string|True|The funding timestamp of the funding rate, expressed in unix nanoseconds|
            |mark_price<br>`mp` |string|True|The mark price of the instrument at funding timestamp, expressed in `9` decimals|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        ``` { .json .copy }
        {
            "result": [{
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
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
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
            "code":1003,
            "message":"Request could not be processed due to malformed syntax",
            "status":400
        }
        ```
    </section>
=== "Try it out"
    <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
    !!! example "Try DEV Full"
        ``` { .bash .copy }
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
    !!! example "Try STG Full"
        ``` { .bash .copy }
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
    !!! example "Try TESTNET Full"
        ``` { .bash .copy }
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
    !!! example "Try PROD Full"
        ``` { .bash .copy }
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
    </section>
    <section markdown="1" style="float: right; width: 50%;">
    !!! example "Try DEV Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.dev.gravitymarkets.io/lite/v1/funding' \
        --data '{
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try STG Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.stg.gravitymarkets.io/lite/v1/funding' \
        --data '{
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try TESTNET Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.testnet.grvt.io/lite/v1/funding' \
        --data '{
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    !!! example "Try PROD Lite"
        ``` { .bash .copy }
        curl --location 'https://market-data.grvt.io/lite/v1/funding' \
        --data '{
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        '
        ```
    </section>
<hr class="solid">
