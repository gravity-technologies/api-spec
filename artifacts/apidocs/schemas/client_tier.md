!!! info "[ClientTier](/../../schemas/client_tier)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |tier<br>`t` |integer|True||
    |futures_taker_fee<br>`ft` |integer|True||
    |futures_maker_fee<br>`fm` |integer|True||
    |options_taker_fee<br>`ot` |integer|True||
    |options_maker_fee<br>`om` |integer|True||
    |spot_borrow_configs<br>`sb` |[ApiSpotBorrowConfig]|True|Per-currency borrow & collateral limits for this tier. Populated only in the funding_account_summary response; empty in raw config contexts.|
    ??? info "[ApiSpotBorrowConfig](/../../schemas/api_spot_borrow_config)"
        Per-currency borrow & collateral limits resolved at this account's tier (incl. per-account overrides).<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |currency<br>`c` |string|True||
        |borrow_limit<br>`bl` |string|True|BL — max borrowable amount, native units. 0 = not borrowable.|
        |borrow_rate<br>`br` |string|True|BR — annual borrow interest rate at this tier. Never exceeds the asset's maxBorrowRate.|
        |collateral_limit<br>`cl` |string|True|CL — max amount counted as collateral, native units. 0 = unlimited.|
