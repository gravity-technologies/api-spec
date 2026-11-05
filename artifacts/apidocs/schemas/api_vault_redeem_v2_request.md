!!! info "[ApiVaultRedeemV2Request](/../../schemas/api_vault_redeem_v2_request)"
    Request payload for redeeming from a vault, paid in the vault's investment currency or converted into another currency.<br><br>The investor signs `VaultRedeemV3` over both currencies, the number of shares and the exchange rate. The request keeps the signed rate and is paid at it, at the share price of the payout.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |vault_id<br>`vi` |string|True|The unique identifier of the vault to redeem from.|
    |from_currency<br>`fc` |string|True|The currency the vault pays. This must be the vault's investment currency.|
    |to_currency<br>`tc` |string|True|The currency paid into the funding account: the investment currency, or another currency converted at `exchangeRate`.|
    |num_tokens<br>`nt` |string|True|The number of shares to redeem.|
    |exchange_rate<br>`er` |string|True|The signed rate, `toCurrency` per unit of `fromCurrency`, up to 9 decimal places. Exactly 1 when both currencies are the same.|
    |signature<br>`s` |Signature|True|The `VaultRedeemV3` signature of the redeeming account.<br>The signer needs the vault investor permission on the main account.|
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
