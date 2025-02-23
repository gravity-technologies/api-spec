!!! info "[ApiOrderHistoryRequest](/../../schemas/api_order_history_request)"
    Retrieves the order history for the account.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |kind<br>`k` |[Kind]|False<br>`all`|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
    |base<br>`b` |[Currency]|False<br>`all`|The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned|
    |quote<br>`q` |[Currency]|False<br>`all`|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
    |start_time<br>`st` |string|False<br>`0`|The start time to apply in nanoseconds. If nil, this defaults to all start times. Otherwise, only entries matching the filter will be returned|
    |end_time<br>`et` |string|False<br>`now()`|The end time to apply in nanoseconds. If nil, this defaults to all end times. Otherwise, only entries matching the filter will be returned|
    |limit<br>`l` |integer|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
    |cursor<br>`c` |string|False<br>`''`|The cursor to indicate when to start the query from|
    ??? info "[Kind](/../../schemas/kind)"
        The list of asset kinds that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`PERPETUAL` = 1|the perpetual asset kind|
        |`FUTURE` = 2|the future asset kind|
        |`CALL` = 3|the call option asset kind|
        |`PUT` = 4|the put option asset kind|
    ??? info "[Currency](/../../schemas/currency)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
        |`SOL` = 6|the SOL token|
        |`ARB` = 7|the ARB token|
        |`BNB` = 8|the BNB token|
        |`ZK` = 9|the ZK token|
        |`POL` = 10|the POL token|
        |`OP` = 11|the OP token|
        |`ATOM` = 12|the ATOM token|
        |`KPEPE` = 13|the 1000PEPE token|
        |`TON` = 14|the TON token|
        |`XRP` = 15|the XRP token|
        |`XLM` = 16|the XLM token|
        |`WLD` = 17|the WLD token|
        |`WIF` = 18|the WIF token|
        |`VIRTUAL` = 19|the VIRTUAL token|
        |`TRUMP` = 20|the TRUMP token|
        |`SUI` = 21|the SUI token|
        |`KSHIB` = 22|the 1000SHIB token|
        |`POPCAT` = 23|the POPCAT token|
        |`PENGU` = 24|the PENGU token|
        |`LINK` = 25|the LINK token|
        |`KBONK` = 26|the 1000BONK token|
        |`JUP` = 27|the JUP token|
        |`FARTCOIN` = 28|the FARTCOIN token|
        |`ENA` = 29|the ENA token|
        |`DOGE` = 30|the DOGE token|
        |`AIXBT` = 31|the AIXBT token|
        |`AI_16_Z` = 32|the AI16Z token|
        |`ADA` = 33|the ADA token|
        |`AAVE` = 34|the AAVE token|
        |`BERA` = 35|the BERA token|
        |`VINE` = 36|the VINE token|
        |`PENDLE` = 37|the PENDLE token|
        |`UXLINK` = 38|the UXLINK token|
    ??? info "[Currency](/../../schemas/currency)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
        |`SOL` = 6|the SOL token|
        |`ARB` = 7|the ARB token|
        |`BNB` = 8|the BNB token|
        |`ZK` = 9|the ZK token|
        |`POL` = 10|the POL token|
        |`OP` = 11|the OP token|
        |`ATOM` = 12|the ATOM token|
        |`KPEPE` = 13|the 1000PEPE token|
        |`TON` = 14|the TON token|
        |`XRP` = 15|the XRP token|
        |`XLM` = 16|the XLM token|
        |`WLD` = 17|the WLD token|
        |`WIF` = 18|the WIF token|
        |`VIRTUAL` = 19|the VIRTUAL token|
        |`TRUMP` = 20|the TRUMP token|
        |`SUI` = 21|the SUI token|
        |`KSHIB` = 22|the 1000SHIB token|
        |`POPCAT` = 23|the POPCAT token|
        |`PENGU` = 24|the PENGU token|
        |`LINK` = 25|the LINK token|
        |`KBONK` = 26|the 1000BONK token|
        |`JUP` = 27|the JUP token|
        |`FARTCOIN` = 28|the FARTCOIN token|
        |`ENA` = 29|the ENA token|
        |`DOGE` = 30|the DOGE token|
        |`AIXBT` = 31|the AIXBT token|
        |`AI_16_Z` = 32|the AI16Z token|
        |`ADA` = 33|the ADA token|
        |`AAVE` = 34|the AAVE token|
        |`BERA` = 35|the BERA token|
        |`VINE` = 36|the VINE token|
        |`PENDLE` = 37|the PENDLE token|
        |`UXLINK` = 38|the UXLINK token|
