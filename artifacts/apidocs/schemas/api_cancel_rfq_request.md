!!! info "[ApiCancelRfqRequest](/../../schemas/api_cancel_rfq_request)"
    Cancels an open RFQ identified by its `rfq_id` before it is accepted or expires.<br>On cancellation the platform auto-cancels any maker private quotes bound to the RFQ, and emits a CANCELLED event on the `v1.rfq` stream. (An RFQ left untouched also auto-cancels its bound quotes when it reaches `rfq.expiry`.)<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The subaccount ID cancelling the RFQ|
    |rfq_id<br>`ri` |string|True|Cancel the RFQ with this `rfq_id`|
