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
