!!! info "[ApiTickerResponse](/../../schemas/api_ticker_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |Ticker|True|The mini ticker matching the request asset|
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
        |funding_rate_8h_curr<br>`fr` |string|False<br>`None`|DEPRECATED: To be removed in a future release. Please refer to the field `funding_rate` instead, for the funding rate being applied over `funding_interval_hours` (interval ending at `next_funding_time`).|
        |funding_rate_8h_avg<br>`fr1` |string|False<br>`None`|DEPRECATED: To be removed in a future release. Please refer to the field `funding_rate` instead, for the funding rate being applied over `funding_interval_hours` (interval ending at `next_funding_time`).|
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
        |funding_rate<br>`fr2` |string|False<br>`None`|The current indicative funding rate for the active interval, expressed in centibeeps. Absent for stable perps, which have `funding_rate_long_apr_pct` and `funding_rate_short_apr_pct` instead.|
        |next_funding_time<br>`nf` |string|False<br>`None`|Timestamp in nanoseconds when the current funding interval ends|
        |status<br>`s` |InstrumentStatus|False<br>`None`|The current status of the instrument|
        |session<br>`s1` |TradingSessionType|False<br>`None`|The current trading session of the instrument's underlying market|
        |long_open_interest<br>`lo` |string|False<br>`None`|The long open interest in the instrument, expressed in base asset decimal units. Excludes qualified-maker and DMM open interest.|
        |short_open_interest<br>`so` |string|False<br>`None`|The short open interest in the instrument, expressed in base asset decimal units. Excludes qualified-maker and DMM open interest.|
        |funding_rate_long_apr_pct<br>`fr3` |string|False<br>`None`|Stable perps only: the indicative annual rate for retail longs at the next charge, in percent a year (`'-5.5'` = retail longs pay 5.5%; positive = retail receives, negative = retail pays). Updated when the rates change. Absent for other kinds.|
        |funding_rate_short_apr_pct<br>`fr4` |string|False<br>`None`|Stable perps only: the indicative annual rate for retail shorts at the next charge, in percent a year (`'-5'` = retail shorts pay 5%; positive = retail receives, negative = retail pays). Updated when the rates change. Absent for other kinds.|
        ??? info "[InstrumentStatus](/../../schemas/instrument_status)"
            The lifecycle/trading status of an instrument on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`ACTIVE` = 1|Instrument is fully tradable|
            |`REDUCE_ONLY` = 2|Only position-reducing orders are accepted (e.g. pre-delist wind-down)|
            |`MAINTENANCE` = 3|Trading is temporarily paused for scheduled maintenance; cancel-only|
            |`HALTED` = 4|Underlying halted at its primary market (LULD, news pending); index and mark frozen|
            |`CLOSED` = 5|Outside trading window: daily maintenance break, weekend, holiday; cancel-only|
            |`PENDING` = 6|Instrument is created but not yet open for trading (pre-listing)|
            |`DELISTED` = 7|Instrument has been permanently removed|
        ??? info "[TradingSessionType](/../../schemas/trading_session_type)"
            Specifies different types of trading sessions<br>

            |Value| Description |
            |-|-|
            |`REGULAR` = 1|Core market hours. Full liquidity.|
            |`PRE_MARKET` = 2|Extended hours before open. Lower liquidity.|
            |`AFTER_MARKET` = 3|Extended hours after close. Lower liquidity.|
            |`OVERNIGHT` = 4|For 24/5 or specific overnight TradFi perps. Minimal liquidity.|
            |`CLOSE` = 5|Weekends, holidays, or daily maintenance windows.|
