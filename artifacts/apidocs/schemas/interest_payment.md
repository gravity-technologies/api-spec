!!! info "[InterestPayment](/../../schemas/interest_payment)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |event_time<br>`et` |string|True|Time at which the interest charge was computed in unix nanoseconds|
    |sub_account_id<br>`sa` |string|True|The sub-account being charged interest|
    |currency<br>`c` |string|True|The currency the interest is charged in|
    |amount<br>`a` |string|True|The interest charged for this hour.|
    |charge_time<br>`ct` |string|True|The last interest charge time accumulated to this amount (HH:05 tick).|
    |borrowed_amount<br>`ba` |string|True|The borrowed principal in this currency that the hourly interest was computed on.|
