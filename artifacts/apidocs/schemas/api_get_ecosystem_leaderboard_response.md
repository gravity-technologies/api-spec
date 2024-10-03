!!! info "[ApiGetEcosystemLeaderboardResponse](schemas/api_get_ecosystem_leaderboard_response.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |points<br>`p` |[EcosystemPoint]|True|The list of ecosystem points|
    ??? info "[EcosystemPoint](schemas/ecosystem_point.md)"
        <br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |account_id<br>`ai` |string|True|The off chain account id|
        |main_account_id<br>`ma` |string|True|The main account id|
        |total_point<br>`tp` |string|True|Total ecosystem point|
        |direct_invite_count<br>`di` |number|True|Direct invite count|
        |indirect_invite_count<br>`ii` |number|True|Indirect invite count|
        |direct_invite_trading_volume<br>`di1` |string|True|Direct invite trading volume|
        |indirect_invite_trading_volume<br>`ii1` |string|True|Indirect invite trading volume|
        |calculate_at<br>`ca` |string|True|The time when the ecosystem point is calculated|
        |calculate_from<br>`cf` |string|True|Start time of the epoch - phase|
        |calculate_to<br>`ct` |string|True|End time of the epoch - phase|
        |rank<br>`r` |number|True|The rank of the account in the ecosystem|
