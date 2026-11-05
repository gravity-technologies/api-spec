!!! info "[AlgoOrderMetadata](/../../schemas/algo_order_metadata)"
    Metadata fields are used to support Backend only operations.<br>Type-specific parameters live in the nested struct matching the algo order type.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |client_order_id<br>`co` |string|True|A unique identifier for the active algo order within a subaccount, specified by the client<br>This field can be used for algo order cancellation|
    |create_time<br>`ct` |string|False<br>`0`|[Filled by GRVT Backend] Time at which the algo order was received by GRVT in unix nanoseconds|
    |trigger<br>`t` |TriggerOrderMetadata|False<br>``|Trigger fields. If set, the algo order stays pending until the trigger price is crossed|
    |broker<br>`b` |BrokerTag|False<br>``|Specifies the broker who brokered the algo order|
    |expiry<br>`e` |string|False<br>`0`|Time at which the algo order expires, expressed in unix nanoseconds. Defaults to and must be capped at 90 days|
    |chase<br>`c` |ChaseAlgoOrderMetadata|False<br>``|Chase order parameters. Set only when the algo order type is CHASE|
    ??? info "[TriggerOrderMetadata](/../../schemas/trigger_order_metadata)"
        Contains metadata related to trigger orders, such as Take Profit (TP) or Stop Loss (SL).<br><br>Trigger orders are used to automatically execute an order when a predefined price condition is met, allowing traders to implement risk management strategies.<br><br><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |trigger_type<br>`tt` |TriggerType|True|Type of the trigger order. eg: Take Profit, Stop Loss, etc|
        |tpsl<br>`t` |TPSLOrderMetadata|True|Contains metadata for Take Profit (TP) and Stop Loss (SL) trigger orders.<br><br>|
        ??? info "[TriggerType](/../../schemas/trigger_type)"
            Defines the type of trigger order used in trading, such as Take Profit or Stop Loss.<br><br>Trigger orders allow execution based on pre-defined price conditions rather than immediate market conditions.<br><br><br>

            |Value| Description |
            |-|-|
            |`UNSPECIFIED` = 0|Not a trigger order. The order executes normally without any trigger conditions.|
            |`TAKE_PROFIT` = 1|Take Profit Order - Executes when the price reaches a specified level to secure profits.|
            |`STOP_LOSS` = 2|Stop Loss Order - Executes when the price reaches a specified level to limit losses.|
        ??? info "[TPSLOrderMetadata](/../../schemas/tpsl_order_metadata)"
            Contains metadata for Take Profit (TP) and Stop Loss (SL) trigger orders.<br><br>

            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |trigger_by<br>`tb` |TriggerBy|True|Defines the price type (e.g., index price) that activates a Take Profit (TP) or Stop Loss (SL) order|
            |trigger_price<br>`tp` |string|True|The Trigger Price of the order, expressed in `9` decimals.|
            |close_position<br>`cp` |boolean|True|If True, the order will close the position when the trigger price is reached|
            |is_split_position<br>`is` |boolean|True|If True, the order will be treated as part of a position's split-TP/SL set, subject to aggregate size/count limits.|
            ??? info "[TriggerBy](/../../schemas/trigger_by)"
                Defines the price type that activates a Take Profit (TP) or Stop Loss (SL) order.<br><br>Trigger orders are executed when the selected price type reaches the specified trigger price.Different price types ensure flexibility in executing strategies based on market conditions.<br><br><br>

                |Value| Description |
                |-|-|
                |`UNSPECIFIED` = 0|no trigger condition|
                |`INDEX` = 1|INDEX - Order is activated when the index price reaches the trigger price|
                |`LAST` = 2|LAST - Order is activated when the last trade price reaches the trigger price|
                |`MID` = 3|MID - Order is activated when the mid price reaches the trigger price|
                |`MARK` = 4|MARK - Order is activated when the mark price reaches the trigger price|
    ??? info "[BrokerTag](/../../schemas/broker_tag)"
        BrokerTag is a tag for the broker that the order is sent from.<br>

        |Value| Description |
        |-|-|
        |`UNSPECIFIED` = 0||
        |`COIN_ROUTES` = 1|CoinRoutes|
        |`ALERTATRON` = 2|Alertatron|
        |`ORIGAMI` = 3|Origami|
    ??? info "[ChaseAlgoOrderMetadata](/../../schemas/chase_algo_order_metadata)"
        Contains the parameters of a chase algo order.<ul><li>`chase_price_mode` defines how the price is derived at each re-price.</li><li>`max_distance` caps how far the chase price may move away from the reference price. Once the cap is reached, the order is held at the boundary instead of chasing further.</li></ul><br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |chase_price_mode<br>`cp` |ChasePriceMode|True|How the chase price is determined at each re-price tick|
        |max_distance<br>`md` |string|True|The maximum distance the chase price can move away from the reference price, as an absolute price distance in quote currency units, expressed in `9` decimals.<br>Always absolute: when the user picks a percentage, the client converts it and sends the result here.|
        |max_distance_bps<br>`md1` |integer|False<br>`0`|The max distance as a percentage in basis points (1 bp = 0.01%, 100% = 10000), as the user entered it. `0` if the user entered an absolute distance.<br>Informational only, for display and history. `maxDistance` is what is enforced.|
        ??? info "[ChasePriceMode](/../../schemas/chase_price_mode)"
            Defines how a chase order determines its price at each re-price tick<br>

            |Value| Description |
            |-|-|
            |`BEST_BID_ASK` = 1|BEST_BID_ASK - The chase price equals the best bid (buy) or best ask (sell)|
