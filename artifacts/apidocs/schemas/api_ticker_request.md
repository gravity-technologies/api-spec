!!! info "[ApiTickerRequest](/../../schemas/api_ticker_request)"
    Retrieves a single ticker value for a single instrument. Please do not use this to repeatedly poll for data -- a websocket subscription is much more performant, and useful.<br><br>Rate limit:<ul><li>Perpetual, future, option and spot instruments: the standard rate limit for this endpoint, per IP address.</li><li>Stable perps (`_SFP` instruments): a separate per-IP-address limit, shared across all stable perp instruments (one budget for all of them, not one per instrument). IP addresses on the gateway whitelist are exempt.</li></ul>A request over the limit is rejected with error `1006` (HTTP `429`). The `X-RateLimit-Limit` and `X-RateLimit-Remaining` response headers show the limit that applied to the request.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
