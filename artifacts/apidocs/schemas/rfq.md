!!! info "[Rfq](/../../schemas/rfq)"
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
