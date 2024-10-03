!!! info "[ApiGetLatestLPSnapshotResponse](schemas/api_get_latest_lp_snapshot_response.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |snapshot<br>`s` |ApproximateLPSnapshot|True|The latest LP snapshot|
    ??? info "[ApproximateLPSnapshot](schemas/approximate_lp_snapshot.md)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |main_account_id<br>`ma` |string|True|The main account id|
        |underlying_multiplier<br>`um` |string|True|Underlying multiplier|
        |market_share_multiplier<br>`ms` |string|True|Market share multiplier|
        |bid_fast_market_multiplier<br>`bf` |number|True|Fast market multiplier|
        |ask_fast_market_multiplier<br>`af` |number|True|Fast market multiplier|
        |liquidity_score<br>`ls` |string|True|Liquidity score|
        |calculate_at<br>`ca` |string|True|The time when the snapshot was calculated|
