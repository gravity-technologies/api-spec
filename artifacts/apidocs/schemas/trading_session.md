!!! info "[TradingSession](/../../schemas/trading_session)"
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
