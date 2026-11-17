!!! info "[ApiGetInstrumentResponse](/../../schemas/api_get_instrument_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |InstrumentDisplay|True|The instrument matching the request asset|
    ??? info "[InstrumentDisplay](/../../schemas/instrument_display)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |instrument_hash<br>`ih` |string|True|The asset ID used for instrument signing.|
        |base<br>`b` |string|True|The base currency|
        |quote<br>`q` |string|True|The quote currency|
        |kind<br>`k` |Kind|True|The kind of instrument|
        |venues<br>`v` |[Venue]|True|Venues that this instrument can be traded at|
        |settlement_period<br>`sp1` |InstrumentSettlementPeriod|False<br>`None`|The settlement period of the instrument|
        |base_decimals<br>`bd` |integer|True|The smallest denomination of the base asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
        |quote_decimals<br>`qd` |integer|True|The smallest denomination of the quote asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)|
        |tick_size<br>`ts` |string|True|The size of a single tick, expressed in price decimal units|
        |min_size<br>`ms` |string|True|The minimum contract size, expressed in base asset decimal units|
        |create_time<br>`ct` |string|True|Creation time in unix nanoseconds|
        |max_position_size<br>`mp` |string|False<br>`None`|The maximum position size, expressed in base asset decimal units|
        |funding_interval_hours<br>`fi` |integer|False<br>`None`|Defines the funding interval to be applied.|
        |adjusted_funding_rate_cap<br>`af` |string|False<br>`None`|Funding rate cap over the defined `intervalHours`.|
        |adjusted_funding_rate_floor<br>`af1` |string|False<br>`None`|Funding rate floor over the defined `intervalHours`.|
        |min_notional<br>`mn` |string|True|The minimum order notional value, expressed in quote currency decimal units|
        |asset_class<br>`ac` |AssetClass|False<br>`None`|The asset class of the underlying the instrument tracks|
        |status<br>`s` |InstrumentStatus|False<br>`None`|The current lifecycle/trading status of the instrument|
        |guaranteed_exit_band<br>`ge` |string|False<br>`None`|The guaranteed exit band, expressed in percentage points|
        |spread_penalty_tolerance<br>`sp2` |string|False<br>`None`|The spread penalty tolerance, expressed in percentage points|
        |funding_cap_adjustment_time<br>`fc` |string|False<br>`None`|Timestamp in unix nanoseconds at which the funding cap adjustment applies|
        |funding_cap_adjustment_value<br>`fc1` |string|False<br>`None`|The funding cap adjustment value, expressed as a decimal daily rate|
        |triple_swap_day<br>`ts2` |DayOfWeek|False<br>`None`|Stable perps only: the weekday whose daily funding charge covers 3 days (the weekend)|
        ??? info "[Kind](/../../schemas/kind)"
            The list of asset kinds that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`PERPETUAL` = 1|the perpetual asset kind|
            |`FUTURE` = 2|the future asset kind|
            |`CALL` = 3|the call option asset kind|
            |`PUT` = 4|the put option asset kind|
            |`STABLE_PERP` = 9|Stable Funding Perp on an RWA underlying, USDC-settled|
        ??? info "[Venue](/../../schemas/venue)"
            The list of Trading Venues that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`ORDERBOOK` = 1|the trade is cleared on the orderbook venue|
            |`RFQ` = 2|the trade is cleared on the RFQ venue|
        ??? info "[InstrumentSettlementPeriod](/../../schemas/instrument_settlement_period)"
            |Value| Description |
            |-|-|
            |`PERPETUAL` = 1|Instrument settles through perpetual funding cycles|
            |`DAILY` = 2|Instrument settles at an expiry date, marked as a daily instrument|
            |`WEEKLY` = 3|Instrument settles at an expiry date, marked as a weekly instrument|
            |`MONTHLY` = 4|Instrument settles at an expiry date, marked as a monthly instrument|
            |`QUARTERLY` = 5|Instrument settles at an expiry date, marked as a quarterly instrument|
        ??? info "[AssetClass](/../../schemas/asset_class)"
            Asset class of an instrument's underlying. The first five values (crypto through index) are general classifications used by Perpetuals for display. The remaining values (equityNasdaq, equityNyse, etc.) are schedule-specific and used by SFPs to route to a trading schedule<br>

            |Value| Description |
            |-|-|
            |`CRYPTO` = 1|Digital assets (e.g. BTC, ETH)|
            |`EQUITY` = 2|Equities and equity-linked underlyings (e.g. stocks)|
            |`COMMODITY` = 3|Physical commodities (e.g. gold, oil)|
            |`FX` = 4|Foreign-exchange currency pairs|
            |`INDEX` = 5|Composite indices tracking a basket of underlyings|
            |`EQUITY_NASDAQ` = 6|NASDAQ-listed equities — maps to a TradingSchedule entry|
            |`EQUITY_NYSE` = 7|NYSE/NYSE Arca-listed equities and ETFs — maps to a TradingSchedule entry|
            |`EQUITY_KRX` = 8|Korea Exchange (KRX)-listed equities — maps to a TradingSchedule entry|
            |`COMMODITY_CME` = 9|CME-traded commodities — maps to a TradingSchedule entry|
            |`PRE_IPO` = 10|Pre-IPO instruments — maps to a TradingSchedule entry|
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
        ??? info "[DayOfWeek](/../../schemas/day_of_week)"
            Day of the week, used by recurring trading schedule sessions<br>

            |Value| Description |
            |-|-|
            |`MONDAY` = 1|Monday|
            |`TUESDAY` = 2|Tuesday|
            |`WEDNESDAY` = 3|Wednesday|
            |`THURSDAY` = 4|Thursday|
            |`FRIDAY` = 5|Friday|
            |`SATURDAY` = 6|Saturday|
            |`SUNDAY` = 7|Sunday|
