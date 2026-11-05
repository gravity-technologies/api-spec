!!! info "[ApiCreateAlgoOrderResponse](/../../schemas/api_create_algo_order_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |AlgoOrder|True|The created algo order|
    ??? info "[AlgoOrder](/../../schemas/algo_order)"
        An algo order is the parent order of an algorithmic execution strategy. Instead of resting on the orderbook itself, it is a set of instructions that GRVT Backend executes on your behalf by placing and managing sub-orders, until the algo order is filled, cancelled or expired.<br><br>Algo trading must be enabled (opted in) for the sub account before an algo order can be created.<br><br>The algo order is not signed by you. Sub-orders are placed by GRVT Backend and never appear on the `v1.order` and `v1.state` streams; follow the algo order itself through the `v1.algo.order` stream.<br><br>The `type` field selects the strategy. Currently only `CHASE` is supported.<br><br>**CHASE**: a post-only limit order that automatically follows the market. The order is placed at the best bid (buy) or best ask (sell), and periodically re-priced to keep up with the market, until it is filled, cancelled or expired. Because it is always post-only, it only ever adds liquidity and is never executed as a taker. The chase parameters are in `metadata.chase`.<ul><li>An optional `trigger` keeps the algo order pending until the trigger condition crosses; a chase order without a trigger starts chasing immediately.</li><li>A partial fill does not stop the chase: the unfilled remainder keeps being re-priced.</li></ul>An algo order is `PENDING` while it waits for its trigger, `OPEN` while it is actively chasing (including while held at the maximum distance), and `FILLED`, `CANCELLED` or `REJECTED` once terminated.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |algo_order_id<br>`ao` |string|False<br>`0`|[Filled by GRVT Backend] A unique 128-bit identifier for the algo order, assigned by Trade Data|
        |sub_account_id<br>`sa` |string|True|The subaccount initiating the algo order|
        |type<br>`t` |AlgoOrderType|True|The type of the algo order|
        |post_only<br>`po` |boolean|False<br>`false`|If True, every sub-order must be a maker order. Chase orders are always post-only|
        |reduce_only<br>`ro` |boolean|False<br>`false`|If True, every sub-order must reduce the position size, or be cancelled|
        |leg<br>`l` |AlgoOrderLeg|True|The single leg traded by this algo order|
        |metadata<br>`m` |AlgoOrderMetadata|True|Algo order metadata, including the type-specific parameters|
        |state<br>`s` |AlgoOrderState|False<br>`''`|[Filled by GRVT Backend] The current state of the algo order|
        |builder<br>`b` |string|True|The main account ID of the builder|
        |builder_fee<br>`bf` |string|True|Builder fee charged for every sub-order, expressed as a percentage (e.g., 0.001 means 0.001%). |
        ??? info "[AlgoOrderType](/../../schemas/algo_order_type)"
            Defines the type of an algo order<br>

            |Value| Description |
            |-|-|
            |`CHASE` = 1|CHASE - A post-only limit order that re-prices toward the best bid/ask until filled or cancelled|
        ??? info "[AlgoOrderLeg](/../../schemas/algo_order_leg)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |instrument<br>`i` |string|True|The instrument to trade|
            |size<br>`s` |string|True|The total number of assets to trade across all sub-orders, expressed in base asset decimal units.|
            |is_buying_asset<br>`ib` |boolean|True|Specifies if the algo order is a buy or sell|
        ??? info "[AlgoOrderMetadata](/../../schemas/algo_order_metadata)"
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
        ??? info "[AlgoOrderState](/../../schemas/algo_order_state)"
            |Name<br>`Lite`|Type|Required<br>`Default`| Description |
            |-|-|-|-|
            |status<br>`s` |OrderStatus|True|The status of the algo order|
            |reject_reason<br>`rr` |OrderRejectReason|True|The reason for rejection or cancellation|
            |traded_size<br>`ts` |string|True|The total number of assets traded across all sub-orders|
            |avg_fill_price<br>`af` |string|True|The average fill price across all sub-orders|
            |trigger_time<br>`tt` |string|False<br>`0`|Time at which the algo order was triggered in unix nanoseconds, 0 if not triggered yet|
            |update_time<br>`ut` |string|True|Time at which the algo order was updated by GRVT in unix nanoseconds|
            |chase<br>`c` |ChaseOrderState|False<br>``|Chase order state. Set only when the algo order type is CHASE|
            |last_sub_order_id<br>`ls` |string|True|The latest sub-order placed for this algo order, 0 until the first sub-order is placed|
            ??? info "[OrderStatus](/../../schemas/order_status)"
                |Value| Description |
                |-|-|
                |`PENDING` = 1|Order has been sent to the matching engine and is pending a transition to open/filled/rejected.|
                |`OPEN` = 2|Order is actively matching on the matching engine, could be unfilled or partially filled.|
                |`FILLED` = 3|Order is fully filled and hence closed. Taker Orders can transition directly from pending to filled, without going through open.|
                |`REJECTED` = 4|Order is rejected by matching engine since if fails a particular check (See OrderRejectReason). Once an order is open, it cannot be rejected.|
                |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason). Before an order is open, it cannot be cancelled.|
            ??? info "[OrderRejectReason](/../../schemas/order_reject_reason)"
                |Value| Description |
                |-|-|
                |`UNSPECIFIED` = 0|order is not cancelled or rejected|
                |`CLIENT_CANCEL` = 1|client called a Cancel API|
                |`CLIENT_BULK_CANCEL` = 2|client called a Bulk Cancel API|
                |`CLIENT_SESSION_END` = 3|client called a Session Cancel API, or set the WebSocket connection to 'cancelOrdersOnTerminate'|
                |`MARKET_CANCEL` = 4|the market order was cancelled after no/partial fill. Lower precedence than other TimeInForce cancel reasons|
                |`IOC_CANCEL` = 5|the IOC order was cancelled after no/partial fill|
                |`AON_CANCEL` = 6|the AON order was cancelled as it could not be fully matched|
                |`FOK_CANCEL` = 7|the FOK order was cancelled as it could not be fully matched|
                |`EXPIRED` = 8|the order was cancelled as it has expired|
                |`FAIL_POST_ONLY` = 9|the post-only order could not be posted into the orderbook|
                |`FAIL_REDUCE_ONLY` = 10|the reduce-only order would have caused position size to increase|
                |`MM_PROTECTION` = 11|the order was cancelled due to market maker protection trigger|
                |`SELF_TRADE_PROTECTION` = 12|the order was cancelled due to self-trade protection trigger|
                |`SELF_MATCHED_SUBACCOUNT` = 13|the order matched with another order from the same sub account|
                |`OVERLAPPING_CLIENT_ORDER_ID` = 14|an active order on your sub account shares the same clientOrderId|
                |`BELOW_MARGIN` = 15|the order will bring the sub account below initial margin requirement|
                |`LIQUIDATION` = 16|the sub account is liquidated (and all open orders are cancelled by Gravity)|
                |`INSTRUMENT_INVALID` = 17|instrument is invalid or not found on Gravity|
                |`INSTRUMENT_DEACTIVATED` = 18|instrument is no longer tradable on Gravity. (typically due to a market halt, or instrument expiry)|
                |`SYSTEM_FAILOVER` = 19|system failover resulting in loss of order state|
                |`UNAUTHORISED` = 20|the credentials used (userSession/apiKeySession/walletSignature) is not authorised to perform the action|
                |`SESSION_KEY_EXPIRED` = 21|the session key used to sign the order expired|
                |`SUB_ACCOUNT_NOT_FOUND` = 22|the subaccount does not exist|
                |`NO_TRADE_PERMISSION` = 23|the signature used to sign the order has no trade permission|
                |`UNSUPPORTED_TIME_IN_FORCE` = 24|the order payload does not contain a supported TimeInForce value|
                |`MULTI_LEGGED_ORDER` = 25|the order has multiple legs, but multiple legs are not supported by this venue|
                |`EXCEED_MAX_POSITION_SIZE` = 26|the order would have caused the subaccount to exceed the max position size|
                |`EXCEED_MAX_SIGNATURE_EXPIRATION` = 27|the signature supplied is more than 30 days in the future|
                |`MARKET_ORDER_WITH_LIMIT_PRICE` = 28|the market order has a limit price set|
                |`CLIENT_CANCEL_ON_DISCONNECT_TRIGGERED` = 29|client cancel on disconnect triggered|
                |`OCO_COUNTER_PART_TRIGGERED` = 30|the OCO counter part order was triggered|
                |`REDUCE_ONLY_LIMIT` = 31|the remaining order size was cancelled because it exceeded current position size|
                |`CLIENT_REPLACE` = 32|the order was replaced by a client replace request|
                |`DERISK_MUST_BE_IOC` = 33|the derisk order must be an IOC order|
                |`DERISK_MUST_BE_REDUCE_ONLY` = 34|the derisk order must be a reduce-only order|
                |`DERISK_NOT_SUPPORTED` = 35|derisk is not supported|
                |`INVALID_ORDER_TYPE` = 36|the order type is invalid|
                |`CURRENCY_NOT_DEFINED` = 37|the currency is not defined|
                |`INVALID_CHAIN_ID` = 38|the chain ID is invalid|
                |`BUILDER_ORDER_FEE_EXCEED` = 39|Builder fee exceed the limit|
                |`BUILDER_ORDER_FEE_NEGATIVE` = 40|Builder fee is below 0|
                |`BUILDER_ORDER_BUILDER_NOT_AUTHORIZED` = 41|Builder is not an authorized builder for client|
                |`BUILDER_ORDER_BUILDER_NOT_EXIST` = 42|Builder does not exist|
                |`TRADE_PRICE_WORSE_THAN_BANKRUPTCY_PRICE` = 44|the trade price is worse than the bankruptcy price|
                |`TOO_MANY_MAKER_ORDERS` = 45|the order was cancelled due to matching with too many maker orders|
                |`REDUCE_ONLY_NOT_SUPPORTED_FOR_SPOT_ORDER` = 46|reduce-only order is not supported for spot order|
                |`TPSL_NOT_SUPPORTED_FOR_SPOT_ORDER` = 47|tpsl is not supported for spot order|
                |`SPOT_ORDER_NOT_SUPPORTED` = 48|spot order is not supported|
                |`INSUFFICIENT_BALANCE` = 49|the subaccount has insufficient balance|
                |`SPOT_TRADING_BLOCKED_DURING_SOCIALIZED_LOSS` = 50|spot trading is blocked during socialized loss (SLOW)|
                |`BELOW_MARGIN_WITH_PENALTY_DEVIATION` = 51|the order will bring the sub account below initial margin requirement considering wide price deviation|
                |`CORPORATE_ACTION` = 56|Cancelled by the system due to Corporate Action|
                |`NOT_QUALIFIED_MAKER` = 57|the order was rejected because the sub account is not a qualified maker|
                |`PRIVATE_QUOTE_REQUIRES_RFQ` = 58|rfq_id is required when is_private = true|
                |`STABLE_PERP_REQUIRES_PRICE_BOUND` = 59|a signed slippage bound filled in limit_price is required|
                |`UNSUPPORTED_TRIGGER_BY` = 60|SFP order only supports trigger_by = index or mid|
                |`RFQ_NOT_FOUND` = 61|the order was rejected because the referenced RFQ could not be found|
                |`RESTING_ORDER_WOULD_CROSS` = 62|post-only resting placement crosses opposite best resting or index mid|
                |`SESSION_CLOSED` = 63|the order was submitted when the trading session was either closed or under maintenance|
                |`RFQ_TERMINATED` = 65|the quote was cancelled because the RFQ it was bound to reached a terminal state — expired, cancelled by the taker, or closed once its taker order filled|
                |`STABLE_PERP_REQUIRES_MULTI_ASSET_MODE` = 66|stable perp orders require a multi-asset-mode sub-account|
                |`BORROW_LIMIT_EXCEEDED_AFTER_TRADE` = 67|the trade would have left the sub account borrowing more than its tier borrow limit in the traded quote currency|
                |`UNDEPLOYED_LOAN_AUTO_EXCHANGE` = 68|an undeployed-loan (LTV) auto-exchange executed on the sub account, and all open orders are cancelled by Gravity|
                |`LIQUIDATION_AUTO_EXCHANGE` = 69|a liquidation auto-exchange executed on the sub account, and all open orders are cancelled by Gravity|
                |`USDC_COLLATERAL_DISABLED` = 70|USDC is not enabled as collateral on the sub account, so USDC-quoted instruments cannot be traded; enable USDC as collateral first|
                |`SFP_POST_ONLY_NOT_ALLOWED` = 71|post-only orders are not supported on STABLE_PERP for accounts that are not qualified market makers; their orders only take liquidity|
                |`VAULT_NON_QUOTE_INVESTMENT_CURRENCY` = 72|the order was rejected because its sub account is a vault in single-asset margin mode whose investment currency is not its quote currency, and such a vault cannot trade|
                |`RFQ_ID_REQUIRES_STABLE_PERP` = 161|rfq_id was set on an order whose instrument is not a STABLE_PERP; RFQ is a STABLE_PERP-only product|
                |`RFQ_PRIVATE_POOL_NOT_SUPPORTED` = 162|is_private = true is not supported yet; private per-RFQ quote pools are post-MVP|
                |`RFQ_REQUIRES_IOC` = 163|the taker order accepting an RFQ must be a bounded IOC order — IOC, carrying a limit price; an acceptance takes liquidity immediately and must not be able to rest on the book|
                |`RFQ_MISMATCH` = 164|the order does not match the RFQ it references — wrong instrument, or a side the RFQ did not request|
                |`RFQ_ALREADY_BOUND` = 165|the RFQ already has a taker order bound to it; an RFQ accepts only one|
                |`RFQ_MAKER_MUST_BE_ECN` = 166|a resting order carrying rfq_id must be an ECN quote (is_ecn = true)|
                |`FOK_NOT_SUPPORTED` = 167|fill-or-kill is not supported on STABLE_PERP yet|
                |`MARKET_ORDER_NOT_SUPPORTED` = 168|market orders are not supported on STABLE_PERP; a taker order must be a bounded IOC order, carrying a limit price|
                |`STABLE_PERP_ORDER_NOT_SUPPORTED` = 169|STABLE_PERP orders are disabled on this cluster|
            ??? info "[ChaseOrderState](/../../schemas/chase_order_state)"
                Contains the runtime state specific to a chase algo order<br>

                |Name<br>`Lite`|Type|Required<br>`Default`| Description |
                |-|-|-|-|
                |reprice_count<br>`rc` |integer|True|The number of successful re-prices of this algo order's sub-orders|
