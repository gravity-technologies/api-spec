!!! info "[ApiSetSubAccountCollateralPreferenceRequest](/../../schemas/api_set_sub_account_collateral_preference_request)"
    Enable or disable one or more currencies as collateral for a Multi-Asset Mode sub account.<br><br>USDT (the quote currency) cannot be disabled. Disabling collateral currencies reduces MarginBalance, and the batch is rejected when Initial Margin would no longer be covered.<br><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID to set collateral preferences for|
    |preferences<br>`p` |[ApiCollateralPreferenceItem]|True|Per-currency preferences applied atomically. Duplicate currencies and empty lists are rejected.|
    |signature<br>`s` |Signature|True|The signature of this operation|
    ??? info "[ApiCollateralPreferenceItem](/../../schemas/api_collateral_preference_item)"
        A single (currency, enable) pair to toggle as collateral.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |currency<br>`c` |string|True|The currency whose collateral preference is being changed|
        |enable<br>`e` |boolean|True|True to include the currency as collateral, false to exclude it|
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
