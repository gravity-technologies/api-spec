!!! info "[ApiCrossExchVaultLockRequest](/../../schemas/api_cross_exch_vault_lock_request)"
    Request payload for a cross-exchange vault manager to engage the update lock for their vault.<br><br>While locked, all operations that could change the vault's share count (e.g. invest / redeem / burn) become disabled.<br><br>Should be done prior to an equity-attest update to ensure a fixed-reference share count.<br><br>WARN: Stays locked until the corresponding Unlock API is called, OR a successful equity-attest update.<br><br>Vault managers leaving their vaults locked for prolonged periods will receive GRVT warning alerts.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |cross_exch_vault_id<br>`ce` |string|True|The unique identifier of the cross-exchange vault to lock.|
