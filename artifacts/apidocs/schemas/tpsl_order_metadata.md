!!! info "[TPSLOrderMetadata](/../../schemas/tpsl_order_metadata)"
    Contains metadata for Take Profit (TP) and Stop Loss (SL) trigger orders.<br><br>### Fields:<br>- **triggerBy**: Defines the price type that activates the order (e.g., index price).<br>- **triggerPrice**: The price at which the order is triggered, expressed in `9` decimal precision.<br><br><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |trigger_by<br>`tb` |TriggerBy|True|Defines the price type that activates a Take Profit (TP) or Stop Loss (SL) order|
    |trigger_price<br>`tp` |string|True|The Trigger Price of the order, expressed in `9` decimals.|
