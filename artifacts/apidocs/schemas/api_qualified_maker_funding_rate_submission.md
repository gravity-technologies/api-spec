!!! info "[ApiQualifiedMakerFundingRateSubmission](/../../schemas/api_qualified_maker_funding_rate_submission)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |upload_id<br>`ui` |string|True|The upload ID: the accepted transaction's ID|
    |uploaded_at<br>`ua` |string|True|When the upload was accepted, unix nanoseconds|
    |rates<br>`r` |[QualifiedMakerFundingRateEntry]|True|The rates uploaded|
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
