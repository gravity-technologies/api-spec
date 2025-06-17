!!! info "[ApiVaultDetailResponse](/../../schemas/api_vault_detail_response)"
    Response payload for the detail of a vault.<br><br>This API provides the detail of a vault.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |share_price<br>`sp` |string|True|The share price of the vault.|
    |total_equity<br>`te` |string|True|The total equity of the vault.|
    |valuation_cap<br>`vc` |string|True|The valuation cap of the vault.|
    |unrealized_pnl<br>`up` |string|True|The total unrealized PnL of all positions owned by this subaccount, denominated in quote currency decimal units.<br>`unrealized_pnl = sum(position.unrealized_pnl * position.quote_index_price) / settle_index_price`|
    |initial_margin<br>`im` |string|True|The `total_equity` required to open positions in the account (reported in `settle_currency`).<br>Computation is different depending on account's `margin_type`|
    |maintenance_margin<br>`mm` |string|True|The `total_equity` required to avoid liquidation of positions in the account (reported in `settle_currency`).<br>Computation is different depending on account's `margin_type`|
