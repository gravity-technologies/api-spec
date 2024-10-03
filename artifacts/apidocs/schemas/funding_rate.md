!!! info "[FundingRate](schemas/funding_rate.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |instrument<br>`i` |string|True|The readable instrument name:<ul><li>Perpetual: `ETH_USDT_Perp`</li><li>Future: `BTC_USDT_Fut_20Oct23`</li><li>Call: `ETH_USDT_Call_20Oct23_2800`</li><li>Put: `ETH_USDT_Put_20Oct23_2800`</li></ul>|
    |funding_rate<br>`fr` |number|True|The funding rate of the instrument, expressed in centibeeps|
    |funding_time<br>`ft` |string|True|The funding timestamp of the funding rate, expressed in unix nanoseconds|
    |mark_price<br>`mp` |string|True|The mark price of the instrument at funding timestamp, expressed in `9` decimals|