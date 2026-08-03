!!! info "[ApiSetIndicativePricesRequest](/../../schemas/api_set_indicative_prices_request)"
    Submit a two-sided indicative price for an instrument. Only sub accounts whose main account is an approved qualified maker or designated market maker for the instrument may submit; others are rejected. Both sides are mandatory and bid must be strictly below ask. The quote carries a fixed 60-second TTL and replaces this sub account's previous quote for the instrument.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account submitting the indicative price. Must belong to the authenticated session.|
    |instrument<br>`i` |string|True|The instrument the indicative price is for|
    |bid<br>`b` |string|True|Indicative bid price, expressed in 9 decimals. Must be > 0 and strictly below ask|
    |ask<br>`a` |string|True|Indicative ask price, expressed in 9 decimals. Must be strictly above bid|
