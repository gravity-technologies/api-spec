!!! info "[ApiVaultConversionRateRequest](/../../schemas/api_vault_conversion_rate_request)"
    Request payload for the highest exchange rate the gateway currently accepts for a vault investment or redemption that converts `fromCurrency` into `toCurrency`.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |from_currency<br>`fc` |string|True|The currency converted from.|
    |to_currency<br>`tc` |string|True|The currency converted into.|
    |from_num_tokens<br>`fn` |string|False<br>`0`|Optional amount of `fromCurrency`. When set, the response estimates what it converts into.|
