!!! info "[ApiGetAlgoOrderRequest](/../../schemas/api_get_algo_order_request)"
    Retrieve an algo order for the account. Either `algo_order_id` or `client_order_id` must be provided.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |algo_order_id<br>`ao` |string|False<br>`0`|Filter for `algo_order_id`|
    |client_order_id<br>`co` |string|False<br>`0`|Filter for `client_order_id`|
