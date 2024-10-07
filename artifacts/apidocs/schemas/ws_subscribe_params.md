!!! info "[WSSubscribeParams](/../../schemas/ws_subscribe_params)"
    All V1 Websocket Subscription Requests are housed in this wrapper. You may specify a stream, and a list of feeds to subscribe to.<br>When subscribing to the same primary selector again, the previous secondary selector will be replaced. See `Overview` page for more details.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|The channel to subscribe to (eg: ticker.s / ticker.d)|
    |selectors<br>`s1` |[string]|True|The list of feeds to subscribe to|
