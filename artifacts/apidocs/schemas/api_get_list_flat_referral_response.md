!!! info "[ApiGetListFlatReferralResponse](schemas/api_get_list_flat_referral_response.md)"
    |Name<br>`Lite`|Type|Required<br>`Default`| Description |
    |-|-|-|-|
    |flat_referrals<br>`fr` |[FlatReferral]|True|The list of flat referrals|
    ??? info "[FlatReferral](schemas/flat_referral.md)"
        <br>

        |Name<br>`Lite`|Type|Required<br>`Default`| Description |
        |-|-|-|-|
        |account_id<br>`ai` |string|True|The off chain account id|
        |referrer_id<br>`ri` |string|True|The off chain referrer account id|
        |referrer_level<br>`rl` |number|True|The referrer level; 1: direct referrer, 2: indirect referrer|
        |account_create_time<br>`ac` |string|True|The account creation time|
        |main_account_id<br>`ma` |string|True|The main account id|
        |referrer_main_account_id<br>`rm` |string|True|The referrer main account id|