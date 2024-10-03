!!! info "[WSDepositFeedDataV1](schemas/ws_deposit_feed_data_v1.md)"
    Subscribes to a feed of deposit updates.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|The websocket channel to which the response is sent|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
    |feed<br>`f` |Deposit|True|The Deposit object|
    ??? info "[Deposit](schemas/deposit.md)"
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
