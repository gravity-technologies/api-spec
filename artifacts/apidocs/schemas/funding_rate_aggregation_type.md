!!! info "[FundingRateAggregationType](/../../schemas/funding_rate_aggregation_type)"
    Specifies different methods of aggregating historical funding rates<br>

    |Value| Description |
    |-|-|
    |`FUNDING_INTERVAL` = 1|Default value -- one record returned per funding interval. Query instruments endpoint to learn funding interval of each instrument.|
    |`ONE_HOURLY` = 2|Returns one record per hour -- normalizes all funding rates to 1h durations, so `fundingRate`  value is cumulative and can exceed a funding interval's configured cap / floor.|
    |`FOUR_HOURLY` = 3|Returns one record per 4 hours -- normalizes all funding rates to 4h durations, so `fundingRate`  value is cumulative and can exceed a funding interval's configured cap / floor.|
    |`EIGHT_HOURLY` = 4|Returns one record for eight hours -- normalizes all funding rates to 8h durations, so `fundingRate`  value is cumulative and can exceed a funding interval's configured cap / floor.|
