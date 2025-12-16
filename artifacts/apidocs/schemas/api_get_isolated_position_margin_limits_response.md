!!! info "[ApiGetIsolatedPositionMarginLimitsResponse](/../../schemas/api_get_isolated_position_margin_limits_response)"
    The response to get the max addable and removable amount for an isolated position request<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |instrument<br>`i` |string|True|The isolated position asset|
    |max_addable_amount<br>`ma` |string|True|The max addable amount that can be added to the isolated position, expressed in quote asset decimal units|
    |max_removable_amount<br>`mr` |string|True|The max removable amount that can be removed from the isolated position, expressed in quote asset decimal units|
