!!! info "[ApiTransferHistoryRequest](/../../schemas/api_transfer_history_request)"
    The request to get the historical transfers of an account<br>The history is returned in reverse chronological order<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records (default 500, max 1000). If more data matches, the response returns a non-empty `next` cursor. To read the full result set you MUST re-issue the request with `cursor` set to that value and keep looping until `next` is empty.</li><li><b>A single call silently truncates at `limit` and returns no error.</b> Callers that read only the first page (or omit `limit`, which just applies the 500 default) will undercount whenever the account has more than `limit` matching records — e.g. summing deposits/transfers for a balance or PnL calculation must drain the cursor, not read one page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |currency<br>`c` |[string]|True|The token currency to query for, if nil or empty, return all transfers. Otherwise, only entries matching the filter will be returned|
    |start_time<br>`st` |string|False<br>`0`|The start time to query for in unix nanoseconds|
    |end_time<br>`et` |string|False<br>`now()`|The end time to query for in unix nanoseconds|
    |limit<br>`l` |integer|False<br>`500`|The page size for a single response. Defaults to 500; Max 1000. This caps one page only — omitting it does NOT return everything, it applies the 500 default. To get the full result set, follow the `next` cursor until it is empty.|
    |cursor<br>`c1` |string|False<br>`''`|The cursor to indicate when to start the next query from|
    |tx_id<br>`ti` |string|False<br>`0`|The transaction ID to query for|
    |main_account_id<br>`ma` |string|False<br>``|Main account ID being queried. By default, applies the requestor's main account ID.|
    |transfer_types<br>`tt` |[TransferType]|False<br>`[]`|The transfer type to filters for. If the list is empty, return all transfer types.|
    ??? info "[TransferType](/../../schemas/transfer_type)"
        |Value| Description |
        |-|-|
        |`UNSPECIFIED` = 0|Deprecated: use `standard` instead. Legacy value for transfers created before transfer types were introduced.|
        |`STANDARD` = 1|Standard transfer that has nothing to do with bridging|
        |`FAST_ARB_DEPOSIT` = 2|Fast Arb Deposit Metadata type|
        |`FAST_ARB_WITHDRAWAL` = 3|Fast Arb Withdrawal Metadata type|
        |`NON_NATIVE_BRIDGE_DEPOSIT` = 4|Transfer type for non native bridging deposit|
        |`NON_NATIVE_BRIDGE_WITHDRAWAL` = 5|Transfer type for non native bridging withdrawal|
        |`ADHOC_INCENTIVE` = 6|Transfer type for adhoc incentive|
        |`REFERRAL_INCENTIVE` = 7|Transfer type for referral incentive|
        |`TRADING_DEPOSIT_YIELD_INCENTIVE` = 8|Transfer type for trading deposit yield incentive|
