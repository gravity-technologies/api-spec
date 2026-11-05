!!! info "[WSAlgoOrderFeedSelectorV1](/../../schemas/ws_algo_order_feed_selector_v1)"
    Subscribes to a feed of algo order updates pertaining to algo orders made by your account.<br>Each algo order can be uniquely identified by its `algo_order_id` or `client_order_id`, and carries its `type` so that clients can filter by algo order type.<br>To subscribe to all algo orders, specify an empty `instrument` (eg. `2345123`).<br>Otherwise, specify the `instrument` to only receive algo orders for that instrument (eg. `2345123-BTC_USDT_Perp`).<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
