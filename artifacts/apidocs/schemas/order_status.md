!!! info "[OrderStatus](/../../schemas/order_status)"
    |Value| Description |
    |-|-|
    |`PENDING` = 1|Order is waiting for Trigger Condition to be hit|
    |`OPEN` = 2|Order is actively matching on the orderbook, could be unfilled or partially filled|
    |`FILLED` = 3|Order is fully filled and hence closed|
    |`REJECTED` = 4|Order is rejected by GRVT Backend since if fails a particular check (See OrderRejectReason)|
    |`CANCELLED` = 5|Order is cancelled by the user using one of the supported APIs (See OrderRejectReason)|
