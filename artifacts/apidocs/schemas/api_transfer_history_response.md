!!! info "[ApiTransferHistoryResponse](/../../schemas/api_transfer_history_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |[TransferHistory]|True|The transfer history matching the request account|
    |next<br>`n` |string|False<br>`''`|The cursor to indicate when to start the next query from|
    ??? info "[TransferHistory](/../../schemas/transfer_history)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |tx_id<br>`ti` |string|True|The transaction ID of the transfer|
        |from_account_id<br>`fa` |string|True|The account to transfer from|
        |from_sub_account_id<br>`fs` |string|True|The subaccount to transfer from (0 if transferring from main account)|
        |to_account_id<br>`ta` |string|True|The account to deposit into|
        |to_sub_account_id<br>`ts` |string|True|The subaccount to transfer to (0 if transferring to main account)|
        |currency<br>`c` |Currency|True|The token currency to transfer|
        |num_tokens<br>`nt` |string|True|The number of tokens to transfer|
        |signature<br>`s` |Signature|True|The signature of the transfer|
        |event_time<br>`et` |string|True|The timestamp of the transfer in unix nanoseconds|
        |transfer_type<br>`tt` |TransferType|True|The type of transfer|
        |transfer_metadata<br>`tm` |string|True|The metadata of the transfer|
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
            |`XLM` = 16|the XLM token|
            |`WLD` = 17|the WLD token|
            |`WIF` = 18|the WIF token|
            |`VIRTUAL` = 19|the VIRTUAL token|
            |`TRUMP` = 20|the TRUMP token|
            |`SUI` = 21|the SUI token|
            |`KSHIB` = 22|the 1000SHIB token|
            |`POPCAT` = 23|the POPCAT token|
            |`PENGU` = 24|the PENGU token|
            |`LINK` = 25|the LINK token|
            |`KBONK` = 26|the 1000BONK token|
            |`JUP` = 27|the JUP token|
            |`FARTCOIN` = 28|the FARTCOIN token|
            |`ENA` = 29|the ENA token|
            |`DOGE` = 30|the DOGE token|
            |`AIXBT` = 31|the AIXBT token|
            |`AI_16_Z` = 32|the AI16Z token|
            |`ADA` = 33|the ADA token|
            |`AAVE` = 34|the AAVE token|
            |`BERA` = 35|the BERA token|
            |`VINE` = 36|the VINE token|
            |`PENDLE` = 37|the PENDLE token|
            |`UXLINK` = 38|the UXLINK token|
        ??? info "[Signature](/../../schemas/signature)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |signer<br>`s` |string|True|The address (public key) of the wallet signing the payload|
            |r<br>`r` |string|True|Signature R|
            |s<br>`s1` |string|True|Signature S|
            |v<br>`v` |integer|True|Signature V|
            |expiration<br>`e` |string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
            |nonce<br>`n` |integer|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
        ??? info "[TransferType](/../../schemas/transfer_type)"
            |Value| Description |
            |-|-|
            |`STANDARD` = 1|Standard transfer that has nothing to do with bridging|
            |`FAST_ARB_DEPOSIT` = 2|Fast Arb Deposit Metadata type|
            |`FAST_ARB_WITHDRAWAL` = 3|Fast Arb Withdrawal Metadata type|
