!!! info "[WSWithdrawalFeedDataV1](/../../schemas/ws_withdrawal_feed_data_v1)"
    Subscribes to a feed of withdrawal updates.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|The websocket channel to which the response is sent|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A sequence number used to determine message order within a stream.<br>- If `useGlobalSequenceNumber` is **false**, this returns the gateway sequence number, which increments by one locally within each stream and resets on gateway restarts.<br>- If `useGlobalSequenceNumber` is **true**, this returns the global sequence number, which uniquely identifies messages across the cluster.<br>  - A single cluster payload can be multiplexed into multiple stream payloads.<br>  - To distinguish each stream payload, a `dedupCounter` is included.<br>  - The returned sequence number is computed as: `cluster_sequence_number * 10^5 + dedupCounter`.|
    |feed<br>`f` |Withdrawal|True|The Withdrawal object|
    ??? info "[Withdrawal](/../../schemas/withdrawal)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |from_account_id<br>`fa` |string|True|The subaccount to withdraw from|
        |to_eth_address<br>`te` |string|True|The ethereum address to withdraw to|
        |currency<br>`c` |Currency|True|The token currency to withdraw|
        |num_tokens<br>`nt` |string|True|The number of tokens to withdraw|
        |signature<br>`s` |Signature|True|The signature of the withdrawal|
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
        ??? info "[Signature](/../../schemas/signature)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |signer<br>`s` |string|True|The address (public key) of the wallet signing the payload|
            |r<br>`r` |string|True|Signature R|
            |s<br>`s1` |string|True|Signature S|
            |v<br>`v` |integer|True|Signature V|
            |expiration<br>`e` |string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
            |nonce<br>`n` |integer|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
