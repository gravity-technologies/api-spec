# Trading APIs
All requests should be made using the `POST` HTTP method.

## Order
### Create Order
```
FULL ENDPOINT: full/v1/create_order
LITE ENDPOINT: lite/v1/create_order
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_create_order_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "order": {
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
            }
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "o": {
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "im": false,
                "ti": "GOOD_TILL_TIME",
                "po": false,
                "ro": false,
                "l": [{
                    "i": "BTC_USDT_Perp",
                    "s": "10.5",
                    "lp": "65038.01",
                    "ib": true
                }],
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                },
                "m": {
                    "co": "23042",
                    "ct": "1697788800000000000"
                },
            }
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_create_order_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["10.5"],
                    "traded_size": ["1.5"],
                    "update_time": "1697788800000000000",
                    "avg_fill_price": ["60000.4"]
                }
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "oi": "0x1234567890abcdef",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "im": false,
                "ti": "GOOD_TILL_TIME",
                "po": false,
                "ro": false,
                "l": [{
                    "i": "BTC_USDT_Perp",
                    "s": "10.5",
                    "lp": "65038.01",
                    "ib": true
                }],
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                },
                "m": {
                    "co": "23042",
                    "ct": "1697788800000000000"
                },
                "s1": {
                    "s": "PENDING",
                    "rr": "CLIENT_CANCEL",
                    "bs": ["10.5"],
                    "ts": ["1.5"],
                    "ut": "1697788800000000000",
                    "af": ["60000.4"]
                }
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
        |1004|404|Data Not Found|
        |1005|500|Unknown Error|
        |2000|403|Order signature is from an unauthorized signer|
        |2001|403|Order signature has expired|
        |2002|403|Order signature does not match payload|
        |2003|403|Order sub account does not match logged in user|
        |2010|400|Order ID should be empty when creating an order|
        |2011|400|Client Order ID should be supplied when creating an order|
        |2012|400|Client Order ID overlaps with existing active order|
        |2030|400|Orderbook Orders must have a TimeInForce of GTT/IOC/FOK|
        |2031|400|RFQ Orders must have a TimeInForce of GTT/AON/IOC/FOK|
        |2032|400|Post Only can only be set to true for GTT/AON orders|
        |2020|400|Market Order must always be supplied without a limit price|
        |2021|400|Limit Order must always be supplied with a limit price|
        |2040|400|Order must contain at least one leg|
        |2041|400|Order Legs must be sorted by Derivative.Instrument/Underlying/BaseCurrency/Expiration/StrikePrice|
        |2042|400|Orderbook Orders must contain only one leg|
        |2050|400|Order state must be empty upon creation|
        |2051|400|Order execution metadata must be empty upon creation|
        |2060|400|Order Legs contain one or more inactive derivative|
        |2061|400|Unsupported Instrument Requested|
        |2062|400|Order size smaller than min size|
        |2063|400|Order size smaller than min block size in block trade venue|
        |2064|400|Invalid limit price tick|
        |2070|400|Liquidation Order is not supported|
        |2080|400|Insufficient margin to create order|
        |2081|400|Order Fill would result in exceeding maximum position size|
        |2082|400|Pre-order check failed|
        |2090|429|Max open orders exceeded|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/create_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "order": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "is_market": false,
                    "time_in_force": "GOOD_TILL_TIME",
                    "post_only": false,
                    "reduce_only": false,
                    "legs": [{
                        "instrument": "BTC_USDT_Perp",
                        "size": "10.5",
                        "limit_price": "65038.01",
                        "is_buying_asset": true
                    }],
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    },
                    "metadata": {
                        "client_order_id": "23042",
                        "create_time": "1697788800000000000"
                    },
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/create_order",
                "params": {
                    "order": {
                        "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                        "is_market": false,
                        "time_in_force": "GOOD_TILL_TIME",
                        "post_only": false,
                        "reduce_only": false,
                        "legs": [{
                            "instrument": "BTC_USDT_Perp",
                            "size": "10.5",
                            "limit_price": "65038.01",
                            "is_buying_asset": true
                        }],
                        "signature": {
                            "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                            "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                            "v": 28,
                            "expiration": "1697788800000000000",
                            "nonce": 1234567890
                        },
                        "metadata": {
                            "client_order_id": "23042",
                            "create_time": "1697788800000000000"
                        },
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/create_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "o": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "im": false,
                    "ti": "GOOD_TILL_TIME",
                    "po": false,
                    "ro": false,
                    "l": [{
                        "i": "BTC_USDT_Perp",
                        "s": "10.5",
                        "lp": "65038.01",
                        "ib": true
                    }],
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    },
                    "m": {
                        "co": "23042",
                        "ct": "1697788800000000000"
                    },
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/create_order",
                "p": {
                    "o": {
                        "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                        "im": false,
                        "ti": "GOOD_TILL_TIME",
                        "po": false,
                        "ro": false,
                        "l": [{
                            "i": "BTC_USDT_Perp",
                            "s": "10.5",
                            "lp": "65038.01",
                            "ib": true
                        }],
                        "s": {
                            "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                            "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                            "v": 28,
                            "e": "1697788800000000000",
                            "n": 1234567890
                        },
                        "m": {
                            "co": "23042",
                            "ct": "1697788800000000000"
                        },
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/create_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "order": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "is_market": false,
                    "time_in_force": "GOOD_TILL_TIME",
                    "post_only": false,
                    "reduce_only": false,
                    "legs": [{
                        "instrument": "BTC_USDT_Perp",
                        "size": "10.5",
                        "limit_price": "65038.01",
                        "is_buying_asset": true
                    }],
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    },
                    "metadata": {
                        "client_order_id": "23042",
                        "create_time": "1697788800000000000"
                    },
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/create_order",
                "params": {
                    "order": {
                        "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                        "is_market": false,
                        "time_in_force": "GOOD_TILL_TIME",
                        "post_only": false,
                        "reduce_only": false,
                        "legs": [{
                            "instrument": "BTC_USDT_Perp",
                            "size": "10.5",
                            "limit_price": "65038.01",
                            "is_buying_asset": true
                        }],
                        "signature": {
                            "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                            "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                            "v": 28,
                            "expiration": "1697788800000000000",
                            "nonce": 1234567890
                        },
                        "metadata": {
                            "client_order_id": "23042",
                            "create_time": "1697788800000000000"
                        },
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/create_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "o": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "im": false,
                    "ti": "GOOD_TILL_TIME",
                    "po": false,
                    "ro": false,
                    "l": [{
                        "i": "BTC_USDT_Perp",
                        "s": "10.5",
                        "lp": "65038.01",
                        "ib": true
                    }],
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    },
                    "m": {
                        "co": "23042",
                        "ct": "1697788800000000000"
                    },
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/create_order",
                "p": {
                    "o": {
                        "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                        "im": false,
                        "ti": "GOOD_TILL_TIME",
                        "po": false,
                        "ro": false,
                        "l": [{
                            "i": "BTC_USDT_Perp",
                            "s": "10.5",
                            "lp": "65038.01",
                            "ib": true
                        }],
                        "s": {
                            "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                            "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                            "v": 28,
                            "e": "1697788800000000000",
                            "n": 1234567890
                        },
                        "m": {
                            "co": "23042",
                            "ct": "1697788800000000000"
                        },
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/create_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "order": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "is_market": false,
                    "time_in_force": "GOOD_TILL_TIME",
                    "post_only": false,
                    "reduce_only": false,
                    "legs": [{
                        "instrument": "BTC_USDT_Perp",
                        "size": "10.5",
                        "limit_price": "65038.01",
                        "is_buying_asset": true
                    }],
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    },
                    "metadata": {
                        "client_order_id": "23042",
                        "create_time": "1697788800000000000"
                    },
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/create_order",
                "params": {
                    "order": {
                        "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                        "is_market": false,
                        "time_in_force": "GOOD_TILL_TIME",
                        "post_only": false,
                        "reduce_only": false,
                        "legs": [{
                            "instrument": "BTC_USDT_Perp",
                            "size": "10.5",
                            "limit_price": "65038.01",
                            "is_buying_asset": true
                        }],
                        "signature": {
                            "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                            "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                            "v": 28,
                            "expiration": "1697788800000000000",
                            "nonce": 1234567890
                        },
                        "metadata": {
                            "client_order_id": "23042",
                            "create_time": "1697788800000000000"
                        },
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/create_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "o": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "im": false,
                    "ti": "GOOD_TILL_TIME",
                    "po": false,
                    "ro": false,
                    "l": [{
                        "i": "BTC_USDT_Perp",
                        "s": "10.5",
                        "lp": "65038.01",
                        "ib": true
                    }],
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    },
                    "m": {
                        "co": "23042",
                        "ct": "1697788800000000000"
                    },
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/create_order",
                "p": {
                    "o": {
                        "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                        "im": false,
                        "ti": "GOOD_TILL_TIME",
                        "po": false,
                        "ro": false,
                        "l": [{
                            "i": "BTC_USDT_Perp",
                            "s": "10.5",
                            "lp": "65038.01",
                            "ib": true
                        }],
                        "s": {
                            "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                            "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                            "v": 28,
                            "e": "1697788800000000000",
                            "n": 1234567890
                        },
                        "m": {
                            "co": "23042",
                            "ct": "1697788800000000000"
                        },
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/create_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "order": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "is_market": false,
                    "time_in_force": "GOOD_TILL_TIME",
                    "post_only": false,
                    "reduce_only": false,
                    "legs": [{
                        "instrument": "BTC_USDT_Perp",
                        "size": "10.5",
                        "limit_price": "65038.01",
                        "is_buying_asset": true
                    }],
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    },
                    "metadata": {
                        "client_order_id": "23042",
                        "create_time": "1697788800000000000"
                    },
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/create_order",
                "params": {
                    "order": {
                        "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                        "is_market": false,
                        "time_in_force": "GOOD_TILL_TIME",
                        "post_only": false,
                        "reduce_only": false,
                        "legs": [{
                            "instrument": "BTC_USDT_Perp",
                            "size": "10.5",
                            "limit_price": "65038.01",
                            "is_buying_asset": true
                        }],
                        "signature": {
                            "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                            "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                            "v": 28,
                            "expiration": "1697788800000000000",
                            "nonce": 1234567890
                        },
                        "metadata": {
                            "client_order_id": "23042",
                            "create_time": "1697788800000000000"
                        },
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/create_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "o": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "im": false,
                    "ti": "GOOD_TILL_TIME",
                    "po": false,
                    "ro": false,
                    "l": [{
                        "i": "BTC_USDT_Perp",
                        "s": "10.5",
                        "lp": "65038.01",
                        "ib": true
                    }],
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    },
                    "m": {
                        "co": "23042",
                        "ct": "1697788800000000000"
                    },
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/create_order",
                "p": {
                    "o": {
                        "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                        "im": false,
                        "ti": "GOOD_TILL_TIME",
                        "po": false,
                        "ro": false,
                        "l": [{
                            "i": "BTC_USDT_Perp",
                            "s": "10.5",
                            "lp": "65038.01",
                            "ib": true
                        }],
                        "s": {
                            "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                            "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                            "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                            "v": 28,
                            "e": "1697788800000000000",
                            "n": 1234567890
                        },
                        "m": {
                            "co": "23042",
                            "ct": "1697788800000000000"
                        },
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Cancel Order
```
FULL ENDPOINT: full/v1/cancel_order
LITE ENDPOINT: lite/v1/cancel_order
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_cancel_order_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "oi": "0x1028403",
            "co": "23042"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/ack_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "ack": "true"
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "a": "true"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
        |3021|400|Either order ID or client order ID must be supplied|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/cancel_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "order_id": "0x1028403",
                "client_order_id": "23042"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/cancel_order",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "order_id": "0x1028403",
                    "client_order_id": "23042"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/cancel_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "oi": "0x1028403",
                "co": "23042"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/cancel_order",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "oi": "0x1028403",
                    "co": "23042"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/cancel_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "order_id": "0x1028403",
                "client_order_id": "23042"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/cancel_order",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "order_id": "0x1028403",
                    "client_order_id": "23042"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/cancel_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "oi": "0x1028403",
                "co": "23042"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/cancel_order",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "oi": "0x1028403",
                    "co": "23042"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/cancel_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "order_id": "0x1028403",
                "client_order_id": "23042"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/cancel_order",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "order_id": "0x1028403",
                    "client_order_id": "23042"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/cancel_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "oi": "0x1028403",
                "co": "23042"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/cancel_order",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "oi": "0x1028403",
                    "co": "23042"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/cancel_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "order_id": "0x1028403",
                "client_order_id": "23042"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/cancel_order",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "order_id": "0x1028403",
                    "client_order_id": "23042"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/cancel_order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "oi": "0x1028403",
                "co": "23042"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/cancel_order",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "oi": "0x1028403",
                    "co": "23042"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Cancel All Orders
