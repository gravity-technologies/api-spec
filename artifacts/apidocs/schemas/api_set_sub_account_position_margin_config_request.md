!!! info "[ApiSetSubAccountPositionMarginConfigRequest](/../../schemas/api_set_sub_account_position_margin_config_request)"
    Sets the margin type and leverage configuration for a specific position (instrument) within a sub account.<br><br>This configuration is applied per-instrument, allowing different margin settings for different positions.<br><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID to set the margin type and leverage for|
    |instrument<br>`i` |string|True|The instrument of the position to set the margin type and leverage for|
    |margin_type<br>`mt` |PositionMarginType|True|The margin type to set for the position|
    |leverage<br>`l` |string|True|The leverage to set for the position|
    |signature<br>`s` |Signature|True|The signature of this operation|
    ??? info "[PositionMarginType](/../../schemas/position_margin_type)"
        |Value| Description |
        |-|-|
        |`CROSS` = 2|Cross Margin Mode: uses all available funds in your account as collateral across all cross margin positions|
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
