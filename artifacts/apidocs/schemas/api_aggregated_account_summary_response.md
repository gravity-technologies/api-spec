!!! info "[ApiAggregatedAccountSummaryResponse](/../../schemas/api_aggregated_account_summary_response)"
    The aggregated account summary, that reports the total equity and spot balances of a funding (main) account, and its constituent trading (sub) accounts<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |AggregatedAccountSummary|True|The aggregated account summary|
    ??? info "[AggregatedAccountSummary](/../../schemas/aggregated_account_summary)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |main_account_id<br>`ma` |string|True|The main account ID of the account to which the summary belongs|
        |total_equity<br>`te` |string|True|Total equity of the main (+ sub) account, denominated in USD|
        |spot_balances<br>`sb` |[SpotBalance]|True|The list of spot assets owned by this main (+ sub) account, and their balances|
        ??? info "[SpotBalance](/../../schemas/spot_balance)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |currency<br>`c` |Currency|True|The currency you hold a spot balance in|
            |balance<br>`b` |string|True|This currency's balance in this trading account.|
            |index_price<br>`ip` |string|True|The index price of this currency. (reported in `USD`)|
            ??? info "[Currency](/../../schemas/currency)"
                The list of Currencies that are supported on the GRVT exchange<br>

                |Value| Description |
                |-|-|
                |`USD` = 1|the USD fiat currency|
                |`USDC` = 2|the USDC token|
                |`USDT` = 3|the USDT token|
                |`ETH` = 4|the ETH token|
                |`BTC` = 5|the BTC token|
