!!! info "[ApiECNFromBrokerRequest](/../../schemas/api_ecn_from_broker_request)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID of the ECN order|
    |order_id<br>`oi` |string|True|A unique 128-bit identifier for the order, deterministically generated within the GRVT backend|
    |client_order_id<br>`co` |string|True|A unique client order ID for the ECN order|
    |asset<br>`a` |string|True|The asset of the ECN order|
    |seq_no<br>`sn` |string|True|A sequence number used to determine message order for this ECN orders|
    |cumulative_confirmed_size<br>`cc` |string|True|The cumulative confirmed size for this ECN order|
