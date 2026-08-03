!!! info "[ApiGetSubAccountCollateralPreferenceRequest](/../../schemas/api_get_sub_account_collateral_preference_request)"
    Fetch the per-currency collateral enable/disable state for a Multi-Asset Mode sub account.<br><br>Returns one entry per collateral-eligible currency (CVR > 0), including USDT, which is always enabled and cannot be toggled off.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID to fetch collateral preferences for|
