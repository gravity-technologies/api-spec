!!! info "[OrderMetadata](schemas/order_metadata.md)"
    Metadata fields are used to support Backend only operations. These operations are not trustless by nature.<br>Hence, fields in here are never signed, and is never transmitted to the smart contract.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |client_order_id<br>`co` |string|True|A unique identifier for the active order within a subaccount, specified by the client<br>This is used to identify the order in the client's system<br>This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer<br>This field will not be propagated to the smart contract, and should not be signed by the client<br>This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected<br>Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]<br>To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]<br><br>When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId|
    |create_time<br>`ct` |string|False<br>`0`|[Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds|
