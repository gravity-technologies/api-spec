!!! info "[RfqFeed](/../../schemas/rfq_feed)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |event<br>`e` |RfqEvent|True|The RFQ lifecycle event: NEW, EXPIRED, or CANCELLED. On EXPIRED/CANCELLED only rfqID is populated; the platform then auto-cancels the maker's private quotes bound to this RFQ|
    |rfq_id<br>`ri` |string|True|The RFQ this event refers to|
    |instrument<br>`i` |string|False<br>`None`|The RFQ instrument. Must be kind = STABLE_PERP|
    |taker_anon_account_id<br>`ta` |string|False<br>`None`|The taker's derived anonymous account id shown to makers. Real taker identity is never exposed|
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
