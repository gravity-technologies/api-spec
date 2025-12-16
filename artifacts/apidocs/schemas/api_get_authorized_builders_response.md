!!! info "[ApiGetAuthorizedBuildersResponse](/../../schemas/api_get_authorized_builders_response)"
    Returns list of authorized builders and the associated fee<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |results<br>`r` |[ApiAuthorizedBuilder]|True|The list of authorized builders|
    ??? info "[ApiAuthorizedBuilder](/../../schemas/api_authorized_builder)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |builder_account_id<br>`ba` |string|True|The main account ID of the builder|
        |max_futures_fee_rate<br>`mf` |string|True|The maximum fee rate for the authorized builder|
        |max_spot_fee_rate<br>`ms` |string|True|The maximum fee rate for the authorized builder|
