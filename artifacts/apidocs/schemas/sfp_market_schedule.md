!!! info "[SfpMarketSchedule](/../../schemas/sfp_market_schedule)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sessions<br>`s` |[TradingSession]|True|Trading sessions for the current calendar week (Sunday to Saturday in the exchange's local time). The sessions are contiguous with no gaps, and any period when the market is not open, including holidays falling in this week, is returned as a `CLOSE` session|
    |holidays<br>`h` |[TradingHolidaySchedule]|True|Market holidays and early closes, past and upcoming, sorted by start time. The market is closed from the start time to the end time of each entry. Empty when there are none|
    ??? info "[TradingSession](/../../schemas/trading_session)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |start_time<br>`st` |string|True|Trading session start time timestamp in milliseconds|
        |end_time<br>`et` |string|True|Trading session end time timestamp in milliseconds|
        |type<br>`t` |TradingSessionType|True|Trading session type|
        ??? info "[TradingSessionType](/../../schemas/trading_session_type)"
            Specifies different types of trading sessions<br>

            |Value| Description |
            |-|-|
            |`REGULAR` = 1|Core market hours. Full liquidity.|
            |`PRE_MARKET` = 2|Extended hours before open. Lower liquidity.|
            |`AFTER_MARKET` = 3|Extended hours after close. Lower liquidity.|
            |`OVERNIGHT` = 4|For 24/5 or specific overnight TradFi perps. Minimal liquidity.|
            |`CLOSE` = 5|Weekends, holidays, or daily maintenance windows.|
    ??? info "[TradingHolidaySchedule](/../../schemas/trading_holiday_schedule)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |name<br>`n` |string|True|Holiday name|
        |close_type<br>`ct` |TradingScheduleCloseType|True|`FULL_DAY`: the market is closed for the whole day. `EARLY_CLOSE`: the market trades as normal until the start time, then is closed until the end time|
        |start_time<br>`st` |string|True|When the closure begins, as a Unix timestamp in milliseconds. For `FULL_DAY` this is when the closed trading day's session would have opened (the evening before for a session that opens before midnight); for `EARLY_CLOSE` it is the moment the market closes early|
        |end_time<br>`et` |string|True|When the closed or shortened trading day's session would have closed, as a Unix timestamp in milliseconds. The closure covers the start time up to, but not including, the end time|
        ??? info "[TradingScheduleCloseType](/../../schemas/trading_schedule_close_type)"
            How the market behaves on a holiday date<br>

            |Value| Description |
            |-|-|
            |`FULL_DAY` = 1|Market is fully closed for the entire day|
            |`EARLY_CLOSE` = 2|Market closes early; see the earlyClose time|
