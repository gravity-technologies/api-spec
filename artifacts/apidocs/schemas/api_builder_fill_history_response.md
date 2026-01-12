!!! info "[ApiBuilderFillHistoryResponse](/../../schemas/api_builder_fill_history_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |[BuilderFillHistory]|True|The builder fill history matching the request builder account|
    |next<br>`n` |string|False<br>`''`|The cursor to indicate when to start the next query from|
    ??? info "[BuilderFillHistory](/../../schemas/builder_fill_history)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
        |off_chain_account_id<br>`oc` |string|True|The off chain account id|
        |instrument<br>`i` |string|True|The instrument being represented|
        |is_buyer<br>`ib` |boolean|True|The side that the subaccount took on the trade|
        |is_taker<br>`it` |boolean|True|The role that the subaccount took on the trade|
        |size<br>`s` |string|True|The number of assets being traded, expressed in base asset decimal units|
        |price<br>`p` |string|True|The traded price, expressed in `9` decimals|
        |mark_price<br>`mp` |string|True|The mark price of the instrument at point of trade, expressed in `9` decimals|
        |index_price<br>`ip` |string|True|The index price of the instrument at point of trade, expressed in `9` decimals|
        |fee_rate<br>`fr` |string|True|Builder fee percentage charged for this order. referred to Order.builder builderFee |
        |fee<br>`f` |string|True|The builder fee paid on the trade, expressed in quote asset decimal unit. referred to Trade.builderFee|
