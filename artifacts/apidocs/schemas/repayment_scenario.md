!!! info "[RepaymentScenario](/../../schemas/repayment_scenario)"
    Server-only fee scenario tag for spot orders that repay MAM USDT debt against the insurance fund.<br>The default value 'unspecified' means the order is NOT a repayment (regular spot fees apply).<br>Risk rejects any user-submitted order with a non-unspecified value.<br>

    |Value| Description |
    |-|-|
    |`MANUAL_REPAYMENT` = 1|User-initiated MAM repay via TDG; uses MRR (/8) divisor for fee.|
    |`AUTO_REPAYMENT` = 2|DEPRECATED — replaced by autoRepayBorrowLimit / autoRepayLTV. Kept for capnp ordinal compatibility; no producer emits this value.|
    |`LIQUIDATION_REPAYMENT` = 3|Liquidator MMR>=100% step 2 repayment; uses LRR (/2) divisor for fee.|
    |`AUTO_REPAY_BORROW_LIMIT` = 4|Liquidator borrow-limit auto-repay; uses ARR (/4) divisor for fee. Validator checks BL trigger is still active.|
    |`AUTO_REPAY_LTV` = 5|Liquidator undeployed-loan / LTV auto-repay; uses ARR (/4) divisor for fee. Validator checks LTV trigger is still active.|
