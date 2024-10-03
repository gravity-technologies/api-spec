!!! info "[ApiTransferRequest](schemas/api_transfer_request.md)"
    This API allows you to transfer funds in multiple different ways<ul><br><li>Between SubAccounts within your Main Account</li><br><li>Between your MainAccount and your SubAccounts</li><br><li>To other MainAccounts that you have previously allowlisted</li><br></ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |from_account_id<br>`fa` |string|True|The main account to transfer from|
    |from_sub_account_id<br>`fs` |string|True|The subaccount to transfer from (0 if transferring from main account)|
    |to_account_id<br>`ta` |string|True|The main account to deposit into|
    |to_sub_account_id<br>`ts` |string|True|The subaccount to transfer to (0 if transferring to main account)|
    |currency<br>`c` |Currency|True|The token currency to transfer|
    |num_tokens<br>`nt` |string|True|The number of tokens to transfer, quoted in tokenCurrency decimal units|
    |signature<br>`s` |Signature|True|The signature of the transfer|
    ??? info "[Currency](schemas/currency.md)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
    ??? info "[Signature](schemas/signature.md)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |signer<br>`s` |string|True|The address (public key) of the wallet signing the payload|
        |r<br>`r` |string|True|Signature R|
        |s<br>`s1` |string|True|Signature S|
        |v<br>`v` |number|True|Signature V|
        |expiration<br>`e` |string|True|Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days|
        |nonce<br>`n` |number|True|Users can randomly generate this value, used as a signature deconflicting key.<br>ie. You can send the same exact instruction twice with different nonces.<br>When the same nonce is used, the same payload will generate the same signature.<br>Our system will consider the payload a duplicate, and ignore it.|