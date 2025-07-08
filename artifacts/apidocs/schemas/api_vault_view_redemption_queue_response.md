!!! info "[ApiVaultViewRedemptionQueueResponse](/../../schemas/api_vault_view_redemption_queue_response)"
    Response payload for a vault manager to view the redemption queue for their vault, ordered by descending priority.<br><br>Excludes requests that have not yet aged past the minmimum redemption period.<br><br>Also includes counters for total redemption sizes pending as well as urgent (refer to API integration guide for more detail on redemption request classifications).<br><br><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |redemption_queue<br>`rq` |[VaultRedemptionReqView]|True|Outstanding vault redemption requests, ordered by descending priority. Excludes requests that have not yet aged past the minmimum redemption period.|
    |pending_redemption_token_count<br>`pr` |string|True|Number of LP Tokens pending redemption (at least held in queue for minimum redemption period).|
    |urgent_redemption_token_count<br>`ur` |string|True|Number of LP Tokens due for urgent redemption (>= 90% of maximum redemption period).|
    |auto_redeemable_balance_vault_quote_cur<br>`ar` |string|True|Amount available for automated redemption request servicing, expressed in terms of the vault's quote currency.|
    |currency<br>`c` |string|True|This vault's quote currency.|
    ??? info "[VaultRedemptionReqView](/../../schemas/vault_redemption_req_view)"
        Representation of a pending redemption request for a given vault.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_time<br>`rt` |string|True|[Filled by GRVT Backend] Time at which the redemption request was received by GRVT in unix nanoseconds|
        |currency<br>`c` |string|True|The currency to redeem in|
        |num_lp_tokens<br>`nl` |string|True|The number of LP tokens to redeem|
        |max_redemption_period_timestamp<br>`mr` |string|True|[Filled by GRVT Backend] Time in unix nanoseconds, beyond which the request will be force-redeemed.|
