!!! info "[VaultInvestorSummary](/../../schemas/vault_investor_summary)"
    Vault investor summary information.<br><br>This struct contains the summary of investments in a vault.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |sub_account_id<br>`sa` |string|True|The unique identifier of the vault sub account.|
    |num_lp_tokens<br>`nl` |string|True|The number of Vault LP tokens held by the investor.|
    |avg_entry_price<br>`ae` |string|True|The average entry price (in USD) of the vault LP tokens.|
    |current_price<br>`cp` |string|True|The current price (in USD) of the vault LP tokens.|
    |total_equity<br>`te` |string|True|The current valuation (in USD) of all held vault LP tokens.|
    |all_time_realized_pnl<br>`at` |string|True|The all-time realized PnL (in USD) that the investor has received from the vault.|
    |pending_redemption<br>`pr` |VaultRedemption|False<br>`None`|The singleton pending redemption (omitted if none).|
    |can_burn<br>`cb` |boolean|False<br>`true`|True if the requesting account is authorized to burn tokens on this vault, omitted otherwise.|
    |num_lp_tokens_locked<br>`nl1` |string|True|The number of the investor's vault LP tokens still within the vault's minimum investment period.|
    |num_lp_tokens_redeemable<br>`nl2` |string|True|The number of vault LP tokens the investor can request to redeem now: those past the minimum investment period, less any pending redemption.|
    |locked_lots<br>`ll` |[VaultLpLotView]|True|The investor's vault LP tokens within the minimum investment period, by the time they unlock (earliest first).|
    ??? info "[VaultRedemption](/../../schemas/vault_redemption)"
        Vault redemption information.<br><br>This struct contains information about a pending redemption from a vault.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |num_lp_tokens<br>`nl` |string|True|The number of LP Tokens requested for redemption.|
        |request_valuation<br>`rv` |string|True|The valuation (in USD) of the redemption request.|
        |request_time<br>`rt` |string|True|[Filled by GRVT Backend] Time at which the redemption request was received by GRVT in unix nanoseconds|
        |max_redemption_period_timestamp<br>`mr` |string|True|[Filled by GRVT Backend] Time in unix nanoseconds, beyond which the request will be force-redeemed.|
        |cancel_blocked<br>`cb` |boolean|False<br>`true`|Omitted for redemption requests to non-cross exchange vaults. True if cancellation is blocked within the CEV allocation allowance for the user's current tier (e.g. because the user has already transferred out the spot balance underlying the redemption request).|
        |to_currency<br>`tc` |string|True|The currency the request pays into the investor's funding account: the vault's investment currency, unless the request converts.|
        |exchange_rate<br>`er` |string|True|The signed rate the request is paid at, `to_currency` per unit of the vault's investment currency. 1 when the request does not convert.|
    ??? info "[VaultLpLotView](/../../schemas/vault_lp_lot_view)"
        Vault LP tokens minted together that unlock at the same time.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |unlock_time<br>`ut` |string|True|Time in unix nanoseconds from which these LP tokens can be redeemed.|
        |num_lp_tokens<br>`nl` |string|True|The number of LP tokens in the lot.|