```
FULL ENDPOINT: full/v1/cancel_all_orders
LITE ENDPOINT: lite/v1/cancel_all_orders
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_cancel_all_orders_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"]
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/ack_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "ack": "true"
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "a": "true"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/cancel_all_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/cancel_all_orders",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/cancel_all_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/cancel_all_orders",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/cancel_all_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/cancel_all_orders",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/cancel_all_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/cancel_all_orders",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/cancel_all_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/cancel_all_orders",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/cancel_all_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/cancel_all_orders",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/cancel_all_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/cancel_all_orders",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/cancel_all_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/cancel_all_orders",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Get Order
```
FULL ENDPOINT: full/v1/order
LITE ENDPOINT: lite/v1/order
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_get_order_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "order_id": "0x1028403",
            "client_order_id": "23042"
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "oi": "0x1028403",
            "co": "23042"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_get_order_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["10.5"],
                    "traded_size": ["1.5"],
                    "update_time": "1697788800000000000",
                    "avg_fill_price": ["60000.4"]
                }
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "oi": "0x1234567890abcdef",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "im": false,
                "ti": "GOOD_TILL_TIME",
                "po": false,
                "ro": false,
                "l": [{
                    "i": "BTC_USDT_Perp",
                    "s": "10.5",
                    "lp": "65038.01",
                    "ib": true
                }],
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                },
                "m": {
                    "co": "23042",
                    "ct": "1697788800000000000"
                },
                "s1": {
                    "s": "PENDING",
                    "rr": "CLIENT_CANCEL",
                    "bs": ["10.5"],
                    "ts": ["1.5"],
                    "ut": "1697788800000000000",
                    "af": ["60000.4"]
                }
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
        |1004|404|Data Not Found|
        |3021|400|Either order ID or client order ID must be supplied|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "order_id": "0x1028403",
                "client_order_id": "23042"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/order",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "order_id": "0x1028403",
                    "client_order_id": "23042"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "oi": "0x1028403",
                "co": "23042"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/order",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "oi": "0x1028403",
                    "co": "23042"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "order_id": "0x1028403",
                "client_order_id": "23042"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/order",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "order_id": "0x1028403",
                    "client_order_id": "23042"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "oi": "0x1028403",
                "co": "23042"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/order",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "oi": "0x1028403",
                    "co": "23042"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "order_id": "0x1028403",
                "client_order_id": "23042"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/order",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "order_id": "0x1028403",
                    "client_order_id": "23042"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "oi": "0x1028403",
                "co": "23042"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/order",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "oi": "0x1028403",
                    "co": "23042"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "order_id": "0x1028403",
                "client_order_id": "23042"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/order",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "order_id": "0x1028403",
                    "client_order_id": "23042"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/order' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "oi": "0x1028403",
                "co": "23042"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/order",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "oi": "0x1028403",
                    "co": "23042"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Open Orders
