!!! info "[ApiSpotSubAccountSummaryResponse](/../../schemas/api_spot_sub_account_summary_response)"
    The spot account summary, that reports the total equity and spot balances of a spot sub account<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |SpotSubAccount|True|The spot sub account summary|
    ??? info "[SpotSubAccount](/../../schemas/spot_sub_account)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
        |sub_account_id<br>`sa` |string|True|The sub account ID this entry refers to|
        |total_equity<br>`te` |string|True|Total equity of the spot sub account, denominated USD|
        |spot_balances<br>`sb` |[SpotBalance]|True|The list of spot assets owned by this spot sub account, and their balances|
        ??? info "[SpotBalance](/../../schemas/spot_balance)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |currency<br>`c` |string|True|The currency you hold a spot balance in|
            |balance<br>`b` |string|True|This currency's balance in this trading account.|
            |index_price<br>`ip` |string|True|The index price of this currency. (reported in `USD`)|
            |entry_price<br>`ep` |string|True|The entry price of this spot currency. (reported in `USD`)|
            |realized_pnl<br>`rp` |string|True|The realized PnL of this spot currency. (reported in `USD`)|
            |unrealized_pnl<br>`up` |string|True|The unrealized PnL of this spot currency. (reported in `USD`)|
            |available_to_transfer<br>`at` |string|True|The available to transfer amount of this spot currency.|
