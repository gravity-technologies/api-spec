!!! info "[TPSLOrderTrigger](/../../schemas/tpsl_order_trigger)"
    TPSL Order Trigger fields are used to support any type of trigger order such as TP/SL.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |trigger_type<br>`tt` |TriggerType|True|The type that triggers a take profit or stop loss order|
    |trigger_point<br>`tp` |string|True|The Trigger Price of the order, expressed in `9` decimals.If Trigger Type is percentage based, this will be interpreted as 0.01 bps, eg. 100 = 1bps|
    |conditional_client_order_id<br>`cc` |string|True|Used for OCO orders. If this order is triggered, the conditionalClientOrderID will be cancelled|
    ??? info "[TriggerType](/../../schemas/trigger_type)"
        The type that triggers a take profit or stop loss order<br><br>

        |Value| Description |
        |-|-|
        |`UNSPECIFIED` = 0|no trigger condition|
        |`INDEX` = 1|INDEX - Order is activated when the index price reaches the trigger price|
