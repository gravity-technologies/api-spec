!!! info "[ApiGetMarginRulesResponse](/../../schemas/api_get_margin_rules_response)"
    API response payload for margin rules of a particular instrument<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |instrument<br>`i` |string|True|The instrument name|
    |max_position_size<br>`mp` |string|True|The maximum position size, expressed in base asset decimal units|
    |risk_brackets<br>`rb` |[RiskBracket]|True|List of risk brackets defining margin requirements at different notional tiers|
    ??? info "[RiskBracket](/../../schemas/risk_bracket)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |tier<br>`t` |integer|True|1-indexed tier number|
        |notional_floor<br>`nf` |string|True|Lower bound of notional value (inclusive) in quote currency|
        |notional_cap<br>`nc` |string|False<br>`None`|Upper bound of notional value (exclusive) in quote currency, omitted for last tier|
        |maintenance_margin_rate<br>`mm` |string|True|Maintenance margin rate as a decimal (e.g., '0.01' for 1%)|
        |initial_margin_rate<br>`im` |string|True|Initial margin rate as a decimal (e.g., '0.02' for 2%)|
        |max_leverage<br>`ml` |integer|True|Maximum leverage allowed at this tier (floor of 1 / initial_margin_rate)|
        |cumulative_maintenance_amount<br>`cm` |string|True|Cumulative maintenance margin amount in quote currency|
