!!! info "[ApiAuthorizeBuilderRequest](/../../schemas/api_authorize_builder_request)"
    Authorizes a specific Builder to execute transactions on behalf of the Main Account.<br><br>This endpoint acts as an **upsert** operation:<br>- **New Authorization**: If the builder is not currently authorized, a new record is created.<br>- **Update Limit**: If the builder is already authorized, this request updates the `maxFuturesFeeRate` and `maxSpotFeeRate` to the new values provided.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |main_account_id<br>`ma` |string|True|The Main Account ID of the user granting the authorization.|
    |builder_account_id<br>`ba` |string|True|The Main Account ID of the Builder receiving the authorization.|
    |max_futures_fee_rate<br>`mf` |string|True|The maximum fee rate cap for **Futures** trades executed by this builder. The builder cannot charge fees exceeding this limit.|
    |max_spot_fee_rate<br>`ms` |string|True|The maximum fee rate cap for **Spot** trades executed by this builder. The builder cannot charge fees exceeding this limit.|
    |signature<br>`s` |Signature|True|The cryptographic signature authenticating this request. Must be signed by the private key associated with `mainAccountID`.|
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
