!!! info "[ApiCreateRfqRequest](/../../schemas/api_create_rfq_request)"
    Creates a new RFQ (Request For Quote): a taker solicits private quotes for a single STABLE_PERP instrument by specifying a size, and optionally a direction (`rfq.side`; omit for a two-way request). This request is unsigned — creating an RFQ commits the taker to nothing.<br><br>End-to-end flow:<br>1. The taker submits an RFQ here. (In the GRVT UI, entering a size on the trade page is the RFQ.)<br>2. GRVT broadcasts the RFQ to makers on the `v1.rfq` stream; makers respond with private quotes.<br>3. Those private quotes stream back to the taker on the `v1.quote` stream, alongside the public order book (firm resting liquidity + public quotes) which is already visible.<br>4. The taker accepts by signing an order via create_order with `metadata.rfq_id` set (single leg; IOC or FOK), which executes across the private pool merged with the public book — or walks away and lets the RFQ expire.<br><br>The created RFQ is returned in the response. A sub-account may hold at most one open RFQ per instrument. The RFQ lives until `rfq.expiry`, after which GRVT expires it and auto-cancels the makers' private quotes bound to it.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |rfq<br>`r` |Rfq|True|The RFQ to create|
    ??? info "[Rfq](/../../schemas/rfq)"
        A Request for Quote (RFQ) lets a taker solicit private quotes on a single instrument from makers.<br><br><ul><li>Single instrument</li><ul><li>Each RFQ targets one instrument (kind = STABLE_PERP) for a single requested size.</li><li>The taker may disclose a direction via `rfq.side`, or omit it to request a two-way (buy and sell) quote.</li></ul><li>Maker solicitation</li><ul><li>On submission, GRVT broadcasts the RFQ to makers over the `v1.rfq` feed (see RfqFeed).</li><li>Makers respond with private quotes, which the taker receives as a private quote book over the `v1.quote` feed (see RfqQuoteFeed).</li></ul><li>Anonymity</li><ul><li>Anonymity is automatic and always enforced — the taker and makers only ever see each other's derived anonymous account ids.</li><li>Real taker and maker identities are never exposed to the counterparty.</li></ul><li>Expiry</li><ul><li>The RFQ lives until `rfq.expiry`, after which GRVT expires it and auto-cancels the makers' private quotes bound to it.</li></ul></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |rfq_id<br>`ri` |string|True|[Filled by GRVT Backend] A unique 128-bit identifier for the RFQ, deterministically generated within the GRVT backend|
        |sub_account_id<br>`sa` |string|True|The subaccount initiating the RFQ|
        |expiry<br>`e` |string|True|RFQ TTL. The timestamp after which Gravity expires the RFQ, expressed in unix nanoseconds. Default 60s, cap 300s (per-instrument config)|
        |instrument<br>`i` |string|True|The instrument to trade. Must be kind = STABLE_PERP|
        |size<br>`s` |string|True|Requested size (positive), expressed in base asset decimal units|
        |side<br>`s1` |RfqSide|False<br>`None`|Optional — omitted = two-way request. The GRVT UI always fills it; API takers may withhold direction and accept two-way quotes|
        ??? info "[RfqSide](/../../schemas/rfq_side)"
            |Value| Description |
            |-|-|
            |`UNSPECIFIED` = 0|omitted = two-way request|
            |`BUY` = 1|the RFQ side is a buy|
            |`SELL` = 2|the RFQ side is a sell|
