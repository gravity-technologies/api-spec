!!! info "[AssetClass](/../../schemas/asset_class)"
    Asset class of an instrument's underlying. The first five values (crypto through index) are general classifications used by Perpetuals for display. The remaining values (equityNasdaq, equityNyse, etc.) are schedule-specific and used by SFPs to route to a trading schedule<br>

    |Value| Description |
    |-|-|
    |`CRYPTO` = 1|Digital assets (e.g. BTC, ETH)|
    |`EQUITY` = 2|Equities and equity-linked underlyings (e.g. stocks)|
    |`COMMODITY` = 3|Physical commodities (e.g. gold, oil)|
    |`FX` = 4|Foreign-exchange currency pairs|
    |`INDEX` = 5|Composite indices tracking a basket of underlyings|
    |`EQUITY_NASDAQ` = 6|NASDAQ-listed equities — maps to a TradingSchedule entry|
    |`EQUITY_NYSE` = 7|NYSE/NYSE Arca-listed equities and ETFs — maps to a TradingSchedule entry|
    |`EQUITY_KRX` = 8|Korea Exchange (KRX)-listed equities — maps to a TradingSchedule entry|
    |`COMMODITY_CME` = 9|CME-traded commodities — maps to a TradingSchedule entry|
    |`PRE_IPO` = 10|Pre-IPO instruments — maps to a TradingSchedule entry|
