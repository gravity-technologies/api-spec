!!! info "[ApiTransferHistoryRequest](/../../schemas/api_transfer_history_request)"
    The request to get the historical transfers of an account<br>The history is returned in reverse chronological order<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |currency<br>`c` |[string]|True|The token currency to query for, if nil or empty, return all transfers. Otherwise, only entries matching the filter will be returned|
    |start_time<br>`st` |string|False<br>`0`|The start time to query for in unix nanoseconds|
    |end_time<br>`et` |string|False<br>`now()`|The end time to query for in unix nanoseconds|
    |limit<br>`l` |integer|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
    |cursor<br>`c1` |string|False<br>`''`|The cursor to indicate when to start the next query from|
    |tx_id<br>`ti` |string|False<br>`0`|The transaction ID to query for|
    |main_account_id<br>`ma` |string|False<br>``|Main account ID being queried. By default, applies the requestor's main account ID.|
    |transfer_types<br>`tt` |[TransferType]|False<br>`[]`|The transfer type to filters for. If the list is empty, return all transfer types.|
    ??? info "[TransferType](/../../schemas/transfer_type)"
        |Value| Description |
        |-|-|
        |`UNSPECIFIED` = 0|Default transfer that has nothing to do with bridging|
        |`STANDARD` = 1|Standard transfer that has nothing to do with bridging|
        |`FAST_ARB_DEPOSIT` = 2|Fast Arb Deposit Metadata type|
        |`FAST_ARB_WITHDRAWAL` = 3|Fast Arb Withdrawal Metadata type|
        |`NON_NATIVE_BRIDGE_DEPOSIT` = 4|Transfer type for non native bridging deposit|
        |`NON_NATIVE_BRIDGE_WITHDRAWAL` = 5|Transfer type for non native bridging withdrawal|
        |`ADHOC_INCENTIVE` = 6|Transfer type for adhoc incentive|
        |`REFERRAL_INCENTIVE` = 7|Transfer type for referral incentive|
        |`TRADING_DEPOSIT_YIELD_INCENTIVE` = 8|Transfer type for trading deposit yield incentive|
