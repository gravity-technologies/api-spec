!!! info "[ApiAlgoSubOrderHistoryRequest](/../../schemas/api_algo_sub_order_history_request)"
    Retrieves the terminal sub-orders of an algo order. A sub-order appears once it reaches a terminal state: partially filled and superseded, fully filled, cancelled or rejected. Re-price cancels and rejects are not included.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |algo_order_id<br>`ao` |string|True|The `algo_order_id` whose sub-orders are retrieved|
