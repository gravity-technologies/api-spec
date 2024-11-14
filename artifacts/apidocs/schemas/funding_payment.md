!!! info "[FundingPayment](/../../schemas/funding_payment)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
    |sub_account_id<br>`sa` |string|True|The sub account ID that made the funding payment|
    |instrument<br>`i` |string|True|The perpetual instrument being funded|
    |currency<br>`c` |Currency|True|The currency of the funding payment|
    |amount<br>`a` |string|True|The amount of the funding payment. Positive if paid, negative if received|
    |tx_id<br>`ti` |string|True|The transaction ID of the funding payment.<br>Funding payments can be triggered by a trade, transfer, or liquidation.<br>The `tx_id` will match the corresponding `trade_id` or `tx_id`.|
    ??? info "[Currency](/../../schemas/currency)"
        The list of Currencies that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`USD` = 1|the USD fiat currency|
        |`USDC` = 2|the USDC token|
        |`USDT` = 3|the USDT token|
        |`ETH` = 4|the ETH token|
        |`BTC` = 5|the BTC token|
