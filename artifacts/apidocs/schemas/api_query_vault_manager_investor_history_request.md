!!! info "[ApiQueryVaultManagerInvestorHistoryRequest](/../../schemas/api_query_vault_manager_investor_history_request)"
    Request for the manager to retrieve the vault investor history for their vault<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |vault_id<br>`vi` |string|True|The unique identifier of the vault to filter by|
    |only_own_investments<br>`oo` |boolean|True|Whether to only return investments made by the manager|
    |start_time<br>`st` |string|False<br>`0`|Optional. Start time in unix nanoseconds|
    |end_time<br>`et` |string|False<br>`now()`|Optional. End time in unix nanoseconds|
