!!! info "[WSECNToBrokerFeedSelectorV1](/../../schemas/wsecn_to_broker_feed_selector_v1)"
    Subscribes to a feed of order updates pertaining to orders made by your account.<br>Each Order can be uniquely identified by its `order_id` or `client_order_id`.<br>To subscribe to all orders, specify an empty `instrument` (eg. `2345123`).<br>Otherwise, specify the `instrument` to only receive orders for that instrument (eg. `2345123-BTC_USDT_Perp`).<br>This stream is only applicable to STABLE_PERP (SFP) instruments with qualified market makers.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
