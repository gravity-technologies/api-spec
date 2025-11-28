!!! info "[ApiAddIsolatedPositionMarginRequest](/../../schemas/api_add_isolated_position_margin_request)"
    The request to add margin to a isolated position<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID to add isolated margin in or remove margin from|
    |instrument<br>`i` |string|True|The instrument to add margin into, or remove margin from|
    |amount<br>`a` |string|True|The amount of margin to add to the position, positive to add, negative to remove, expressed in quote asset decimal units|
    |signature<br>`s` |Signature|True|The signature of this operation|
    ??? info "[Signature](/../../schemas/signature)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |signer<br>`s` |string|True|The address (public key) of the wallet signing the payload|
        |r<br>`r` |string|True|Signature R|
        |s<br>`s1` |string|True|Signature S|
        |v<br>`v` |integer|True|Signature V|
        |expiration<br>`e` |string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
        |nonce<br>`n` |integer|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|
        |chain_id<br>`ci` |string|True|Chain ID used in EIP-712 domain. Zero value fallbacks to GRVT Chain ID.|
