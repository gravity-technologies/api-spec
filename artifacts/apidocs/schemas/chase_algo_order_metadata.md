!!! info "[ChaseAlgoOrderMetadata](/../../schemas/chase_algo_order_metadata)"
    Contains the parameters of a chase algo order.<ul><li>`chase_price_mode` defines how the price is derived at each re-price.</li><li>`max_distance` caps how far the chase price may move away from the reference price. Once the cap is reached, the order is held at the boundary instead of chasing further.</li></ul><br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |chase_price_mode<br>`cp` |ChasePriceMode|True|How the chase price is determined at each re-price tick|
    |max_distance<br>`md` |string|True|The maximum distance the chase price can move away from the reference price, as an absolute price distance in quote currency units, expressed in `9` decimals.<br>Always absolute: when the user picks a percentage, the client converts it and sends the result here.|
    |max_distance_bps<br>`md1` |integer|False<br>`0`|The max distance as a percentage in basis points (1 bp = 0.01%, 100% = 10000), as the user entered it. `0` if the user entered an absolute distance.<br>Informational only, for display and history. `maxDistance` is what is enforced.|
    ??? info "[ChasePriceMode](/../../schemas/chase_price_mode)"
        Defines how a chase order determines its price at each re-price tick<br>

        |Value| Description |
        |-|-|
        |`BEST_BID_ASK` = 1|BEST_BID_ASK - The chase price equals the best bid (buy) or best ask (sell)|
