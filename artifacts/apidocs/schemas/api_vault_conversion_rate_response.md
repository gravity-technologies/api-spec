!!! info "[ApiVaultConversionRateResponse](/../../schemas/api_vault_conversion_rate_response)"
    Response payload with the highest exchange rate the gateway currently accepts for the currency pair. Sign it as `exchangeRate`: any rate at or below it passes while the quote is valid.<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |from_currency<br>`fc` |string|True|The currency converted from.|
    |to_currency<br>`tc` |string|True|The currency converted into.|
    |exchange_rate<br>`er` |string|True|The highest rate accepted now, `toCurrency` per unit of `fromCurrency`, floored to 9 decimal places. It is 1 when both currencies are the same.|
    |spot_rate<br>`sr` |string|True|The current spot rate from the latest oracle prices, 9 decimal places.|
    |fee_rate_centi_beeps<br>`fr` |integer|True|The conversion fee configured for the pair, in centibeeps (1 = 0.0001%).|
    |window_seconds<br>`ws` |integer|True|The length of the window the rate is the highest of, in seconds.|
    |valid_until<br>`vu` |string|True|When the price sample the rate comes from leaves the window, in unix nanoseconds. Show a validity no longer than this.|
    |event_time<br>`et` |string|True|The time of the newest oracle price the rate uses, in unix nanoseconds.|
    |from_num_tokens<br>`fn` |string|False<br>`None`|The amount of `fromCurrency` the request named, if any.|
    |to_num_tokens<br>`tn` |string|False<br>`None`|What `fromNumTokens` converts into at `exchangeRate`, floored to `toCurrency` decimals. Omitted without `fromNumTokens`.|
