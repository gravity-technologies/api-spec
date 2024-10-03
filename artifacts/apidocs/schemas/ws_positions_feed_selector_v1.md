!!! info "[WSPositionsFeedSelectorV1](schemas/ws_positions_feed_selector_v1.md)"
    Subscribes to a feed of position updates. This happens when a trade is executed.<br>To subscribe to all positions, specify an empty `instrument` (eg. `2345123`).<br>Otherwise, specify the `instrument` to only receive positions for that instrument (eg. `2345123-BTC_USDT_Perp`).<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
