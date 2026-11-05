!!! info "[ApiQualifiedMakerFundingRateSubmissionHistoryRequest](/../../schemas/api_qualified_maker_funding_rate_submission_history_request)"
    Query the caller's accepted qualified maker funding rate submissions, newest first. Rejected submissions are not stored; their reason is in the submit response.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |start_time<br>`st` |string|False<br>`0`|The start time in unix nanoseconds|
    |end_time<br>`et` |string|False<br>`now()`|The end time in unix nanoseconds|
    |limit<br>`l` |integer|False<br>`500`|The limit to query for. Defaults to 500; Max 1000|
    |cursor<br>`c` |string|False<br>`''`|The cursor to indicate when to start the query from|
