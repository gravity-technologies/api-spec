!!! info "[ApiFindTraderEpochMetricResponse](schemas/api_find_trader_epoch_metric_response.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |metric<br>`m` |TraderMetric|True|Phase zero metric|
    |rank<br>`r` |number|True|The rank of the account in the trader|
    |total<br>`t` |number|True|The total number of accounts in the trader|
    |last_calculated_at<br>`lc` |string|True|The time when the trader points were last calculated|
    ??? info "[TraderMetric](schemas/trader_metric.md)"
        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |total_fee<br>`tf` |string|True|Total fee paid|
        |total_point<br>`tp` |string|True|Total trader point of this epoch/phase|