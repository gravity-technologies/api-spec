!!! info "[InternalPreOrderMarginCheckRequest](/../../schemas/internal_pre_order_margin_check_request)"
    Pre-order margin check to determine if a new order can be created for a given sub-account<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub-account for which the order is being evaluated|
    |open_order_legs<br>`oo` |[OrderLeg]|True|Open orders created by this sub-account|
    |new_order_legs<br>`no` |[OrderLeg]|True|New orders this sub-account is attempting to create|
    ??? info "[OrderLeg](/../../schemas/order_leg)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The instrument to trade in this leg|
        |size<br>`s` |string|True|The total number of assets to trade in this leg, expressed in base asset decimal units.|
        |limit_price<br>`lp` |string|False<br>`0`|The limit price of the order leg, expressed in `9` decimals.<br>This is the number of quote currency units to pay/receive for this leg.<br>This should be `null/0` if the order is a market order|
        |is_buying_asset<br>`ib` |boolean|True|Specifies if the order leg is a buy or sell|
    ??? info "[OrderLeg](/../../schemas/order_leg)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |instrument<br>`i` |string|True|The instrument to trade in this leg|
        |size<br>`s` |string|True|The total number of assets to trade in this leg, expressed in base asset decimal units.|
        |limit_price<br>`lp` |string|False<br>`0`|The limit price of the order leg, expressed in `9` decimals.<br>This is the number of quote currency units to pay/receive for this leg.<br>This should be `null/0` if the order is a market order|
        |is_buying_asset<br>`ib` |boolean|True|Specifies if the order leg is a buy or sell|
