!!! info "[PreOrderCheckResult](/../../schemas/pre_order_check_result)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |max_qty<br>`mq` |[AssetMaxQty]|True|The maximum quantity for each leg|
    |margin_required<br>`mr` |string|True|The margin required for the order (reported in `settle_currency`)|
    |order_valid<br>`ov` |boolean|True|Whether the order is valid|
    |reason<br>`r` |string|True|The reason the order is invalid, if any|
    |settle_currency<br>`sc` |Currency|True|The subAccount settle currency|
    ??? info "[AssetMaxQty](/../../schemas/asset_max_qty)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |asset<br>`a` |string|True|The asset associated with the max quantity|
        |max_buy_qty<br>`mb` |string|True|The maximum buy quantity|
        |max_sell_qty<br>`ms` |string|True|The maximum sell quantity|
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
