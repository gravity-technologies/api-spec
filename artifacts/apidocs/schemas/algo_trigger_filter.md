!!! info "[AlgoTriggerFilter](/../../schemas/algo_trigger_filter)"
    Filters algo orders by whether they carry a trigger condition. Leave the filter unset to apply no trigger filter<br>

    |Value| Description |
    |-|-|
    |`WITH_TRIGGER` = 1|WITH_TRIGGER - Only algo orders that carry a trigger and wait for it to cross before becoming active|
    |`WITHOUT_TRIGGER` = 2|WITHOUT_TRIGGER - Only algo orders that have no trigger and become active on creation|
