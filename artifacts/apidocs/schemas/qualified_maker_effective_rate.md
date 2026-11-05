!!! info "[QualifiedMakerEffectiveRate](/../../schemas/qualified_maker_effective_rate)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |event_time<br>`et` |string|True|The charge (funding) time in unix nanoseconds|
    |main_account_id<br>`ma` |string|True|The qualified maker main account|
    |instrument<br>`i` |string|True|The stable perp|
    |mode<br>`m` |SfpFundingMode|True|The mode the qualified maker uploaded in; the record carries only that mode's pair of rate fields|
    |long_rate_apr_pct<br>`lr` |string|False<br>`0`|ANNUAL_PCT_OF_CURRENT_PRICE only: the qualified maker's long rate used, in percent a year ("-4.5" = retail longs pay 4.5%); positive = retail receives, negative = retail pays|
    |short_rate_apr_pct<br>`sr` |string|False<br>`0`|ANNUAL_PCT_OF_CURRENT_PRICE only: the qualified maker's short rate used, in percent a year; positive = retail receives, negative = retail pays|
    |long_rate_cash_per_unit<br>`lr1` |string|False<br>`0`|DAILY_CASH_PER_UNIT only: the qualified maker's long rate used, in quote currency per unit per day; positive = retail receives, negative = retail pays|
    |short_rate_cash_per_unit<br>`sr1` |string|False<br>`0`|DAILY_CASH_PER_UNIT only: the qualified maker's short rate used, in quote currency per unit per day; positive = retail receives, negative = retail pays|
    |upload_id<br>`ui` |string|True|The upload this rate comes from|
    |uploaded_at<br>`ua` |string|True|When that upload was accepted, unix nanoseconds|
    |carried_forward<br>`cf` |boolean|True|True if the qualified maker did not upload since the previous charge and its last rate was reused|
    |tx_id<br>`ti` |string|True|The funding tick transaction ID|
    |funding_sub_account_id<br>`fs` |string|True|The sub-account the netted payment was booked on: the sfpFundingSubAccount config, else the main account's non-vault sub-account with the largest total equity. 0 when the charge paid nothing|
    |net_position<br>`np` |string|True|The qualified maker's position netted across all sub-accounts of its main account, in base units (negative = short). Net short is settled at its long rate, net long at its short rate|
    |index_price<br>`ip` |string|True|The index price the charge used, expressed in `9` decimals|
    |multiplier<br>`m1` |integer|True|Days of funding the charge covered: 3 on the triple swap day, else 1|
    |amount<br>`a` |string|True|The netted funding payment in the quote currency, as on the funding sub-account's funding payment: negative = the qualified maker received it, positive = it paid. 0 when the charge paid nothing|
    ??? info "[SfpFundingMode](/../../schemas/sfp_funding_mode)"
        |Value| Description |
        |-|-|
        |`UNSPECIFIED` = 0||
        |`ANNUAL_PCT_OF_CURRENT_PRICE` = 1|Rate is an annual percentage of notional, as a fraction with 9 decimals: 4.5% = 45000000|
        |`DAILY_CASH_PER_UNIT` = 2|Rate is quote currency per unit per day, with 9 decimals: 0.25 USDC = 250000000|