```
FULL ENDPOINT: full/v1/open_orders
LITE ENDPOINT: lite/v1/open_orders
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_open_orders_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"]
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_open_orders_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["10.5"],
                    "traded_size": ["1.5"],
                    "update_time": "1697788800000000000",
                    "avg_fill_price": ["60000.4"]
                }
            }]
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "oi": "0x1234567890abcdef",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "im": false,
                "ti": "GOOD_TILL_TIME",
                "po": false,
                "ro": false,
                "l": [{
                    "i": "BTC_USDT_Perp",
                    "s": "10.5",
                    "lp": "65038.01",
                    "ib": true
                }],
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                },
                "m": {
                    "co": "23042",
                    "ct": "1697788800000000000"
                },
                "s1": {
                    "s": "PENDING",
                    "rr": "CLIENT_CANCEL",
                    "bs": ["10.5"],
                    "ts": ["1.5"],
                    "ut": "1697788800000000000",
                    "af": ["60000.4"]
                }
            }]
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/open_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/open_orders",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/open_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/open_orders",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/open_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/open_orders",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/open_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/open_orders",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/open_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/open_orders",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/open_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/open_orders",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/open_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/open_orders",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/open_orders' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/open_orders",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Order History
```
FULL ENDPOINT: full/v1/order_history
LITE ENDPOINT: lite/v1/order_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_order_history_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_order_history_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "order_id": "0x1234567890abcdef",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "is_market": false,
                "time_in_force": "GOOD_TILL_TIME",
                "post_only": false,
                "reduce_only": false,
                "legs": [{
                    "instrument": "BTC_USDT_Perp",
                    "size": "10.5",
                    "limit_price": "65038.01",
                    "is_buying_asset": true
                }],
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                },
                "metadata": {
                    "client_order_id": "23042",
                    "create_time": "1697788800000000000"
                },
                "state": {
                    "status": "PENDING",
                    "reject_reason": "CLIENT_CANCEL",
                    "book_size": ["10.5"],
                    "traded_size": ["1.5"],
                    "update_time": "1697788800000000000",
                    "avg_fill_price": ["60000.4"]
                }
            }],
            "next": "Qw0918="
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "oi": "0x1234567890abcdef",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "im": false,
                "ti": "GOOD_TILL_TIME",
                "po": false,
                "ro": false,
                "l": [{
                    "i": "BTC_USDT_Perp",
                    "s": "10.5",
                    "lp": "65038.01",
                    "ib": true
                }],
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                },
                "m": {
                    "co": "23042",
                    "ct": "1697788800000000000"
                },
                "s1": {
                    "s": "PENDING",
                    "rr": "CLIENT_CANCEL",
                    "bs": ["10.5"],
                    "ts": ["1.5"],
                    "ut": "1697788800000000000",
                    "af": ["60000.4"]
                }
            }],
            "n": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/order_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/order_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/order_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/order_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/order_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/order_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/order_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/order_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/order_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/order_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/order_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/order_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/order_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/order_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/order_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/order_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
