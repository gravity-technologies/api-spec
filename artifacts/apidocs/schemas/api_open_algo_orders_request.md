!!! info "[ApiOpenAlgoOrdersRequest](/../../schemas/api_open_algo_orders_request)"
    Retrieves all open algo orders for the account, including algo orders still pending on their trigger.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID to filter by|
    |kind<br>`k` |[Kind]|False<br>`all`|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned|
    |base<br>`b` |[string]|False<br>`all`|The base filter to apply. If nil, this defaults to all bases. Otherwise, only entries matching the filter will be returned|
    |quote<br>`q` |[string]|False<br>`all`|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned|
    |type<br>`t` |[AlgoOrderType]|False<br>`all`|The algo order type filter to apply. If nil, this defaults to all types. Otherwise, only entries matching the filter will be returned|
    |trigger_filter<br>`tf` |AlgoTriggerFilter|False<br>`all`|The trigger filter to apply. If nil, this defaults to all algo orders. Otherwise, `WITH_TRIGGER` returns only algo orders that carry a trigger, and `WITHOUT_TRIGGER` returns only those that do not|
    ??? info "[Kind](/../../schemas/kind)"
        The list of asset kinds that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`PERPETUAL` = 1|the perpetual asset kind|
        |`FUTURE` = 2|the future asset kind|
        |`CALL` = 3|the call option asset kind|
        |`PUT` = 4|the put option asset kind|
        |`STABLE_PERP` = 9|Stable Funding Perp on an RWA underlying, USDC-settled|
    ??? info "[AlgoOrderType](/../../schemas/algo_order_type)"
        Defines the type of an algo order<br>

        |Value| Description |
        |-|-|
        |`CHASE` = 1|CHASE - A post-only limit order that re-prices toward the best bid/ask until filled or cancelled|
    ??? info "[AlgoTriggerFilter](/../../schemas/algo_trigger_filter)"
        Filters algo orders by whether they carry a trigger condition. Leave the filter unset to apply no trigger filter<br>

        |Value| Description |
        |-|-|
        |`WITH_TRIGGER` = 1|WITH_TRIGGER - Only algo orders that carry a trigger and wait for it to cross before becoming active|
        |`WITHOUT_TRIGGER` = 2|WITHOUT_TRIGGER - Only algo orders that have no trigger and become active on creation|
