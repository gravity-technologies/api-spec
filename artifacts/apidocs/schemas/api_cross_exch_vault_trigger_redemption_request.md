!!! info "[ApiCrossExchVaultTriggerRedemptionRequest](/../../schemas/api_cross_exch_vault_trigger_redemption_request)"
    Request payload for a cross-exchange vault manager to trigger execution of the redemption request at the head of their cross-exchange vault's redemption queue.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |vault_id<br>`vi` |string|True|The unique identifier of the cross-exchange vault to redeem from.|
    |request_time<br>`rt` |string|True|Value provided must be equal to the `request_time` field of the first element returned from the View Investment Queue API.|
