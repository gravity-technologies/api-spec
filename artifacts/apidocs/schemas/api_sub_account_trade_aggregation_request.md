!!! info "[ApiSubAccountTradeAggregationRequest](schemas/api_sub_account_trade_aggregation_request.md)"
    startTime are optional parameters. The semantics of these parameters are as follows:<ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |limit<br>`l` |number|True|Optional. The limit of the number of results to return|
    |interval<br>`i` |SubAccountTradeInterval|True|The interval of each sub account trade|
    |sub_account_i_ds<br>`sa` |[string]|True|The list of sub account ids to query|
    |sub_account_id_greater_than<br>`sa1` |string|True|The sub account id to query greater than|
    |start_interval<br>`si` |string|True|Optional. The starting time in unix nanoseconds of a specific interval to query|
    |start_time<br>`st` |string|False<br>`0`|Optional. Start time in unix nanoseconds|
    |end_time<br>`et` |string|False<br>`now()`|Optional. End time in unix nanoseconds|
    |cursor<br>`c` |string|False<br>``|The cursor to indicate when to start the next query from|
    ??? info "[SubAccountTradeInterval](schemas/sub_account_trade_interval.md)"
        |Value| Description |
        |-|-|
        |`SAT_1_MO` = 1|1 month|
        |`SAT_1_D` = 2|1 day|
