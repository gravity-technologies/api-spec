!!! info "[DepositHistory](schemas/deposit_history.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |tx_id<br>`ti` |string|True|The transaction ID of the deposit|
    |tx_hash<br>`th` |string|True|The txHash of the bridgemint event|
    |to_account_id<br>`ta` |string|True|The account to deposit into|
    |currency<br>`c` |Currency|True|The token currency to deposit|
    |num_tokens<br>`nt` |string|True|The number of tokens to deposit|
    |event_time<br>`et` |string|True|The timestamp of the deposit in unix nanoseconds|
    ??? info "[Currency](schemas/currency.md)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|