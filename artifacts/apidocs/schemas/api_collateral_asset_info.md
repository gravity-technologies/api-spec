!!! info "[ApiCollateralAssetInfo](/../../schemas/api_collateral_asset_info)"
    Platform-wide collateral configuration and usage for a single asset<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |currency<br>`c` |string|True|The asset|
    |collateral_value_ratio<br>`cv` |string|True|CVR, expressed in percentage points. 0 = not usable as collateral.|
    |collateral_deposit_cap<br>`cd` |string|True|CDC limit, native units. 0 = untracked / unlimited.|
    |max_borrow_rate<br>`mb` |string|True|MBR - per-asset ceiling on the annual borrow rate, expressed in percentage points; the tier borrow rate never exceeds this.|
    |manual_repayment_fee_rate<br>`mr` |string|True|Effective manual-repay/convert fee = max((1-CVR)/MRR, RFR), expressed in percentage points.|
    |cdc_status<br>`cs` |CDCStatus|True|Collateral-deposit-cap utilization status: normal / reduceOnly / autoExchange.|
    ??? info "[CDCStatus](/../../schemas/cdc_status)"
        Per-asset collateral-deposit-cap (CDC) utilization status.<br>

        |Value| Description |
        |-|-|
        |`NORMAL` = 1|CDC utilization below the reduce-only threshold.|
        |`REDUCE_ONLY` = 2|CDC utilization at or above the reduce-only threshold but below 100% — new collateral deposits are restricted.|
        |`AUTO_EXCHANGE` = 3|CDC utilization at or above 100% — subject to auto-exchange.|
