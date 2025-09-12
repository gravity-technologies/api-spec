!!! info "[ApiCrossExchVaultViewInvestmentQueueRequest](/../../schemas/api_cross_exch_vault_view_investment_queue_request)"
    Request payload for a cross-exchange vault manager to view the investment queue for their vault in FIFO order.<br><br>This queue gets drained on every equity attestation event submitted by the cross-exchange vault manager.<br><br><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |vault_id<br>`vi` |string|True|The unique identifier of the cross-exchange vault to fetch the investment queue for.|
