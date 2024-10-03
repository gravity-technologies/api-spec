!!! info "[Deposit](schemas/deposit.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |tx_hash<br>`th` |string|True|The hash of the bridgemint event producing the deposit|
    |to_account_id<br>`ta` |string|True|The account to deposit into|
    |currency<br>`c` |Currency|True|The token currency to deposit|
    |num_tokens<br>`nt` |string|True|The number of tokens to deposit|
    ??? info "[Currency](schemas/currency.md)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
