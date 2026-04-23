!!! info "[ApiPositionHistoryRequest](/../../schemas/api_position_history_request)"
    Query for position lifecycle records for a single sub account.<br><br>Returns both fully closed positions and positions that are still open but have been partially reduced (`PARTIALLY_CLOSED`).<br><br>Results are ordered as follows: partially closed positions (most recently opened first), then fully closed positions (most recently closed first).<br><br>Partially closed positions are included only when all of the following are true:<ul><li>`start_time` is unset (partially closed positions have no close time)</li><li>`end_time` is unset (partially closed positions have no close time)</li><li>`cursor` is unset (they are only returned on the initial page)</li><li>`status` is nil or includes `PARTIALLY_CLOSED`</li></ul>Since these positions have no close time, query-row limits, as well as time-range and cursor-based pagination, do not apply to them.<br><br>Pagination works as follows:<ul><li>We perform a reverse chronological lookup by position-close time, starting from `end_time`. If `end_time` is not set, we start from the most recent data.</li><li>The lookup is limited to `limit` records. If more data is requested, the response will contain a `next` cursor for you to query the next page.</li><li>If a `cursor` is provided, it will be used to fetch results from that point onwards.</li><li>Pagination will continue until the `start_time` is reached. If `start_time` is not set, pagination will continue as far back as our data retention policy allows.</li></ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID to request for|
    |start_time<br>`st` |string|False<br>`0`|Start of the close-time range in unix nanoseconds. If nil, defaults to no lower bound. Only positions with close_time >= start_time are returned. Does not apply to partially closed positions (they have no close time and will be excluded when this field is set)|
    |end_time<br>`et` |string|False<br>`now()`|End of the close-time range in unix nanoseconds. If nil, defaults to now. Only positions with close_time <= end_time are returned. Does not apply to partially closed positions (they have no close time and will be excluded when this field is set)|
    |kind<br>`k` |[Kind]|False<br>`all`|The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only positions matching the filter will be returned|
    |base<br>`b` |[string]|False<br>`all`|The base filter to apply. If nil, this defaults to all bases. Otherwise, only positions matching the filter will be returned|
    |quote<br>`q` |[string]|False<br>`all`|The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only positions matching the filter will be returned|
    |limit<br>`l` |integer|False<br>`500`|The limit to query for. Defaults to 500; Max 1000. Applies to fully closed positions only; limit excludes any matching partially-closed positions|
    |cursor<br>`c` |string|False<br>`''`|The cursor to indicate when to start the next page query from. Partially closed positions are only returned on the initial page (when cursor is unset)|
    |status<br>`s` |[PositionCloseStatus]|False<br>`all`|The status filter to apply. If nil, this defaults to all statuses. Otherwise, only positions matching the filter will be returned|
    |is_long<br>`il` |boolean|False<br>`false`|Set to true to filter for long positions. If both is_long and is_short are false (default), positions of both directions are returned|
    |is_short<br>`is` |boolean|False<br>`false`|Set to true to filter for short positions. If both is_long and is_short are false (default), positions of both directions are returned|
    |margin_type<br>`mt` |[PositionMarginType]|False<br>`all`|The margin type filter to apply. If nil, this defaults to all margin types. Otherwise, only positions matching the filter will be returned|
    ??? info "[Kind](/../../schemas/kind)"
        The list of asset kinds that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`PERPETUAL` = 1|the perpetual asset kind|
        |`FUTURE` = 2|the future asset kind|
        |`CALL` = 3|the call option asset kind|
        |`PUT` = 4|the put option asset kind|
        |`SPOT_SWAP` = 8|the spot swap asset kind|
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
