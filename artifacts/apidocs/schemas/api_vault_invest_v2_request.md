!!! info "[ApiVaultInvestV2Request](/../../schemas/api_vault_invest_v2_request)"
    Request payload for investing in a vault from the funding account or from a trading account, converting the source currency into the vault's investment currency when they differ.<br><br>The investor signs `VaultInvestV3` over both currencies, the amount and the exchange rate. Without conversion the rate is exactly 1. With conversion it must be at most the rate `/vault_conversion_rate` returns.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |vault_id<br>`vi` |string|True|The unique identifier of the vault to invest in.|
    |from_sub_account_id<br>`fs` |string|True|The trading account to invest from. 0 means the funding account.|
    |from_currency<br>`fc` |string|True|The currency debited from the source wallet.|
    |from_num_tokens<br>`fn` |string|True|The amount debited from the source wallet, in `fromCurrency`.|
    |to_currency<br>`tc` |string|True|The currency the vault receives. This must be the vault's investment currency.|
    |exchange_rate<br>`er` |string|True|The signed rate, `toCurrency` per unit of `fromCurrency`, up to 9 decimal places. Exactly 1 when both currencies are the same.|
    |signature<br>`s` |Signature|True|The `VaultInvestV3` signature of the investing account.<br>The signer needs the vault investor permission on the main account and, for a trading account source, the transfer permission on that trading account.|
    ??? info "[WalletType](/../../schemas/wallet_type)"
        |Value| Description |
        |-|-|
        |`FUNDING` = 1|Funding wallet|
        |`SPOT` = 2|Spot wallet|
        |`FUTURES` = 3|Futures wallet|
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
