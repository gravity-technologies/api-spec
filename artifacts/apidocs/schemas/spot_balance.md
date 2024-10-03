!!! info "[SpotBalance](/../../schemas/spot_balance)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |currency<br>`c` |Currency|True|The currency you hold a spot balance in|
    |balance<br>`b` |string|True|This currency's balance in this trading account.|
    |index_price<br>`ip` |string|True|The index price of this currency. (reported in `USD`)|
    ??? info "[Currency](/../../schemas/currency)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
