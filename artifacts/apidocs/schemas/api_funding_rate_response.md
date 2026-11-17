!!! info "[ApiFundingRateResponse](/../../schemas/api_funding_rate_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |[ApiFundingRate]|True|The funding rate result set for given interval|
    |next<br>`n` |string|False<br>`''`|The cursor to indicate when to start the next query from|
    ??? info "[ApiFundingRate](/../../schemas/api_funding_rate)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |funding_rate<br>`fr` |string|False<br>`None`|The funding rate of the instrument, expressed in percentage points. Absent for stable perps, which have `funding_rate_long_apr_pct` and `funding_rate_short_apr_pct` instead.|
        |funding_time<br>`ft` |string|True|The funding timestamp of the funding rate, expressed in unix nanoseconds|
        |mark_price<br>`mp` |string|True|The mark price of the instrument at funding timestamp, expressed in `9` decimals. For stable perps, the index price the charge used.|
        |funding_rate_8_h_avg<br>`fr1` |string|False<br>`None`|Deprecated: Refer to `funding_rate` instead. Will be removed in a future release. Absent for stable perps.|
        |funding_interval_hours<br>`fi` |integer|True|Funding interval in hours (e.g. 1/4/8/etc).|
        |funding_rate_long_apr_pct<br>`fr2` |string|False<br>`None`|Stable perps only: the annual rate for retail longs at this charge, in percent a year (`'-5.5'` = retail longs paid 5.5%; positive = retail receives, negative = retail pays). Absent for other kinds.|
        |funding_rate_short_apr_pct<br>`fr3` |string|False<br>`None`|Stable perps only: the annual rate for retail shorts at this charge, in percent a year (`'-5'` = retail shorts paid 5%; positive = retail receives, negative = retail pays). Absent for other kinds.|
        |funding_multiplier<br>`fm` |integer|False<br>`None`|Stable perps only: days of funding the charge covered, 3 on the triple day, else 1. Absent for other kinds.|
