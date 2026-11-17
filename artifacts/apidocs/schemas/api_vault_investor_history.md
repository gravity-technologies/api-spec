!!! info "[ApiVaultInvestorHistory](/../../schemas/api_vault_investor_history)"
    The vault investor history returned by the service to client<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |event_time<br>`et` |string|True|Time at which the event was emitted in unix nanoseconds|
    |off_chain_account_id<br>`oc` |string|True|The off chain account id of the investor, only visible to the manager|
    |vault_id<br>`vi` |string|True|The unique identifier of the vault.|
    |type<br>`t` |VaultInvestorAction|True|The type of transaction that occurred. List of types: vaultInvest, vaultBurnLpToken, vaultRedeem|
    |price<br>`p` |string|True|The price of the vault LP tokens at the time of the event.|
    |size<br>`s` |string|True|The amount of Vault LP tokens invested or redeemed.|
    |realized_pnl<br>`rp` |string|True|The realized PnL of the vault.|
    |performance_fee<br>`pf` |string|True|The performance fee of the vault.|
    |token_currency<br>`tc` |string|True|The vault leg's currency: the vault's investment currency, which the vault received or paid. Empty on a burn, which moves no tokens.|
    |num_tokens<br>`nt` |string|True|The vault leg: the tokens of tokenCurrency the vault received on an invest or paid on a redemption. 0 on a burn, and on a vaultRedeem recorded before its results carried the amount.|
    |from_currency<br>`fc` |string|True|The currency that left its owner: on an invest the investor's source currency (the user leg), on a redemption tokenCurrency. A row without conversion has the vault leg's currency. Empty on a burn.|
    |from_num_tokens<br>`fn` |string|True|The tokens of fromCurrency that left their owner: on an invest what the investor paid (the user leg), on a redemption numTokens. 0 on a burn, and on a vaultRedeem recorded before its results carried the amount.|
    |to_currency<br>`tc1` |string|True|The currency that reached its owner: on a redemption the investor's payout currency (the user leg), on an invest tokenCurrency. A row without conversion has the vault leg's currency. Empty on a burn.|
    |to_num_tokens<br>`tn` |string|True|The tokens of toCurrency that reached their owner: on a redemption what the investor received (the user leg), on an invest numTokens. 0 on a burn, and on a vaultRedeem recorded before its results carried the amount.|
    |conversion_fee_num_tokens<br>`cf` |string|True|The conversion fee in toCurrency: the difference between the two legs of a converting invest or redemption. 0 without conversion.|
    |from_sub_account_id<br>`fs` |string|True|The trading sub-account an invest was paid from. 0 for the funding account and on other rows.|
    |request_time<br>`rt` |string|True|On a redemption, when its redemption request was made, in unix nanoseconds. 0 when unknown and on other rows.|
    ??? info "[VaultInvestorAction](/../../schemas/vault_investor_action)"
        |Value| Description |
        |-|-|
        |`UNSPECIFIED` = 0||
        |`VAULT_INVEST` = 1||
        |`VAULT_BURN_LP_TOKEN` = 2||
        |`VAULT_REDEEM` = 3||
    ??? info "[WalletType](/../../schemas/wallet_type)"
        |Value| Description |
        |-|-|
        |`FUNDING` = 1|Funding wallet|
        |`SPOT` = 2|Spot wallet|
        |`FUTURES` = 3|Futures wallet|
