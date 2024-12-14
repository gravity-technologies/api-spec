!!! info "[ApiPreDepositCheckRequest](/../../schemas/api_pre_deposit_check_request)"
    UI only for bridge deposits through non native bridge. Currently only supports XY Finance bridge account.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |currency<br>`c` |Currency|True|The currency you hold the deposit in|
    |bridge<br>`b` |BridgeType|True|The bridge type to conduct checks for|
    ??? info "[Currency](/../../schemas/currency)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
    ??? info "[BridgeType](/../../schemas/bridge_type)"
        |Value| Description |
        |-|-|
        |`XY` = 1|XY Bridge type|
