!!! info "[ApiVaultInvestV2Response](/../../schemas/api_vault_invest_v2_response)"
    Response payload for a vault investment.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |ack<br>`a` |boolean|True|Whether the investment was accepted.|
    |tx_id<br>`ti` |string|True|The transaction ID of the investment once risk confirmed it. 0 when the investment was queued.|
    |enqueued<br>`e` |boolean|False<br>`None`|Cross-exchange vaults only: true when the vault was locked and the investment was queued.|