## Execution
### Fill History
```
FULL ENDPOINT: full/v1/fill_history
LITE ENDPOINT: lite/v1/fill_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_fill_history_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_fill_history_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "is_buyer": true,
                "is_taker": true,
                "size": "0.30",
                "price": "65038.01",
                "mark_price": "65038.01",
                "index_price": "65038.01",
                "interest_rate": 0.0003,
                "forward_price": "65038.01",
                "realized_pnl": "2400.50",
                "fee": "9.75",
                "fee_rate": 0.0003,
                "trade_id": "209358:2",
                "order_id": "0x10000101000203040506",
                "venue": "ORDERBOOK",
                "client_order_id": "23042"
            }],
            "next": "Qw0918="
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "et": "1697788800000000000",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "i": "BTC_USDT_Perp",
                "ib": true,
                "it": true,
                "s": "0.30",
                "p": "65038.01",
                "mp": "65038.01",
                "ip": "65038.01",
                "ir": 0.0003,
                "fp": "65038.01",
                "rp": "2400.50",
                "f": "9.75",
                "fr": 0.0003,
                "ti": "209358:2",
                "oi": "0x10000101000203040506",
                "v": "ORDERBOOK",
                "co": "23042"
            }],
            "n": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/fill_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/fill_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/fill_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/fill_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/fill_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/fill_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/fill_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/fill_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/fill_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/fill_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/fill_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/fill_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/fill_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/fill_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/fill_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/fill_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Positions
```
FULL ENDPOINT: full/v1/positions
LITE ENDPOINT: lite/v1/positions
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_positions_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "kind": ["PERPETUAL"],
            "base": ["BTC", "ETH"],
            "quote": ["USDT", "USDC"]
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "k": ["PERPETUAL"],
            "b": ["BTC", "ETH"],
            "q": ["USDT", "USDC"]
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_positions_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "size": "2635000.50",
                "notional": "2635000.50",
                "entry_price": "65038.01",
                "exit_price": "65038.01",
                "mark_price": "65038.01",
                "unrealized_pnl": "135000.50",
                "realized_pnl": "-35000.30",
                "total_pnl": "100000.20",
                "roi": "10.20",
                "quote_index_price": "1.0000102"
            }]
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "et": "1697788800000000000",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "i": "BTC_USDT_Perp",
                "s": "2635000.50",
                "n": "2635000.50",
                "ep": "65038.01",
                "ep1": "65038.01",
                "mp": "65038.01",
                "up": "135000.50",
                "rp": "-35000.30",
                "tp": "100000.20",
                "r": "10.20",
                "qi": "1.0000102"
            }]
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/positions' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/positions",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/positions' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/positions",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/positions' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/positions",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/positions' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/positions",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/positions' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/positions",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/positions' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/positions",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/positions' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "kind": ["PERPETUAL"],
                "base": ["BTC", "ETH"],
                "quote": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/positions",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "kind": ["PERPETUAL"],
                    "base": ["BTC", "ETH"],
                    "quote": ["USDT", "USDC"]
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/positions' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "k": ["PERPETUAL"],
                "b": ["BTC", "ETH"],
                "q": ["USDT", "USDC"]
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/positions",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "k": ["PERPETUAL"],
                    "b": ["BTC", "ETH"],
                    "q": ["USDT", "USDC"]
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Funding Payment History
```
FULL ENDPOINT: full/v1/funding_payment_history
LITE ENDPOINT: lite/v1/funding_payment_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_funding_payment_history_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "instrument": "BTC_USDT_Perp",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "i": "BTC_USDT_Perp",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_funding_payment_history_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "currency": "USDT",
                "amount": "9.75",
                "tx_id": "209358"
            }],
            "next": "Qw0918="
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "et": "1697788800000000000",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "i": "BTC_USDT_Perp",
                "c": "USDT",
                "a": "9.75",
                "ti": "209358"
            }],
            "n": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/funding_payment_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/funding_payment_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "instrument": "BTC_USDT_Perp",
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/funding_payment_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "i": "BTC_USDT_Perp",
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/funding_payment_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "i": "BTC_USDT_Perp",
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/funding_payment_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/funding_payment_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "instrument": "BTC_USDT_Perp",
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/funding_payment_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "i": "BTC_USDT_Perp",
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/funding_payment_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "i": "BTC_USDT_Perp",
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/funding_payment_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/funding_payment_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "instrument": "BTC_USDT_Perp",
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/funding_payment_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "i": "BTC_USDT_Perp",
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/funding_payment_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "i": "BTC_USDT_Perp",
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/funding_payment_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "instrument": "BTC_USDT_Perp",
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/funding_payment_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "instrument": "BTC_USDT_Perp",
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/funding_payment_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "i": "BTC_USDT_Perp",
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/funding_payment_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "i": "BTC_USDT_Perp",
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
## Transfer
### Deposit
```
FULL ENDPOINT: full/v1/deposit
LITE ENDPOINT: lite/v1/deposit
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_deposit_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "currency": "USDT",
            "num_tokens": "1500.0"
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "c": "USDT",
            "nt": "1500.0"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/ack_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "ack": "true"
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "a": "true"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/deposit' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/deposit",
                "params": {
                    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "currency": "USDT",
                    "num_tokens": "1500.0"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/deposit' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/deposit",
                "p": {
                    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "c": "USDT",
                    "nt": "1500.0"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/deposit' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/deposit",
                "params": {
                    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "currency": "USDT",
                    "num_tokens": "1500.0"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/deposit' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/deposit",
                "p": {
                    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "c": "USDT",
                    "nt": "1500.0"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/deposit' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/deposit",
                "params": {
                    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "currency": "USDT",
                    "num_tokens": "1500.0"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/deposit' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/deposit",
                "p": {
                    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "c": "USDT",
                    "nt": "1500.0"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/deposit' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/deposit",
                "params": {
                    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "currency": "USDT",
                    "num_tokens": "1500.0"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/deposit' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/deposit",
                "p": {
                    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "c": "USDT",
                    "nt": "1500.0"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Deposit History
```
FULL ENDPOINT: full/v1/deposit_history
LITE ENDPOINT: lite/v1/deposit_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_deposit_history_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "c": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c1": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_deposit_history_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "l_1_hash": "0x10000101000203040506",
                "l_2_hash": "0x10000101000203040506",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "initiated_time": "1697788800000000000",
                "confirmed_time": "1697788800000000000",
                "from_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0"
            }],
            "next": "Qw0918="
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "l1": "0x10000101000203040506",
                "l2": "0x10000101000203040506",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0",
                "it": "1697788800000000000",
                "ct": "1697788800000000000",
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0"
            }],
            "n": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/deposit_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/deposit_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/deposit_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/deposit_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/deposit_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/deposit_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/deposit_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/deposit_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/deposit_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/deposit_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/deposit_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/deposit_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/deposit_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/deposit_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/deposit_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/deposit_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Transfer
```
FULL ENDPOINT: full/v1/transfer
LITE ENDPOINT: lite/v1/transfer
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_transfer_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": 28,
                "expiration": "1697788800000000000",
                "nonce": 1234567890
            }
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "fs": "'$GRVT_SUB_ACCOUNT_ID'",
            "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "ts": "'$GRVT_SUB_ACCOUNT_ID'",
            "c": "USDT",
            "nt": "1500.0",
            "s": {
                "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": 28,
                "e": "1697788800000000000",
                "n": 1234567890
            }
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/ack_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "ack": "true"
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "a": "true"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/transfer' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/transfer",
                "params": {
                    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "currency": "USDT",
                    "num_tokens": "1500.0",
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/transfer' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/transfer",
                "p": {
                    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                    "c": "USDT",
                    "nt": "1500.0",
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/transfer' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/transfer",
                "params": {
                    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "currency": "USDT",
                    "num_tokens": "1500.0",
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/transfer' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/transfer",
                "p": {
                    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                    "c": "USDT",
                    "nt": "1500.0",
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/transfer' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/transfer",
                "params": {
                    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "currency": "USDT",
                    "num_tokens": "1500.0",
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/transfer' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/transfer",
                "p": {
                    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                    "c": "USDT",
                    "nt": "1500.0",
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/transfer' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/transfer",
                "params": {
                    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "currency": "USDT",
                    "num_tokens": "1500.0",
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/transfer' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/transfer",
                "p": {
                    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                    "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                    "c": "USDT",
                    "nt": "1500.0",
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Transfer History
```
FULL ENDPOINT: full/v1/transfer_history
LITE ENDPOINT: lite/v1/transfer_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_transfer_history_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "c": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c1": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_transfer_history_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "tx_id": "1028403",
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "from_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "to_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                },
                "event_time": "1697788800000000000"
            }],
            "next": "Qw0918="
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "ti": "1028403",
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "fs": "'$GRVT_SUB_ACCOUNT_ID'",
                "ta": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "ts": "'$GRVT_SUB_ACCOUNT_ID'",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                },
                "et": "1697788800000000000"
            }],
            "n": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/transfer_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/transfer_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/transfer_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/transfer_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/transfer_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/transfer_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/transfer_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/transfer_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/transfer_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/transfer_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/transfer_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/transfer_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/transfer_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/transfer_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/transfer_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/transfer_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Withdrawal
```
FULL ENDPOINT: full/v1/withdrawal
LITE ENDPOINT: lite/v1/withdrawal
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_withdrawal_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "currency": "USDT",
            "num_tokens": "1500.0",
            "signature": {
                "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": 28,
                "expiration": "1697788800000000000",
                "nonce": 1234567890
            }
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
            "c": "USDT",
            "nt": "1500.0",
            "s": {
                "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                "v": 28,
                "e": "1697788800000000000",
                "n": 1234567890
            }
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/ack_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "ack": "true"
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "a": "true"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/withdrawal' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/withdrawal",
                "params": {
                    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "currency": "USDT",
                    "num_tokens": "1500.0",
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/withdrawal' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/withdrawal",
                "p": {
                    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "c": "USDT",
                    "nt": "1500.0",
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/withdrawal' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/withdrawal",
                "params": {
                    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "currency": "USDT",
                    "num_tokens": "1500.0",
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/withdrawal' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/withdrawal",
                "p": {
                    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "c": "USDT",
                    "nt": "1500.0",
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/withdrawal' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/withdrawal",
                "params": {
                    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "currency": "USDT",
                    "num_tokens": "1500.0",
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/withdrawal' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/withdrawal",
                "p": {
                    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "c": "USDT",
                    "nt": "1500.0",
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/withdrawal' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/withdrawal",
                "params": {
                    "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "currency": "USDT",
                    "num_tokens": "1500.0",
                    "signature": {
                        "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "expiration": "1697788800000000000",
                        "nonce": 1234567890
                    }
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/withdrawal' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                }
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/withdrawal",
                "p": {
                    "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "c": "USDT",
                    "nt": "1500.0",
                    "s": {
                        "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                        "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                        "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                        "v": 28,
                        "e": "1697788800000000000",
                        "n": 1234567890
                    }
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Withdrawal History
```
FULL ENDPOINT: full/v1/withdrawal_history
LITE ENDPOINT: lite/v1/withdrawal_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_withdrawal_history_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "currency": ["USDT", "USDC"],
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "c": ["USDT", "USDC"],
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c1": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_withdrawal_history_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "tx_id": "1028403",
                "from_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "to_eth_address": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "currency": "USDT",
                "num_tokens": "1500.0",
                "signature": {
                    "signer": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "expiration": "1697788800000000000",
                    "nonce": 1234567890
                },
                "event_time": "1697788800000000000"
            }],
            "next": "Qw0918="
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "ti": "1028403",
                "fa": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "c": "USDT",
                "nt": "1500.0",
                "s": {
                    "s": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                    "r": "0xb788d96fee91c7cdc35918e0441b756d4000ec1d07d900c73347d9abbc20acc8",
                    "s1": "0x3d786193125f7c29c958647da64d0e2875ece2c3f845a591bdd7dae8c475e26d",
                    "v": 28,
                    "e": "1697788800000000000",
                    "n": 1234567890
                },
                "et": "1697788800000000000"
            }],
            "n": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/withdrawal_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/withdrawal_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/withdrawal_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/withdrawal_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/withdrawal_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/withdrawal_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/withdrawal_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/withdrawal_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/withdrawal_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/withdrawal_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/withdrawal_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/withdrawal_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/withdrawal_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "currency": ["USDT", "USDC"],
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/withdrawal_history",
                "params": {
                    "currency": ["USDT", "USDC"],
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/withdrawal_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "c": ["USDT", "USDC"],
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c1": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/withdrawal_history",
                "p": {
                    "c": ["USDT", "USDC"],
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c1": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
## Account
### Sub Account Summary
```
FULL ENDPOINT: full/v1/account_summary
LITE ENDPOINT: lite/v1/account_summary
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_sub_account_summary_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'"
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_sub_account_summary_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "margin_type": "SIMPLE_CROSS_MARGIN",
                "settle_currency": "USDT",
                "unrealized_pnl": "123456.78",
                "total_equity": "123456.78",
                "initial_margin": "123456.78",
                "maintenance_margin": "123456.78",
                "available_balance": "123456.78",
                "spot_balances": [{
                    "currency": "USDT",
                    "balance": "123456.78",
                    "index_price": "1.0000102"
                }],
                "positions": [{
                    "event_time": "1697788800000000000",
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "instrument": "BTC_USDT_Perp",
                    "size": "2635000.50",
                    "notional": "2635000.50",
                    "entry_price": "65038.01",
                    "exit_price": "65038.01",
                    "mark_price": "65038.01",
                    "unrealized_pnl": "135000.50",
                    "realized_pnl": "-35000.30",
                    "total_pnl": "100000.20",
                    "roi": "10.20",
                    "quote_index_price": "1.0000102"
                }],
                "settle_index_price": "1.0000102"
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "et": "1697788800000000000",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "mt": "SIMPLE_CROSS_MARGIN",
                "sc": "USDT",
                "up": "123456.78",
                "te": "123456.78",
                "im": "123456.78",
                "mm": "123456.78",
                "ab": "123456.78",
                "sb": [{
                    "c": "USDT",
                    "b": "123456.78",
                    "ip": "1.0000102"
                }],
                "p": [{
                    "et": "1697788800000000000",
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "i": "BTC_USDT_Perp",
                    "s": "2635000.50",
                    "n": "2635000.50",
                    "ep": "65038.01",
                    "ep1": "65038.01",
                    "mp": "65038.01",
                    "up": "135000.50",
                    "rp": "-35000.30",
                    "tp": "100000.20",
                    "r": "10.20",
                    "qi": "1.0000102"
                }],
                "si": "1.0000102"
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/account_summary",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/account_summary",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/account_summary",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/account_summary",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/account_summary",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/account_summary",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/account_summary",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'"
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'"
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/account_summary",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'"
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Sub Account History
```
FULL ENDPOINT: full/v1/account_history
LITE ENDPOINT: lite/v1/account_history
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_sub_account_history_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
            "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
            "start_time": "1697788800000000000",
            "end_time": "1697788800000000000",
            "limit": 500,
            "cursor": ""
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
            "sa": "'$GRVT_SUB_ACCOUNT_ID'",
            "st": "1697788800000000000",
            "et": "1697788800000000000",
            "l": 500,
            "c": ""
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_sub_account_history_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": [{
                "event_time": "1697788800000000000",
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "margin_type": "SIMPLE_CROSS_MARGIN",
                "settle_currency": "USDT",
                "unrealized_pnl": "123456.78",
                "total_equity": "123456.78",
                "initial_margin": "123456.78",
                "maintenance_margin": "123456.78",
                "available_balance": "123456.78",
                "spot_balances": [{
                    "currency": "USDT",
                    "balance": "123456.78",
                    "index_price": "1.0000102"
                }],
                "positions": [{
                    "event_time": "1697788800000000000",
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "instrument": "BTC_USDT_Perp",
                    "size": "2635000.50",
                    "notional": "2635000.50",
                    "entry_price": "65038.01",
                    "exit_price": "65038.01",
                    "mark_price": "65038.01",
                    "unrealized_pnl": "135000.50",
                    "realized_pnl": "-35000.30",
                    "total_pnl": "100000.20",
                    "roi": "10.20",
                    "quote_index_price": "1.0000102"
                }],
                "settle_index_price": "1.0000102"
            }],
            "next": "Qw0918="
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": [{
                "et": "1697788800000000000",
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "mt": "SIMPLE_CROSS_MARGIN",
                "sc": "USDT",
                "up": "123456.78",
                "te": "123456.78",
                "im": "123456.78",
                "mm": "123456.78",
                "ab": "123456.78",
                "sb": [{
                    "c": "USDT",
                    "b": "123456.78",
                    "ip": "1.0000102"
                }],
                "p": [{
                    "et": "1697788800000000000",
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "i": "BTC_USDT_Perp",
                    "s": "2635000.50",
                    "n": "2635000.50",
                    "ep": "65038.01",
                    "ep1": "65038.01",
                    "mp": "65038.01",
                    "up": "135000.50",
                    "rp": "-35000.30",
                    "tp": "100000.20",
                    "r": "10.20",
                    "qi": "1.0000102"
                }],
                "si": "1.0000102"
            }],
            "n": "Qw0918="
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1000|401|You need to authenticate prior to using this functionality|
        |1001|403|You are not authorized to access this functionality|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1000,
            "message":"You need to authenticate prior to using this functionality",
            "status":401
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1000,
            "m":"You need to authenticate prior to using this functionality",
            "s":401
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/account_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/account_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/account_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/account_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/account_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/account_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/account_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/account_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/account_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/account_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/account_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/account_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/account_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                "start_time": "1697788800000000000",
                "end_time": "1697788800000000000",
                "limit": 500,
                "cursor": ""
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/account_history",
                "params": {
                    "sub_account_id": "'$GRVT_SUB_ACCOUNT_ID'",
                    "start_time": "1697788800000000000",
                    "end_time": "1697788800000000000",
                    "limit": 500,
                    "cursor": ""
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/account_history' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
                "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                "st": "1697788800000000000",
                "et": "1697788800000000000",
                "l": 500,
                "c": ""
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/account_history",
                "p": {
                    "sa": "'$GRVT_SUB_ACCOUNT_ID'",
                    "st": "1697788800000000000",
                    "et": "1697788800000000000",
                    "l": 500,
                    "c": ""
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Aggregated Account Summary
```
FULL ENDPOINT: full/v1/aggregated_account_summary
LITE ENDPOINT: lite/v1/aggregated_account_summary
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/empty_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_aggregated_account_summary_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "main_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "total_equity": "3945034.23",
                "spot_balances": [{
                    "currency": "USDT",
                    "balance": "123456.78",
                    "index_price": "1.0000102"
                }]
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "ma": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "3945034.23",
                "sb": [{
                    "c": "USDT",
                    "b": "123456.78",
                    "ip": "1.0000102"
                }]
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1002,
            "m":"Internal Server Error",
            "s":500
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/aggregated_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/aggregated_account_summary",
                "params": {
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/aggregated_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/aggregated_account_summary",
                "p": {
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/aggregated_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/aggregated_account_summary",
                "params": {
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/aggregated_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/aggregated_account_summary",
                "p": {
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/aggregated_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/aggregated_account_summary",
                "params": {
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/aggregated_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/aggregated_account_summary",
                "p": {
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/aggregated_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/aggregated_account_summary",
                "params": {
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/aggregated_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/aggregated_account_summary",
                "p": {
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
### Funding Account Summary
```
FULL ENDPOINT: full/v1/funding_account_summary
LITE ENDPOINT: lite/v1/funding_account_summary
```

=== "Request"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/empty_request.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! question "Query"
        **Full Request**
        ``` { .json .copy }
        {
        }
        ```
        **Lite Request**
        ``` { .json .copy }
        {
        }
        ```
    </section>
=== "Response"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    -8<- "docs/schemas/api_funding_account_summary_response.md"
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! success
        **Full Response**
        ``` { .json .copy }
        {
            "result": {
                "main_account_id": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "total_equity": "3945034.23",
                "spot_balances": [{
                    "currency": "USDT",
                    "balance": "123456.78",
                    "index_price": "1.0000102"
                }]
            }
        }
        ```
        **Lite Response**
        ``` { .json .copy }
        {
            "r": {
                "ma": "0xc73c0c2538fd9b833d20933ccc88fdaa74fcb0d0",
                "te": "3945034.23",
                "sb": [{
                    "c": "USDT",
                    "b": "123456.78",
                    "ip": "1.0000102"
                }]
            }
        }
        ```
    </section>
=== "Errors"
    <section markdown="1" style="float: left; width: 70%; padding-right: 10px;">
    !!! info "Error Codes"
        |Code|HttpStatus| Description |
        |-|-|-|
        |1002|500|Internal Server Error|
        |1003|400|Request could not be processed due to malformed syntax|
    </section>
    <section markdown="1" style="float: right; width: 30%;">
    !!! failure
        **Full Error Response**
        ``` { .json .copy }
        {
            "request_id":1,
            "code":1002,
            "message":"Internal Server Error",
            "status":500
        }
        ```
        **Lite Error Response**
        ``` { .json .copy }
        {
            "ri":1,
            "c":1002,
            "m":"Internal Server Error",
            "s":500
        }
        ```
    </section>
=== "Try it out"
    -8<- "sections/auth_closed.md"
    === "DEV"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/full/v1/funding_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/funding_account_summary",
                "params": {
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.dev.gravitymarkets.io/lite/v1/funding_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.dev.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/funding_account_summary",
                "p": {
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "STAGING"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/full/v1/funding_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/funding_account_summary",
                "params": {
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.staging.gravitymarkets.io/lite/v1/funding_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.staging.gravitymarkets.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/funding_account_summary",
                "p": {
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "TESTNET"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/full/v1/funding_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/funding_account_summary",
                "params": {
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.testnet.grvt.io/lite/v1/funding_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.testnet.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/funding_account_summary",
                "p": {
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
    === "PROD"
        <section markdown="1" style="float: left; width: 50%; padding-right: 10px;">
        !!! example "REST Full"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/full/v1/funding_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Full"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/full" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "jsonrpc": "2.0",
                "method": "v1/funding_account_summary",
                "params": {
                },
                "id": 123
            }
            ' -w 360
            ```
        </section>
        <section markdown="1" style="float: right; width: 50%;">
        !!! example "REST Lite"
            ``` { .bash .copy }
            curl --location 'https://trades.grvt.io/lite/v1/funding_account_summary' \
            --header "Cookie: $GRVT_COOKIE" \
            --data '{
            }
            '
            ```
        !!! example "JSONRPC Lite"
            ``` { .bash .copy }
            wscat -c "wss://trades.grvt.io/ws/lite" \
            -H "Cookie: $GRVT_COOKIE" \
            -x '
            {
                "j": "2.0",
                "m": "v1/funding_account_summary",
                "p": {
                },
                "i": 123
            }
            ' -w 360
            ```
        </section>
<hr class="solid">
