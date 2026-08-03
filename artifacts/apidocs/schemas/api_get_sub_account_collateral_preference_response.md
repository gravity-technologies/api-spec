!!! info "[ApiGetSubAccountCollateralPreferenceResponse](/../../schemas/api_get_sub_account_collateral_preference_response)"
    The response to get the sub account collateral preference<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID the preferences apply to|
    |preferences<br>`p` |[ApiCollateralPreferenceStatus]|True|One entry per collateral-eligible currency (CVR configured), with its current effective state.|
    ??? info "[ApiCollateralPreferenceStatus](/../../schemas/api_collateral_preference_status)"
        The current effective collateral state of a single currency.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |currency<br>`c` |string|True|The currency whose collateral state is being reported|
        |enabled<br>`e` |boolean|True|Whether this currency currently counts as collateral for the sub account|
