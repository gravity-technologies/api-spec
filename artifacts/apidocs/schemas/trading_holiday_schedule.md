!!! info "[TradingHolidaySchedule](/../../schemas/trading_holiday_schedule)"
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
