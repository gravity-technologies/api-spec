!!! info "[Source](/../../schemas/source)"
    Defines the source of the order or trade, such as a UI, API, or a bot.<br>This is used to track the source of the order, and is not signed by the client<br>

    |Value| Description |
    |-|-|
    |`WEB` = 1|The order/trade was created by a web client|
    |`MOBILE` = 2|The order/trade was created by a mobile client|
    |`API` = 3|The order/trade was created by an API client|
    |`LIQUIDATOR` = 4|The order/trade was created by the liquidator service|
