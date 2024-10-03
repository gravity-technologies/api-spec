!!! info "[WSTradeFeedSelectorV1](schemas/ws_trade_feed_selector_v1.md)"
    Subscribes to a stream of Public Trades for an instrument.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
    |limit<br>`l` |number|True|The limit to query for. Defaults to 500; Max 1000|