!!! info "[ApiFundingAccountSummaryResponse](/../../schemas/api_funding_account_summary_response)"
    The funding account summary, that reports the total equity and spot balances of a funding (main) account<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |FundingAccountSummary|True|The funding account summary|
    |tier<br>`t` |ClientTier|True|Client fee tier at the time of query|
    ??? info "[FundingAccountSummary](/../../schemas/funding_account_summary)"
        The funding account summary, that reports the total equity and spot balances of a funding (main) account<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |main_account_id<br>`ma` |string|True|The main account ID of the account to which the summary belongs|
        |total_equity<br>`te` |string|True|Total equity of the main account, denominated in USD|
        |spot_balances<br>`sb` |[SpotBalance]|True|The list of spot assets owned by this main account, and their balances|
        ??? info "[SpotBalance](/../../schemas/spot_balance)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |currency<br>`c` |string|True|The currency you hold a spot balance in|
            |balance<br>`b` |string|True|This currency's balance in this trading account.|
            |index_price<br>`ip` |string|True|The index price of this currency. (reported in `USD`)|
    ??? info "[ClientTier](/../../schemas/client_tier)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |tier<br>`t` |integer|True||
        |futures_taker_fee<br>`ft` |integer|True||
        |futures_maker_fee<br>`fm` |integer|True||
        |options_taker_fee<br>`ot` |integer|True||
        |options_maker_fee<br>`om` |integer|True||
