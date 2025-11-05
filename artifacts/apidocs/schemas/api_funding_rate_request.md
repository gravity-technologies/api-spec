!!! info "[ApiFundingRateRequest](/../../schemas/api_funding_rate_request)"
    Lookup the historical funding rate of a perpetual future.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
    |start_time<br>`st` |string|False<br>`0`|Start time of funding rate in unix nanoseconds|
    |end_time<br>`et` |string|False<br>`now()`|End time of funding rate in unix nanoseconds|
    |limit<br>`l` |integer|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
    |cursor<br>`c` |string|False<br>`''`|The cursor to indicate when to start the query from|
    |agg_type<br>`at` |FundingRateAggregationType|False<br>`'FUNDING_INTERVAL'`|Aggregation method for historical funding rate observations. Defaults to using the instrument-specific funding interval.|
    ??? info "[FundingRateAggregationType](/../../schemas/funding_rate_aggregation_type)"
        Specifies different methods of aggregating historical funding rates<br>

        |Value| Description |
        |-|-|
        |`FUNDING_INTERVAL` = 1|Default value -- one record returned per funding interval. Query instruments endpoint to learn funding interval of each instrument.|
        |`ONE_HOURLY` = 2|Returns one record per hour -- normalizes all funding rates to 1h durations, so `fundingRate`  value is cumulative and can exceed a funding interval's configured cap / floor.|
        |`FOUR_HOURLY` = 3|Returns one record per 4 hours -- normalizes all funding rates to 4h durations, so `fundingRate`  value is cumulative and can exceed a funding interval's configured cap / floor.|
        |`EIGHT_HOURLY` = 4|Returns one record for eight hours -- normalizes all funding rates to 8h durations, so `fundingRate`  value is cumulative and can exceed a funding interval's configured cap / floor.|
