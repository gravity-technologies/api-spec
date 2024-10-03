!!! info "[ApiGetLPLeaderboardResponse](/../../schemas/api_get_lp_leaderboard_response)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |points<br>`p` |[LPPoint]|True|The list of LP points|
    ??? info "[LPPoint](/../../schemas/lp_point)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |main_account_id<br>`ma` |string|True|The main account id|
        |lp_asset<br>`la` |string|True|The LP Asset|
        |start_interval<br>`si` |string|True|Start time of the epoch - phase|
        |liquidity_score<br>`ls` |string|True|Liquidity score|
        |rank<br>`r` |number|True|The rank of user in the LP leaderboard|
