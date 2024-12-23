!!! info "[ApiPreDepositCheckResponse](/../../schemas/api_pre_deposit_check_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |max_deposit_limit<br>`md` |string|True|Max Deposit Limit reported for the Bridge Account reported in the currency balance|
    |currency<br>`c` |Currency|True|The currency you hold the deposit in|
    ??? info "[Currency](/../../schemas/currency)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
