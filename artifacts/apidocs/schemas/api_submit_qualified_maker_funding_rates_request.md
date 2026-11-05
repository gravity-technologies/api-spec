!!! info "[ApiSubmitQualifiedMakerFundingRatesRequest](/../../schemas/api_submit_qualified_maker_funding_rates_request)"
    Submits a qualified maker's long and short funding rates for stable perps. Each entry applies from the instrument's next charge. Only qualified makers can submit.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |rates<br>`r` |[QualifiedMakerFundingRateEntry]|True|One entry per instrument; the request is accepted or rejected as a whole|
    |signature<br>`s` |Signature|True|The EIP-712 signature over rates|
    ??? info "[QualifiedMakerFundingRateEntry](/../../schemas/qualified_maker_funding_rate_entry)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|A listed stable perp|
        |mode<br>`m` |SfpFundingMode|True|Either funding mode; the entry carries only that mode's pair of rate fields|
        |long_rate_apr_pct<br>`lr` |string|False<br>`0`|ANNUAL_PCT_OF_CURRENT_PRICE only: the long rate in percent a year, up to 6 decimals ("-4.5" = retail longs pay 4.5%); positive = retail receives, negative = retail pays|
        |short_rate_apr_pct<br>`sr` |string|False<br>`0`|ANNUAL_PCT_OF_CURRENT_PRICE only: the short rate in percent a year, up to 6 decimals; positive = retail receives, negative = retail pays|
        |long_rate_cash_per_unit<br>`lr1` |string|False<br>`0`|DAILY_CASH_PER_UNIT only: the long rate in quote currency per unit per day, up to 6 decimals; positive = retail receives, negative = retail pays|
        |short_rate_cash_per_unit<br>`sr1` |string|False<br>`0`|DAILY_CASH_PER_UNIT only: the short rate in quote currency per unit per day, up to 6 decimals; positive = retail receives, negative = retail pays|
        ??? info "[SfpFundingMode](/../../schemas/sfp_funding_mode)"
            |Value| Description |
            |-|-|
            |`UNSPECIFIED` = 0||
            |`ANNUAL_PCT_OF_CURRENT_PRICE` = 1|Rate is an annual percentage of notional, as a fraction with 9 decimals: 4.5% = 45000000|
            |`DAILY_CASH_PER_UNIT` = 2|Rate is quote currency per unit per day, with 9 decimals: 0.25 USDC = 250000000|
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
