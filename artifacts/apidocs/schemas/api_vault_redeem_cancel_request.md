!!! info "[ApiVaultRedeemCancelRequest](/../../schemas/api_vault_redeem_cancel_request)"
    Request payload for canceling a vault redemption.<br><br>This API allows a client to cancel a previously initiated redemption from a vault.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |main_account_id<br>`ma` |string|True|The address of the main account initiating the cancellation.|
    |vault_id<br>`vi` |string|True|The unique identifier of the vault to cancel the redemption from.|
