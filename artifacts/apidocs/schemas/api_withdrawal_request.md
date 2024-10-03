!!! info "[ApiWithdrawalRequest](schemas/api_withdrawal_request.md)"
    Leverage this API to initialize a withdrawal from GRVT's Hyperchain onto Ethereum.<br>Do take note that the bridging process does take time. The GRVT UI will help you keep track of bridging progress, and notify you once its complete.<br><br>If not withdrawing the entirety of your balance, there is a minimum withdrawal amount. Currently that amount is ~25 USDT.<br>Withdrawal fees also apply to cover the cost of the Ethereum transaction.<br>Note that your funds will always remain in self-custory throughout the withdrawal process. At no stage does GRVT gain control over your funds.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |from_account_id<br>`fa` |string|True|The main account to withdraw from|
    |to_eth_address<br>`te` |string|True|The Ethereum wallet to withdraw into|
    |currency<br>`c` |Currency|True|The token currency to withdraw|
    |num_tokens<br>`nt` |string|True|The number of tokens to withdraw, quoted in tokenCurrency decimal units|
    |signature<br>`s` |Signature|True|The signature of the withdrawal|
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
