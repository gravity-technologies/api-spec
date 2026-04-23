!!! info "[FuturesWalletAssets](/../../schemas/futures_wallet_assets)"
    Supported assets for a futures wallet mode<br>

    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |mode<br>`m` |SubAccountMode|True|The sub account mode|
    |supported_assets<br>`sa` |[SupportedAsset]|True|Assets supported under this futures mode|
    ??? info "[SubAccountMode](/../../schemas/sub_account_mode)"
        |Value| Description |
        |-|-|
        |`SINGLE_ASSET_MODE` = 1|Single asset mode: the subaccount is only allowed to hold one asset as collateral|
    ??? info "[SupportedAsset](/../../schemas/supported_asset)"
        An asset supported for a given wallet type<br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |asset_id<br>`ai` |integer|True|The currency ID of the asset|
        |asset_code<br>`ac` |string|True|The readable currency code of the asset|
        |balance_decimals<br>`bd` |integer|True|The number of decimals used for balance representation|
