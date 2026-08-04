!!! info "[WSRfqQuoteFeedDataV1](/../../schemas/ws_rfq_quote_feed_data_v1)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |stream<br>`s` |string|True|Stream name|
    |selector<br>`s1` |string|True|Primary selector|
    |sequence_number<br>`sn` |string|True|A sequence number used to determine message order within a stream.<br>- If `useGlobalSequenceNumber` is **false**, this returns the gateway sequence number, which increments by one locally within each stream and resets on gateway restarts.<br>- If `useGlobalSequenceNumber` is **true**, this returns the global sequence number, which uniquely identifies messages across the cluster.<br>  - A single cluster payload can be multiplexed into multiple stream payloads.<br>  - To distinguish each stream payload, a `dedupCounter` is included.<br>  - The returned sequence number is computed as: `cluster_sequence_number * 10^5 + dedupCounter`.|
    |feed<br>`f` |RfqQuoteFeed|True|The taker's private quote book for their open RFQ on this instrument|
    |prev_sequence_number<br>`ps` |string|True|The previous sequence number that determines the message order|
    ??? info "[RfqQuoteFeed](/../../schemas/rfq_quote_feed)"
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
            |maker_anon_account_id<br>`ma` |string|True|The maker's derived anonymous account id shown to the taker. Real maker identity is never exposed|
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
            |maker_anon_account_id<br>`ma` |string|True|The maker's derived anonymous account id shown to the taker. Real maker identity is never exposed|
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
