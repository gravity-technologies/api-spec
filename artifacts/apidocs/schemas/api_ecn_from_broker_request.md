!!! info "[ApiECNFromBrokerRequest](/../../schemas/api_ecn_from_broker_request)"
    Reports the size a broker has confirmed for an ECN order, in response to the size requested<br>on the `v1.ecn_to_broker` stream.<br>- The target order is identified by `order_id` or `client_order_id`. At least one must be provided;<br>  if both are provided, they must refer to the same order, and `instrument` must match that order.<br>- `cumulative_confirmed_size` is an absolute running total for the order. Resending a<br>  smaller or equal value has no effect, so the request is safe to retry.<br>- `seq_no` echoes the `v1.ecn_to_broker` message being confirmed and must not be ahead of the latest<br>  sequence number GRVT published for this order.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The sub account ID that owns the ECN order being confirmed. Must match the sub account of the referenced order|
    |order_id<br>`oi` |string|True|A unique identifier for the order, generated within the GRVT backend. Required unless `client_order_id` is provided|
    |client_order_id<br>`co` |string|True|The client-specified identifier of the ECN order within the sub account. Required unless `order_id` is provided|
    |asset<br>`a` |string|True|The instrument of the ECN order. Must match the instrument of the referenced order|
    |seq_no<br>`sn` |string|True|The `seq_no` of the `v1.ecn_to_broker` message this confirmation responds to. A value ahead of the latest sequence number published for this order is rejected|
    |cumulative_confirmed_size<br>`cc` |string|True|The total size the broker has confirmed for this ECN order since inception. Must be a multiple of the instrument's minimum size increment and should not exceed the cumulative requested size|
