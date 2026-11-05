!!! info "[InstrumentStatus](/../../schemas/instrument_status)"
    The lifecycle/trading status of an instrument on the GRVT exchange<br>

    |Value| Description |
    |-|-|
    |`ACTIVE` = 1|Instrument is fully tradable|
    |`REDUCE_ONLY` = 2|Only position-reducing orders are accepted (e.g. pre-delist wind-down)|
    |`MAINTENANCE` = 3|Trading is temporarily paused for scheduled maintenance; cancel-only|
    |`HALTED` = 4|Underlying halted at its primary market (LULD, news pending); index and mark frozen|
    |`CLOSED` = 5|Outside trading window: daily maintenance break, weekend, holiday; cancel-only|
    |`PENDING` = 6|Instrument is created but not yet open for trading (pre-listing)|
    |`DELISTED` = 7|Instrument has been permanently removed|
