!!! info "[DepositHistory](/../../schemas/deposit_history)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |l_1_hash<br>`l1` |string|True|The L1 txHash of the deposit|
    |l_2_hash<br>`l2` |string|True|The L2 txHash of the deposit|
    |to_account_id<br>`ta` |string|True|The account to deposit into|
    |currency<br>`c` |Currency|True|The token currency to deposit|
    |num_tokens<br>`nt` |string|True|The number of tokens to deposit|
    |initiated_time<br>`it` |string|True|The timestamp when the deposit was initiated on L1 in unix nanoseconds|
    |confirmed_time<br>`ct` |string|True|The timestamp when the deposit was confirmed on L2 in unix nanoseconds|
    |from_address<br>`fa` |string|True|The address of the sender|
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
        |`LINK` = 25|the LINK token|
        |`JUP` = 27|the JUP token|
        |`FARTCOIN` = 28|the FARTCOIN token|
        |`ENA` = 29|the ENA token|
        |`DOGE` = 30|the DOGE token|
        |`ADA` = 33|the ADA token|
        |`AAVE` = 34|the AAVE token|
        |`BERA` = 35|the BERA token|
        |`IP` = 40|the IP token|
