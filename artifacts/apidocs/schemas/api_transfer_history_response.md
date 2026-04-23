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
        |currency<br>`c` |string|True|The token currency to transfer|
        |num_tokens<br>`nt` |string|True|The number of tokens to transfer|
        |signature<br>`s` |Signature|True|The signature of the transfer|
        |event_time<br>`et` |string|True|The timestamp of the transfer in unix nanoseconds|
        |transfer_type<br>`tt` |TransferType|True|The type of transfer|
        |transfer_metadata<br>`tm` |string|True|The metadata of the transfer|
        |from_wallet_type<br>`fw` |WalletType|True|The wallet type of the from account or subaccount|
        |to_wallet_type<br>`tw` |WalletType|True|The wallet type of the to account or subaccount|
        ??? info "[Signature](/../../schemas/signature)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |signer<br>`s` |string|True|The address (public key) of the wallet signing the payload|
            |r<br>`r` |string|True|Signature R|
            |s<br>`s1` |string|True|Signature S|
            |v<br>`v` |integer|True|Signature V|
            |expiration<br>`e` |string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
            |nonce<br>`n` |integer|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.<br>Range: 0 to 4,294,967,295 (uint32)|
            |chain_id<br>`ci` |string|True|Chain ID used in EIP-712 domain. Zero value fallbacks to GRVT Chain ID.|
        ??? info "[TransferType](/../../schemas/transfer_type)"
            |Value| Description |
            |-|-|
            |`UNSPECIFIED` = 0|Deprecated: use `standard` instead. Legacy value for transfers created before transfer types were introduced.|
            |`STANDARD` = 1|Standard transfer that has nothing to do with bridging|
            |`FAST_ARB_DEPOSIT` = 2|Fast Arb Deposit Metadata type|
            |`FAST_ARB_WITHDRAWAL` = 3|Fast Arb Withdrawal Metadata type|
            |`NON_NATIVE_BRIDGE_DEPOSIT` = 4|Transfer type for non native bridging deposit|
            |`NON_NATIVE_BRIDGE_WITHDRAWAL` = 5|Transfer type for non native bridging withdrawal|
            |`ADHOC_INCENTIVE` = 6|Transfer type for adhoc incentive|
            |`REFERRAL_INCENTIVE` = 7|Transfer type for referral incentive|
            |`TRADING_DEPOSIT_YIELD_INCENTIVE` = 8|Transfer type for trading deposit yield incentive|
            |`TGE_VESTING` = 9|Transfer type for TGE vesting distribution|
            |`TGE_AIRDROP` = 10|Transfer type for TGE airdrop distribution|
        ??? info "[WalletType](/../../schemas/wallet_type)"
            |Value| Description |
            |-|-|
            |`FUNDING` = 1|Funding wallet|
            |`SPOT` = 2|Spot wallet|
            |`FUTURES` = 3|Futures wallet|
        ??? info "[WalletType](/../../schemas/wallet_type)"
            |Value| Description |
            |-|-|
            |`FUNDING` = 1|Funding wallet|
            |`SPOT` = 2|Spot wallet|
            |`FUTURES` = 3|Futures wallet|
