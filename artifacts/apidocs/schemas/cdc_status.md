!!! info "[CDCStatus](/../../schemas/cdc_status)"
    Per-asset collateral-deposit-cap (CDC) utilization status.<br>

    |Value| Description |
    |-|-|
    |`NORMAL` = 1|CDC utilization below the reduce-only threshold.|
    |`REDUCE_ONLY` = 2|CDC utilization at or above the reduce-only threshold but below 100% — new collateral deposits are restricted.|
    |`AUTO_EXCHANGE` = 3|CDC utilization at or above 100% — subject to auto-exchange.|
