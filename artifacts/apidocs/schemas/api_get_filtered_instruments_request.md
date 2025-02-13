!!! info "[ApiGetFilteredInstrumentsRequest](/../../schemas/api_get_filtered_instruments_request)"
    Fetch a list of instruments based on the filters provided<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |kind<br>`k` |[Kind]|False<br>`all`|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
    |base<br>`b` |[Currency]|False<br>`all`|The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned|
    |quote<br>`q` |[Currency]|False<br>`all`|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
    |is_active<br>`ia` |boolean|False<br>`false`|Request for active instruments only|
    |limit<br>`l` |integer|False<br>`500`|The limit to query for. Defaults to 500; Max 100000|
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
