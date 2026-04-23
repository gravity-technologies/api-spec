!!! info "[SpotBalance](/../../schemas/spot_balance)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |currency<br>`c` |string|True|The currency you hold a spot balance in|
    |balance<br>`b` |string|True|This currency's balance in this trading account.|
    |index_price<br>`ip` |string|True|The index price of this currency. (reported in `USD`)|
    |entry_price<br>`ep` |string|True|The entry price of this spot currency. (reported in `USD`)|
    |realized_pnl<br>`rp` |string|True|The realized PnL of this spot currency. (reported in `USD`)|
    |unrealized_pnl<br>`up` |string|True|The unrealized PnL of this spot currency. (reported in `USD`)|
    |available_to_transfer<br>`at` |string|True|The available to transfer amount of this spot currency.|
