!!! info "[WSRfqFeedDataV1](/../../schemas/ws_rfq_feed_data_v1)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|Stream name|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A sequence number used to determine message order within a stream.<br>- If `useGlobalSequenceNumber` is **false**, this returns the gateway sequence number, which increments by one locally within each stream and resets on gateway restarts.<br>- If `useGlobalSequenceNumber` is **true**, this returns the global sequence number, which uniquely identifies messages across the cluster.<br>  - A single cluster payload can be multiplexed into multiple stream payloads.<br>  - To distinguish each stream payload, a `dedupCounter` is included.<br>  - The returned sequence number is computed as: `cluster_sequence_number * 10^5 + dedupCounter`.|
    |feed<br>`f` |RfqFeed|True|The RFQ lifecycle event (NEW / EXPIRED / CANCELLED)|
    |prev_sequence_number<br>`ps` |string|True|The previous sequence number that determines the message order|
    ??? info "[RfqFeed](/../../schemas/rfq_feed)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |event<br>`e` |RfqEvent|True|The RFQ lifecycle event: NEW, EXPIRED, or CANCELLED. On EXPIRED/CANCELLED only rfqID is populated; the platform then auto-cancels the maker's private quotes bound to this RFQ|
        |rfq_id<br>`ri` |string|True|The RFQ this event refers to|
        |instrument<br>`i` |string|False<br>`None`|The RFQ instrument. Must be kind = STABLE_PERP|
        |size<br>`s` |string|False<br>`None`|Requested size, expressed in base asset decimal units. Zero-size = platform solicitation for missing public presence|
        |side<br>`s1` |RfqSide|False<br>`None`|Present only if the taker disclosed direction; omitted = two-way request|
        |expiry<br>`e1` |string|False<br>`None`|RFQ TTL. The timestamp after which Gravity expires the RFQ, expressed in unix nanoseconds|
        ??? info "[RfqEvent](/../../schemas/rfq_event)"
            |Value| Description |
            |-|-|
            |`NEW` = 1|a new maker channel was created|
            |`EXPIRED` = 2|both channels were expired|
            |`CANCELLED` = 3|both channels were cancelled|
        ??? info "[RfqSide](/../../schemas/rfq_side)"
            |Value| Description |
            |-|-|
            |`UNSPECIFIED` = 0|omitted = two-way request|
            |`BUY` = 1|the RFQ side is a buy|
            |`SELL` = 2|the RFQ side is a sell|
