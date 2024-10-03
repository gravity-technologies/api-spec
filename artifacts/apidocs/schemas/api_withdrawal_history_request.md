!!! info "[ApiWithdrawalHistoryRequest](schemas/api_withdrawal_history_request.md)"
    The request to get the historical withdrawals of an account<br>The history is returned in reverse chronological order<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |currency<br>`c` |[Currency]|True|The token currency to query for, if nil or empty, return all withdrawals. Otherwise, only entries matching the filter will be returned|
    |start_time<br>`st` |string|False<br>`0`|The start time to query for in unix nanoseconds|
    |end_time<br>`et` |string|False<br>`now()`|The end time to query for in unix nanoseconds|
    |limit<br>`l` |number|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
    |cursor<br>`c1` |string|False<br>`''`|The cursor to indicate when to start the next query from|
    ??? info "[Currency](schemas/currency.md)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|