!!! info "[ApiQualifiedMakerEffectiveRateHistoryRequest](/../../schemas/api_qualified_maker_effective_rate_history_request)"
    Query the rates the caller's qualified maker main account was settled at, one row per (charge, instrument). Paginated like funding_payment_history: reverse chronological from `end_time`, `limit` rows per page, `next` cursor.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |instrument<br>`i` |string|False<br>`all`|The instrument to filter for|
    |start_time<br>`st` |string|False<br>`0`|The start time in unix nanoseconds|
    |end_time<br>`et` |string|False<br>`now()`|The end time in unix nanoseconds|
    |limit<br>`l` |integer|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
    |cursor<br>`c` |string|False<br>`''`|The cursor to indicate when to start the query from|
