!!! info "[ApiSetSubAccountModeRequest](/../../schemas/api_set_sub_account_mode_request)"
    Sets the sub account mode (Single Asset Mode or Multi Asset Mode).<br><br>Switching modes requires passing validation checks to ensure the account remains healthy.<br><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID to set the mode for|
    |sub_account_mode<br>`sa1` |SubAccountMode|True|The target sub account mode to switch to|
    |signature<br>`s` |Signature|True|The signature of this operation|
    ??? info "[SubAccountMode](/../../schemas/sub_account_mode)"
        |Value| Description |
        |-|-|
        |`SINGLE_ASSET_MODE` = 1|Single asset mode: the subaccount is only allowed to hold one asset as collateral|
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
