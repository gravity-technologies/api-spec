!!! info "[WSOrderbookLevelsFeedDataV1](schemas/ws_orderbook_levels_feed_data_v1.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|Stream name|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A running sequence number that determines global message order within the specific stream|
    |feed<br>`f` |OrderbookLevels|True|An orderbook levels object matching the request filter|
    ??? info "[OrderbookLevels](schemas/orderbook_levels.md)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
        |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
        |bids<br>`b` |[OrderbookLevel]|True|The list of best bids up till query depth|
        |asks<br>`a` |[OrderbookLevel]|True|The list of best asks up till query depth|
        ??? info "[OrderbookLevel](schemas/orderbook_level.md)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |price<br>`p` |string|True|The price of the level, expressed in `9` decimals|
            |size<br>`s` |string|True|The number of assets offered, expressed in base asset decimal units|
            |num_orders<br>`no` |number|True|The number of open orders at this level|
        ??? info "[OrderbookLevel](schemas/orderbook_level.md)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |price<br>`p` |string|True|The price of the level, expressed in `9` decimals|
            |size<br>`s` |string|True|The number of assets offered, expressed in base asset decimal units|
            |num_orders<br>`no` |number|True|The number of open orders at this level|
