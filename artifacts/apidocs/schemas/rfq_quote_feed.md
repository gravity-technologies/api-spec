!!! info "[RfqQuoteFeed](/../../schemas/rfq_quote_feed)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |rfq_id<br>`ri` |string|True|The RFQ this private quote book belongs to|
    |best_bid<br>`bb` |string|False<br>`None`|Best (highest) bid price across the book, expressed in the instrument's quote-asset decimals.|
    |best_ask<br>`ba` |string|False<br>`None`|Best (lowest) ask price across the book, expressed in the instrument's quote-asset decimals.|
    |bid_levels<br>`bl` |[RfqQuoteLevel]|True|Private quote bid levels, sorted best (highest) price first|
    |ask_levels<br>`al` |[RfqQuoteLevel]|True|Private quote ask levels, sorted best (lowest) price first|
    ??? info "[RfqQuoteLevel](/../../schemas/rfq_quote_level)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |price<br>`p` |string|True|Price of the level, expressed in `9` decimals|
        |size<br>`s` |string|True|Size at this level, expressed in base asset decimal units|
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
        |price<br>`p` |string|True|Price of the level, expressed in `9` decimals|
        |size<br>`s` |string|True|Size at this level, expressed in base asset decimal units|
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
