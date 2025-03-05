!!! info "[Deposit](/../../schemas/deposit)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |tx_hash<br>`th` |string|True|The hash of the bridgemint event producing the deposit|
    |to_account_id<br>`ta` |string|True|The account to deposit into|
    |currency<br>`c` |Currency|True|The token currency to deposit|
    |num_tokens<br>`nt` |string|True|The number of tokens to deposit|
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
        |`TRUMP` = 20|the TRUMP token|
        |`SUI` = 21|the SUI token|
        |`FARTCOIN` = 28|the FARTCOIN token|
        |`BERA` = 35|the BERA token|
        |`KAITO` = 39|the KAITO token|
