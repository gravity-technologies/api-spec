!!! info "[ApiCrossExchVaultViewInvestmentQueueResponse](/../../schemas/api_cross_exch_vault_view_investment_queue_response)"
    Response payload for a cross-exchange vault manager to view the investment queue for their vault in FIFO order.<br><br>This queue gets drained on every equity attestation event submitted by the cross-exchange vault manager.<br><br><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |investment_queue<br>`iq` |[CrossExchVaultPendingInvestment]|True|Outstanding cross-exchange vault investment requests in FIFO order.|
    |total_investment_equity<br>`ti` |string|True|The current valuation (in USD) of all pending investments.|
    ??? info "[CrossExchVaultPendingInvestment](/../../schemas/cross_exch_vault_pending_investment)"
        Representation of a pending investment for a given cross-exchange vault.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_time<br>`rt` |string|True|[Filled by GRVT Backend] Time at which the investment request was confirmed and enqueued by GRVT in unix nanoseconds|
        |currency<br>`c` |string|True|The currency used for the investment. This should be the vault's quote currency.|
        |num_tokens<br>`nt` |string|True|The investment sum, in terms of the token currency specified (i.e., `numTokens` of '1000' with `tokenCurrency` of 'USDT' denotes investment of 1,000 USDT).|
        |is_manager<br>`im` |boolean|False<br>`None`|`true` if this pending investment belongs to the vault manager, omitted otherwise.|
