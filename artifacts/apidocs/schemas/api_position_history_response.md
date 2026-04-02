!!! info "[ApiPositionHistoryResponse](/../../schemas/api_position_history_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |[ApiPositionHistory]|True|Position lifecycle records matching the request filters. Partially closed positions appear first (most recently opened first), followed by fully closed positions (most recently closed first)|
    |next<br>`n` |string|True|The cursor to indicate when to start the query from|
    ??? info "[ApiPositionHistory](/../../schemas/api_position_history)"
        A position lifecycle record.<br><br>When status is `PARTIALLY_CLOSED`, the position is still open. Fields that describe the close event (`close_time`, `position_close_mark_price`) will be omitted, and `leverage` reflects the current value<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |sub_account_id<br>`sa` |string|True|Trading account ID which held this position|
        |instrument<br>`i` |string|True|Asset this position was for|
        |open_time<br>`ot` |string|True|Timestamp of first trade that opened this lifecycle|
        |status<br>`s` |PositionCloseStatus|True||
        |is_long<br>`il` |boolean|True|True if the closed position was long|
        |margin_type<br>`mt` |PositionMarginType|True||
        |close_time<br>`ct` |string|False<br>`None`|Timestamp when the position lifecycle ended. Omitted when status is `PARTIALLY_CLOSED`|
        |entry_price<br>`ep` |string|True|Average entry price at 9 decimals|
        |exit_price<br>`ep1` |string|True|Average exit price at 9 decimals|
        |position_close_mark_price<br>`pc` |string|False<br>`None`|Mark price at close. Omitted when status is `PARTIALLY_CLOSED`|
        |realized_pnl<br>`rp` |string|True|Cumulative realized PnL in quote currency|
        |cumulative_fee<br>`cf` |string|True|Cumulative fees in quote currency|
        |cumulative_realized_funding_payment<br>`cr` |string|True|Cumulative realized funding payment in quote currency|
        |closed_volume_base<br>`cv` |string|True|Sum of abs(reducingTradeSize) across all reducing trades|
        |closed_volume_quote<br>`cv1` |string|True|Sum of abs(reducingTradeSize) * tradePrice across all reducing trades|
        |max_open_interest_base<br>`mo` |string|True|Max absolute position size reached during lifecycle|
        |max_open_interest_quote<br>`mo1` |string|True|Max abs(size) * entryVWAP reached during lifecycle|
        |cumulative_initial_margin<br>`ci` |string|True|Sum of markPrice * abs(tradeSize) / leverage for position-increasing trades|
        |max_initial_margin<br>`mi` |string|True|High-water mark of cumulativeInitialMargin during lifecycle|
        |leverage<br>`l` |string|True|Leverage at time of close. When status is `PARTIALLY_CLOSED`, this is the current leverage|
        |unrealized_pnl<br>`up` |string|False<br>`None`|The unrealized PnL of the position, expressed in quote asset decimal units<br>`unrealized_pnl = (mark_price - entry_price) * size` where `size` is signed (negative for short positions)<br>Only present when status is `PARTIALLY_CLOSED`|
        ??? info "[PositionCloseStatus](/../../schemas/position_close_status)"
            |Value| Description |
            |-|-|
            |`CLOSED` = 1|Position fully closed via reducing trade or flip|
            |`LIQUIDATED` = 2|Position closed via liquidation|
            |`SETTLED` = 3|Position closed via settlement|
            |`PARTIALLY_CLOSED` = 4|Position partially closed|
        ??? info "[PositionMarginType](/../../schemas/position_margin_type)"
            |Value| Description |
            |-|-|
            |`ISOLATED` = 1|Isolated Margin Mode: each position is allocated a fixed amount of collateral|
            |`CROSS` = 2|Cross Margin Mode: uses all available funds in your account as collateral across all cross margin positions|
