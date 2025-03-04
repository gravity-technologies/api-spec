!!! info "[WSOrderGroupFeedDataV1](/../../schemas/ws_order_group_feed_data_v1)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|Stream name|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
    |feed<br>`f` |ClientOrderIDsByGroup|True|The order object being created or updated|
    ??? info "[ClientOrderIDsByGroup](/../../schemas/client_order_i_ds_by_group)"
        Grouping for the client order id and their associated groups.<br><br>This is used to define TP/SL pairs or other order groupings after loading the list of Open Orders.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |group_id<br>`gi` |string|True|The group this order belongs to. It can be used to define TP/SL pairs or other order groupings|
        |client_order_id<br>`co` |[string]|True|List of client order IDs in the group|
        |sub_account_id<br>`sa` |string|True|The sub account ID that these orders belong to|
