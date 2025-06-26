!!! info "[ApiVaultViewRedemptionQueueResponse](/../../schemas/api_vault_view_redemption_queue_response)"
    Response payload for a vault manager to view the redemption queue for their vault, ordered by descending priority.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |redemption_queue<br>`rq` |[VaultRedemptionReqView]|True|Representation of a pending vault redemption request.|
    ??? info "[VaultRedemptionReqView](/../../schemas/vault_redemption_req_view)"
        Representation of a pending redemption request for a given vault.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_time<br>`rt` |string|True|[Filled by GRVT Backend] Time at which the redemption request was received by GRVT in unix nanoseconds|
        |currency<br>`c` |string|True|The currency to redeem in|
        |num_lp_tokens<br>`nl` |string|True|The number of LP tokens to redeem|
        |max_redemption_period_timestamp<br>`mr` |string|True|[Filled by GRVT Backend] Time in unix nanoseconds, beyond which the request will be force-redeemed.|
