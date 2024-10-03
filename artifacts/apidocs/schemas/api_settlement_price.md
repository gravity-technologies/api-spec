!!! info "[APISettlementPrice](schemas/api_settlement_price.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |base<br>`b` |Currency|True|The base currency of the settlement price|
    |quote<br>`q` |Currency|True|The quote currency of the settlement price|
    |settlement_time<br>`st` |string|True|The settlement timestamp of the settlement price, expressed in unix nanoseconds|
    |settlement_price<br>`sp` |string|True|The settlement price, expressed in `9` decimals|
    ??? info "[Currency](schemas/currency.md)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
    ??? info "[Currency](schemas/currency.md)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
