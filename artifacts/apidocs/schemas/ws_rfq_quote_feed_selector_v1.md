!!! info "[WSRfqQuoteFeedSelectorV1](/../../schemas/ws_rfq_quote_feed_selector_v1)"
    Taker feed. Subscribe with selector `(sub_account_id, instrument)` to receive your private RFQ quote book — best bid/ask and all private quote levels — for your open RFQ on that instrument.<br><br>These private quotes are the makers' responses to your RFQ (created via ApiCreateRfqRequest). View them alongside the public order book (firm resting liquidity + public quotes) to decide, then accept by signing an order via create_order with `metadata.rfq_id` set.<br><br>Each update pertains to a single RFQ, uniquely identified by its `rfq_id`. A sub-account may hold at most one open RFQ per instrument, which is what lets this selector be keyed by `(sub_account_id, instrument)` alone, with no `rfq_id` required.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
