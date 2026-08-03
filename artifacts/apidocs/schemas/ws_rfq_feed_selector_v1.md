!!! info "[WSRfqFeedSelectorV1](/../../schemas/ws_rfq_feed_selector_v1)"
    Maker feed. Subscribe with selector `(sub_account_id, instrument)` to receive the RFQs you can quote on, delivered as lifecycle events (NEW, EXPIRED, CANCELLED). Respond to an RFQ by posting quotes via create_order (is_ecn = true, with `metadata.rfq_id` / `metadata.is_private`).<br><br>The subscription is stateful: from the moment you subscribe you are 'on' for that instrument — RFQs are delivered, your response ratios are tracked, and you are expected to keep a live public quote resting on the book (the platform nudges you with a zero-size RFQ if none is resting).<br><br>Each RFQ is uniquely identified by its `rfq_id`. A sub-account may hold at most one open RFQ per instrument, which is what lets this selector be keyed by `(sub_account_id, instrument)` alone, with no `rfq_id` required.<br><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |instrument<br>`i` |string|False<br>`'all'`|The instrument filter to apply.|
