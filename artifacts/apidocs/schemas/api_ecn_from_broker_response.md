!!! info "[ApiECNFromBrokerResponse](/../../schemas/api_ecn_from_broker_response)"
    Acknowledges that the broker confirmation passed validation and was accepted for processing.<br>Acceptance does not mean the confirmed size has been matched — the resulting order updates are<br>published on the `v1.ecn_to_broker` and order streams. Any failure is returned as an error response<br>instead of this payload.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |result<br>`r` |boolean|True|`true` when the confirmation was accepted for processing|
