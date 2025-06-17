!!! info "[ApiVaultViewRedemptionQueueResponse](/../../schemas/api_vault_view_redemption_queue_response)"
    Response payload for a vault manager to view the redemption queue for their vault, ordered by descending priority.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |redemption_queue<br>`rq` |[VaultRedemptionReqView]|True|Representation of a pending vault redemption request.|
    ??? info "[VaultRedemptionReqView](/../../schemas/vault_redemption_req_view)"
        Representation of a pending redemption request for a given vault.<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |request_time<br>`rt` |string|True|[Filled by GRVT Backend] Time at which the redemption request was received by GRVT in unix nanoseconds|
        |currency<br>`c` |Currency|True|The currency to redeem in|
        |num_lp_tokens<br>`nl` |string|True|The number of LP tokens to redeem|
        |max_redemption_period_timestamp<br>`mr` |string|True|[Filled by GRVT Backend] Time in unix nanoseconds, beyond which the request will be force-redeemed.|
        ??? info "[Currency](/../../schemas/currency)"
            The list of Currencies that are supported on the GRVT exchange<br>

            |Value| Description |
            |-|-|
            |`USD` = 1|the USD fiat currency|
            |`USDC` = 2|the USDC token|
            |`USDT` = 3|the USDT token|
            |`ETH` = 4|the ETH token|
            |`BTC` = 5|the BTC token|
            |`SOL` = 6|the SOL token|
            |`ARB` = 7|the ARB token|
            |`BNB` = 8|the BNB token|
            |`ZK` = 9|the ZK token|
            |`POL` = 10|the POL token|
            |`OP` = 11|the OP token|
            |`ATOM` = 12|the ATOM token|
            |`KPEPE` = 13|the 1000PEPE token|
            |`TON` = 14|the TON token|
            |`XRP` = 15|the XRP token|
            |`TRUMP` = 20|the TRUMP token|
            |`SUI` = 21|the SUI token|
            |`LINK` = 25|the LINK token|
            |`JUP` = 27|the JUP token|
            |`FARTCOIN` = 28|the FARTCOIN token|
            |`ENA` = 29|the ENA token|
            |`DOGE` = 30|the DOGE token|
            |`ADA` = 33|the ADA token|
            |`AAVE` = 34|the AAVE token|
            |`BERA` = 35|the BERA token|
            |`IP` = 40|the IP token|
