!!! info "[RfqQuoteFeed](/../../schemas/rfq_quote_feed)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |rfq_id<br>`ri` |string|True|The RFQ this estimate belongs to. A feed with no levels means the RFQ ended|
    |best_bid<br>`bb` |string|False<br>`None`|Average fill price to sell the RFQ size, expressed in `9` decimals. Omitted when the bid side is empty|
    |best_ask<br>`ba` |string|False<br>`None`|Average fill price to buy the RFQ size, expressed in `9` decimals. Omitted when the ask side is empty|
    |bid_levels<br>`bl` |[RfqQuoteLevel]|True|The sell-side estimate (at most one level), from the bids|
    |ask_levels<br>`al` |[RfqQuoteLevel]|True|The buy-side estimate (at most one level), from the asks|
    ??? info "[RfqQuoteLevel](/../../schemas/rfq_quote_level)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |price<br>`p` |string|True|Average fill price for the size, expressed in `9` decimals. Rounded against the taker: up for asks, down for bids|
        |size<br>`s` |string|True|Fillable size, up to the RFQ size, expressed in base asset decimal units|
        |time_in_force<br>`ti` |TimeInForce|True|Distinguishes an AON level (liftable only in full — POST-MVP) from a GTT level|
        ??? info "[TimeInForce](/../../schemas/time_in_force)"
            |                       | Must Fill All | Can Fill Partial |
            | -                     | -             | -                |
            | Must Fill Immediately | FOK           | IOC              |
            | Can Fill Till Time    | AON           | GTC              |
            <br>

            |Value| Description |
            |-|-|
            |`GOOD_TILL_TIME` = 1|GTT - Remains open until it is cancelled, or expired|
            |`ALL_OR_NONE` = 2|AON - Either fill the whole order or none of it (Block Trades Only)|
            |`IMMEDIATE_OR_CANCEL` = 3|IOC - Fill the order as much as possible, when hitting the orderbook. Then cancel it|
            |`FILL_OR_KILL` = 4|FOK - Both AoN and IoC. Either fill the full order when hitting the orderbook, or cancel it|
            |`RETAIL_PRICE_IMPROVEMENT` = 5|RPI - A GTT + PostOnly maker order, that can only be taken by non-algorithmic UI users.|
    ??? info "[RfqQuoteLevel](/../../schemas/rfq_quote_level)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |price<br>`p` |string|True|Average fill price for the size, expressed in `9` decimals. Rounded against the taker: up for asks, down for bids|
        |size<br>`s` |string|True|Fillable size, up to the RFQ size, expressed in base asset decimal units|
        |time_in_force<br>`ti` |TimeInForce|True|Distinguishes an AON level (liftable only in full — POST-MVP) from a GTT level|
        ??? info "[TimeInForce](/../../schemas/time_in_force)"
            |                       | Must Fill All | Can Fill Partial |
            | -                     | -             | -                |
            | Must Fill Immediately | FOK           | IOC              |
            | Can Fill Till Time    | AON           | GTC              |
            <br>

            |Value| Description |
            |-|-|
            |`GOOD_TILL_TIME` = 1|GTT - Remains open until it is cancelled, or expired|
            |`ALL_OR_NONE` = 2|AON - Either fill the whole order or none of it (Block Trades Only)|
            |`IMMEDIATE_OR_CANCEL` = 3|IOC - Fill the order as much as possible, when hitting the orderbook. Then cancel it|
            |`FILL_OR_KILL` = 4|FOK - Both AoN and IoC. Either fill the full order when hitting the orderbook, or cancel it|
            |`RETAIL_PRICE_IMPROVEMENT` = 5|RPI - A GTT + PostOnly maker order, that can only be taken by non-algorithmic UI users.|
