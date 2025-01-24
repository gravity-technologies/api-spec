!!! info "[OrderMetadata](/../../schemas/order_metadata)"
    Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |client_order_id<br>`co` |string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
    |create_time<br>`ct` |string|False<br>`0`|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
    |trigger_order_metadata<br>`to` |TriggerOrderMetadata|True|Trigger fields are used to support any type of trigger order such as TP/SL|
    |broker<br>`b` |BrokerTag|False<br>``|Specifies the broker who brokered the order|
    ??? info "[TriggerOrderMetadata](/../../schemas/trigger_order_metadata)"
        Trigger fields are used to support any type of trigger order such as TP/SL.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |trigger_order_type<br>`to` |TriggerOrderType|True|Type of the trigger order. eg: Take Profit, Stop Loss, etc|
        |tpsl_order_trigger<br>`to1` |TPSLOrderTrigger|True|TODO:|
        |is_activated<br>`ia` |boolean|True|If the trigger order has been activated|
        ??? info "[TriggerOrderType](/../../schemas/trigger_order_type)"
            Type of the trigger order. eg: Take Profit, Stop Loss, etc<br>

            |Value| Description |
            |-|-|
            |`UNSPECIFIED` = 0|not a trigger order|
            |`TAKE_PROFIT` = 1|Take Profit Order. Requires a tpslOrderTrigger triggerType|
            |`STOP_LOSS` = 2|Stop Loss Order. Requires a tpslOrderTrigger triggerType|
        ??? info "[TPSLOrderTrigger](/../../schemas/tpsl_order_trigger)"
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
    ??? info "[BrokerTag](/../../schemas/broker_tag)"
        BrokerTag is a tag for the broker that the order is sent from.<br>

        |Value| Description |
        |-|-|
        |`COIN_ROUTES` = 1|CoinRoutes|
        |`ALERTATRON` = 2|Alertatron|
        |`ORIGAMI` = 3|Origami|
