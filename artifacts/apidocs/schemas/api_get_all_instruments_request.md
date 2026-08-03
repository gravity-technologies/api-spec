!!! info "[ApiGetAllInstrumentsRequest](/../../schemas/api_get_all_instruments_request)"
    Fetch all instruments<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |is_active<br>`ia` |boolean|False<br>`false`|Fetch only active instruments|
    |kinds<br>`k` |[Kind]|False<br>`['PERPETUAL']`|The kind filter to apply. If empty, this defaults to PERPETUAL only. Otherwise, only entries matching the filter will be returned|
    ??? info "[Kind](/../../schemas/kind)"
        The list of asset kinds that are supported on the GRVT exchange<br>

        |Value| Description |
        |-|-|
        |`PERPETUAL` = 1|the perpetual asset kind|
        |`FUTURE` = 2|the future asset kind|
        |`CALL` = 3|the call option asset kind|
        |`PUT` = 4|the put option asset kind|
        |`STABLE_PERP` = 9|Stable Funding Perp on an RWA underlying, USDC-settled|
