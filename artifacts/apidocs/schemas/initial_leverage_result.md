!!! info "[InitialLeverageResult](/../../schemas/initial_leverage_result)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |instrument<br>`i` |string|True|The instrument to get the leverage for|
    |leverage<br>`l` |string|True|The initial leverage of this instrument|
    |min_leverage<br>`ml` |string|True|The min leverage user can set for this instrument|
    |max_leverage<br>`ml1` |string|True|The max leverage user can set for this instrument|
    |margin_type<br>`mt` |PositionMarginType|True|The margin type of this instrument|
    ??? info "[PositionMarginType](/../../schemas/position_margin_type)"
        |Value| Description |
        |-|-|
        |`ISOLATED` = 1|Isolated Margin Mode: each position is allocated a fixed amount of collateral|
        |`CROSS` = 2|Cross Margin Mode: uses all available funds in your account as collateral across all cross margin positions|
