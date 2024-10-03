!!! info "[ApiGetLPPointResponse](schemas/api_get_lp_point_response.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |point<br>`p` |ApproximateLPPoint|True|LP points of user|
    |maker_count<br>`mc` |number|True|The number of maker|
    ??? info "[ApproximateLPPoint](schemas/approximate_lp_point.md)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |main_account_id<br>`ma` |string|True|The main account id|
        |liquidity_score<br>`ls` |string|True|Liquidity score|
        |rank<br>`r` |number|True|The rank of user in the LP leaderboard|