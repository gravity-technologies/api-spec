!!! info "[ApiGetOrderRequest](schemas/api_get_order_request.md)"
    Retrieve the order for the account. Either `order_id` or `client_order_id` must be provided.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |order_id<br>`oi` |string|False<br>`0`|Filter for `order_id`|
    |client_order_id<br>`co` |string|False<br>`0`|Filter for `client_order_id`|