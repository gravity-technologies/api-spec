# ruff: noqa: D200
# ruff: noqa: D204
# ruff: noqa: D205
# ruff: noqa: D404
# ruff: noqa: W291
# ruff: noqa: D400
# ruff: noqa: E501
from dataclasses import dataclass
from enum import Enum


class CandlestickInterval(Enum):
    CI_1_M = 1  # 1 minute
    CI_3_M = 2  # 3 minutes
    CI_5_M = 3  # 5 minutes
    CI_15_M = 4  # 15 minutes
    CI_30_M = 5  # 30 minutes
    CI_1_H = 6  # 1 hour
    CI_2_H = 7  # 2 hour
    CI_4_H = 8  # 4 hour
    CI_6_H = 9  # 6 hour
    CI_8_H = 10  # 8 hour
    CI_12_H = 11  # 12 hour
    CI_1_D = 12  # 1 day
    CI_3_D = 13  # 3 days
    CI_5_D = 14  # 5 days
    CI_1_W = 15  # 1 week
    CI_2_W = 16  # 2 weeks
    CI_3_W = 17  # 3 weeks
    CI_4_W = 18  # 4 weeks


class CandlestickType(Enum):
    TRADE = 1  # Tracks traded prices
    MARK = 2  # Tracks mark prices
    INDEX = 3  # Tracks index prices
    MID = 4  # Tracks book mid prices


class Currency(Enum):
    USDC = 2  # the USDC token
    USDT = 3  # the USDT token
    ETH = 4  # the ETH token
    BTC = 5  # the BTC token


class InstrumentSettlementPeriod(Enum):
    PERPETUAL = 1  # Instrument settles through perpetual hourly funding cycles
    DAILY = 2  # Instrument settles at an expiry date, marked as a daily instrument
    WEEKLY = 3  # Instrument settles at an expiry date, marked as a weekly instrument
    MONTHLY = 4  # Instrument settles at an expiry date, marked as a monthly instrument
    QUARTERLY = (
        5  # Instrument settles at an expiry date, marked as a quarterly instrument
    )


class Kind(Enum):
    PERPETUAL = 1  # the perpetual asset kind
    FUTURE = 2  # the future asset kind
    CALL = 3  # the call option asset kind
    PUT = 4  # the put option asset kind


class MarginType(Enum):
    SIMPLE_CROSS_MARGIN = 2  # Simple Cross Margin Mode: all assets have a predictable margin impact, the whole subaccount shares a single margin
    PORTFOLIO_CROSS_MARGIN = 3  # Portfolio Cross Margin Mode: asset margin impact is analysed on portfolio level, the whole subaccount shares a single margin


class OrderRejectReason(Enum):
    CLIENT_CANCEL = 1  # client called a Cancel API
    CLIENT_BULK_CANCEL = 2  # client called a Bulk Cancel API
    CLIENT_SESSION_END = 3  # client called a Session Cancel API, or set the WebSocket connection to 'cancelOrdersOnTerminate'
    MARKET_CANCEL = 4  # the market order was cancelled after no/partial fill. Takes precedence over other TimeInForce cancel reasons
    IOC_CANCEL = 5  # the IOC order was cancelled after no/partial fill
    AON_CANCEL = 6  # the AON order was cancelled as it could not be fully matched
    FOK_CANCEL = 7  # the FOK order was cancelled as it could not be fully matched
    EXPIRED = 8  # the order was cancelled as it has expired
    FAIL_POST_ONLY = 9  # the post-only order could not be posted into the orderbook
    FAIL_REDUCE_ONLY = (
        10  # the reduce-only order would have caused position size to increase
    )
    MM_PROTECTION = 11  # the order was cancelled due to market maker protection trigger
    SELF_TRADE_PROTECTION = (
        12  # the order was cancelled due to self-trade protection trigger
    )
    SELF_MATCHED_SUBACCOUNT = (
        13  # the order matched with another order from the same sub account
    )
    OVERLAPPING_CLIENT_ORDER_ID = (
        14  # an active order on your sub account shares the same clientOrderId
    )
    BELOW_MARGIN = (
        15  # the order will bring the sub account below initial margin requirement
    )
    LIQUIDATION = (
        16  # the sub account is liquidated (and all open orders are cancelled by Gravity)
    )
    INSTRUMENT_INVALID = 17  # instrument is invalid or not found on Gravity
    INSTRUMENT_DEACTIVATED = 18  # instrument is no longer tradable on Gravity. (typically due to a market halt, or instrument expiry)
    SYSTEM_FAILOVER = 19  # system failover resulting in loss of order state
    UNAUTHORISED = 20  # the credentials used (userSession/apiKeySession/walletSignature) is not authorised to perform the action
    SESSION_KEY_EXPIRED = 21  # the session key used to sign the order expired
    SUB_ACCOUNT_NOT_FOUND = 22  # the subaccount does not exist
    NO_TRADE_PERMISSION = (
        23  # the signature used to sign the order has no trade permission
    )
    UNSUPPORTED_TIME_IN_FORCE = (
        24  # the order payload does not contain a supported TimeInForce value
    )
    MULTI_LEGGED_ORDER = 25  # the order has multiple legs, but multiple legs are not supported by this venue


class OrderStateFilter(Enum):
    C = 1  # create only filter
    U = 2  # update only filter
    A = 3  # create and update filter


class OrderStatus(Enum):
    PENDING = 1  # Order is waiting for Trigger Condition to be hit
    OPEN = 2  # Order is actively matching on the orderbook, could be unfilled or partially filled
    FILLED = 3  # Order is fully filled and hence closed
    REJECTED = 4  # Order is rejected by GRVT Backend since if fails a particular check (See OrderRejectReason)
    CANCELLED = 5  # Order is cancelled by the user using one of the supported APIs (See OrderRejectReason)


class SubAccountTradeInterval(Enum):
    SAT_1_MO = 1  # 1 month
    SAT_1_D = 2  # 1 day


class TimeInForce(Enum):
    """
    |                       | Must Fill All | Can Fill Partial |
    | -                     | -             | -                |
    | Must Fill Immediately | FOK           | IOC              |
    | Can Fill Till Time    | AON           | GTC              |

    """

    GOOD_TILL_TIME = 1  # GTT - Remains open until it is cancelled, or expired
    ALL_OR_NONE = 2  # AON - Either fill the whole order or none of it (Block Trades Only)
    IMMEDIATE_OR_CANCEL = 3  # IOC - Fill the order as much as possible, when hitting the orderbook. Then cancel it
    FILL_OR_KILL = 4  # FOK - Both AoN and IoC. Either fill the full order when hitting the orderbook, or cancel it


class Venue(Enum):
    ORDERBOOK = 1  # the trade is cleared on the orderbook venue


@dataclass
class ApiPositionsRequest:
    sub_account_id: int  # The sub account ID to request for
    kind: list[
        Kind
    ]  # The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
    underlying: list[
        Currency
    ]  # The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned
    quote: list[
        Currency
    ]  # The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned


@dataclass
class Positions:
    event_time: int  # Time at which the event was emitted in unix nanoseconds
    sub_account_id: int  # The sub account ID that participated in the trade
    instrument: str  # The instrument being represented
    balance: str  # The balance of the position, expressed in underlying asset decimal units. Negative for short positions
    value: str  # The value of the position, negative for short assets, expressed in quote asset decimal units
    """
    The entry price of the position, expressed in `9` decimals
    Whenever increasing the balance of a position, the entry price is updated to the new average entry price
    newEntryPrice = (oldEntryPrice * oldBalance + tradePrice * tradeBalance) / (oldBalance + tradeBalance)
    """
    entry_price: str
    """
    The exit price of the position, expressed in `9` decimals
    Whenever decreasing the balance of a position, the exit price is updated to the new average exit price
    newExitPrice = (oldExitPrice * oldExitBalance + tradePrice * tradeBalance) / (oldExitBalance + tradeBalance)
    """
    exit_price: str
    mark_price: str  # The mark price of the position, expressed in `9` decimals
    """
    The unrealized PnL of the position, expressed in quote asset decimal units
    unrealizedPnl = (markPrice - entryPrice) * balance
    """
    unrealized_pnl: str
    """
    The realized PnL of the position, expressed in quote asset decimal units
    realizedPnl = (exitPrice - entryPrice) * exitBalance
    """
    realized_pnl: str
    """
    The total PnL of the position, expressed in quote asset decimal units
    totalPnl = realizedPnl + unrealizedPnl
    """
    pnl: str
    """
    The ROI of the position, expressed as a percentage
    roi = (pnl / (entryPrice * balance)) * 100
    """
    roi: str


@dataclass
class ApiPositionsResponse:
    results: list[Positions]  # The positions matching the request filter


@dataclass
class ApiPrivateTradeHistoryRequest:
    sub_account_id: int  # The sub account ID to request for
    kind: list[
        Kind
    ]  # The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
    underlying: list[
        Currency
    ]  # The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned
    quote: list[
        Currency
    ]  # The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
    expiration: int  # The expiration time to apply in unix nanoseconds. If nil, this defaults to all expirations. Otherwise, only entries matching the filter will be returned
    strike_price: str  # The strike price to apply. If nil, this defaults to all strike prices. Otherwise, only entries matching the filter will be returned
    limit: int  # The limit to query for. Defaults to 500; Max 1000
    cursor: str  # The cursor to indicate when to start the query from


@dataclass
class PrivateTrade:
    event_time: int  # Time at which the event was emitted in unix nanoseconds
    sub_account_id: int  # The sub account ID that participated in the trade
    instrument: str  # The instrument being represented
    is_buyer: bool  # The side that the subaccount took on the trade
    is_taker: bool  # The role that the subaccount took on the trade
    size: str  # The number of assets being traded, expressed in underlying asset decimal units
    price: str  # The traded price, expressed in `9` decimals
    mark_price: str  # The mark price of the instrument at point of trade, expressed in `9` decimals
    index_price: str  # The index price of the instrument at point of trade, expressed in `9` decimals
    interest_rate: str  # The interest rate of the underlying at point of trade, expressed in centibeeps (1/100th of a basis point)
    forward_price: str  # [Options] The forward price of the option at point of trade, expressed in `9` decimals
    realized_pnl: str  # The realized PnL of the trade, expressed in quote asset decimal units (0 if increasing position size)
    fee: str  # The fees paid on the trade, expressed in quote asset decimal unit (negative if maker rebate applied)
    fee_rate: str  # The fee rate paid on the trade
    trade_id: int  # A trade identifier
    order_id: str  # An order identifier
    venue: Venue  # The venue where the trade occurred
    """
    A unique identifier for the active order within a subaccount, specified by the client
    This is used to identify the order in the client's system
    This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer
    This field will not be propagated to the smart contract, and should not be signed by the client
    This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected
    Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]
    To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]

    When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId
    """
    client_order_id: int


@dataclass
class ApiPrivateTradeHistoryResponse:
    total: int  # The total number of private trades matching the request filter
    next: str  # The cursor to indicate when to start the query from
    results: list[PrivateTrade]  # The private trades matching the request asset


@dataclass
class ApiSubAccountSummaryRequest:
    sub_account_id: int  # The subaccount ID to filter by


@dataclass
class SpotBalance:
    currency: Currency  # The currency you hold a spot balance in
    """
    The balance of the asset, expressed in underlying asset decimal units
    Must take into account the value of all positions with this quote asset
    ie. for USDT denominated subaccounts, this is is identical to total balance
    """
    balance: str


@dataclass
class SubAccount:
    event_time: int  # Time at which the event was emitted in unix nanoseconds
    sub_account_id: int  # The sub account ID this entry refers to
    margin_type: MarginType  # The type of margin algorithm this subaccount uses
    """
    The Quote Currency that this Sub Account is denominated in
    This subaccount can only open derivative positions denominated in this quote currency
    All other assets are converted to this quote currency for the purpose of calculating margin
    In the future, when users select a Multi-Currency Margin Type, this will be USD
    """
    quote_currency: Currency
    unrealized_pnl: str  # The total unrealized PnL of all positions owned by this subaccount, denominated in quote currency decimal units
    total_value: str  # The total value across all spot assets, or in other words, the current margin
    initial_margin: str  # The initial margin requirement of all positions owned by this vault, denominated in quote currency decimal units
    maintanence_margin: str  # The maintanence margin requirement of all positions owned by this vault, denominated in quote currency decimal units
    available_margin: str  # The margin available for withdrawal, denominated in quote currency decimal units
    spot_balances: list[
        SpotBalance
    ]  # The list of spot assets owned by this sub account, and their balances
    positions: list[Positions]  # The list of positions owned by this sub account


@dataclass
class ApiSubAccountSummaryResponse:
    results: SubAccount  # The sub account matching the request sub account


@dataclass
class ApiSubAccountHistoryRequest:
    """
    The request to get the history of a sub account
    SubAccount Summary values are snapshotted once every hour
    No snapshots are taken if the sub account has no activity in the hourly window
    The history is returned in reverse chronological order
    History is preserved only for the last 30 days
    """

    sub_account_id: int  # The sub account ID to request for
    start_time: int  # Start time of sub account history in unix nanoseconds
    end_time: int  # End time of sub account history in unix nanoseconds
    cursor: str  # The cursor to indicate when to start the next query from


@dataclass
class ApiSubAccountHistoryResponse:
    total: int  # The total number of sub account snapshots matching the request filter
    next: str  # The cursor to indicate when to start the next query from
    results: list[SubAccount]  # The sub account history matching the request sub account


@dataclass
class ApiLatestSnapSubAccountsRequest:
    """
    The request to get the latest snapshot of list sub account

    """

    sub_account_i_ds: list[int]  # The list of sub account ids to query


@dataclass
class ApiLatestSnapSubAccountsResponse:
    results: list[SubAccount]  # The sub account history matching the request sub account


@dataclass
class MarkPrice:
    currency: Currency  # The currency you hold a spot balance in
    mark_price: str  # The mark price of the asset, expressed in `9` decimals


@dataclass
class ApiAggregatedAccountSummaryResponse:
    main_account_id: (
        str  # The main account ID of the account to which the summary belongs
    )
    total_equity: str  # Total equity of the account, denominated in USD
    spot_balances: list[
        SpotBalance
    ]  # The list of spot assets owned by this sub account, and their balances
    mark_prices: list[
        MarkPrice
    ]  # The list of mark prices for the assets owned by this account


@dataclass
class ApiFundingAccountSummaryResponse:
    main_account_id: (
        str  # The main account ID of the account to which the summary belongs
    )
    total_equity: str  # Total equity of the account, denominated in USD
    spot_balances: list[
        SpotBalance
    ]  # The list of spot assets owned by this account, and their balances
    mark_prices: list[
        MarkPrice
    ]  # The list of mark prices for the assets owned by this account


@dataclass
class ApiOrderbookLevelsRequest:
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """

    instrument: str
    depth: int  # Depth of the order book to be retrieved (API/Snapshot max is 100, Delta max is 1000)
    aggregate: int  # The number of levels to aggregate into one level (1 = no aggregation, 10/100/1000 = aggregate 10/100/1000 levels into 1)


@dataclass
class OrderbookLevel:
    price: str  # The price of the level, expressed in `9` decimals
    size: str  # The number of assets offered, expressed in underlying asset decimal units
    num_orders: int  # The number of open orders at this level


@dataclass
class OrderbookLevels:
    event_time: int  # Time at which the event was emitted in unix nanoseconds
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    bids: list[OrderbookLevel]  # The list of best bids up till query depth
    asks: list[OrderbookLevel]  # The list of best asks up till query depth


@dataclass
class ApiOrderbookLevelsResponse:
    results: OrderbookLevels  # The orderbook levels objects matching the request asset


@dataclass
class ApiMiniTickerRequest:
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """

    instrument: str


@dataclass
class MiniTicker:
    event_time: int | None  # Time at which the event was emitted in unix nanoseconds
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str | None
    mark_price: str | None  # The mark price of the instrument, expressed in `9` decimals
    index_price: (
        str | None
    )  # The index price of the instrument, expressed in `9` decimals
    last_price: (
        str | None
    )  # The last traded price of the instrument (also close price), expressed in `9` decimals
    last_size: (
        str | None
    )  # The number of assets traded in the last trade, expressed in underlying asset decimal units
    mid_price: str | None  # The mid price of the instrument, expressed in `9` decimals
    best_bid_price: (
        str | None
    )  # The best bid price of the instrument, expressed in `9` decimals
    best_bid_size: (
        str | None
    )  # The number of assets offered on the best bid price of the instrument, expressed in underlying asset decimal units
    best_ask_price: (
        str | None
    )  # The best ask price of the instrument, expressed in `9` decimals
    best_ask_size: (
        str | None
    )  # The number of assets offered on the best ask price of the instrument, expressed in underlying asset decimal units


@dataclass
class ApiMiniTickerResponse:
    results: MiniTicker  # The mini ticker matching the request asset


@dataclass
class ApiTickerRequest:
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """

    instrument: str


@dataclass
class Ticker:
    """
    Derived data such as the below, will not be included by default:
      - 24 hour volume (`buyVolume + sellVolume`)
      - 24 hour taker buy/sell ratio (`buyVolume / sellVolume`)
      - 24 hour average trade price (`volumeQ / volumeU`)
      - 24 hour average trade volume (`volume / trades`)
      - 24 hour percentage change (`24hStatChange / 24hStat`)
      - 48 hour statistics (`2 * 24hStat - 24hStatChange`)

    To query for an extended ticker payload, leverage the `greeks` and the `derived` flags.
    Ticker extensions are currently under design to offer you more convenience.
    These flags are only supported on the `Ticker Snapshot` WS endpoint, and on the `Ticker` API endpoint.

    """

    event_time: int | None  # Time at which the event was emitted in unix nanoseconds
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str | None
    mark_price: str | None  # The mark price of the instrument, expressed in `9` decimals
    index_price: (
        str | None
    )  # The index price of the instrument, expressed in `9` decimals
    last_price: (
        str | None
    )  # The last traded price of the instrument (also close price), expressed in `9` decimals
    last_size: (
        str | None
    )  # The number of assets traded in the last trade, expressed in underlying asset decimal units
    mid_price: str | None  # The mid price of the instrument, expressed in `9` decimals
    best_bid_price: (
        str | None
    )  # The best bid price of the instrument, expressed in `9` decimals
    best_bid_size: (
        str | None
    )  # The number of assets offered on the best bid price of the instrument, expressed in underlying asset decimal units
    best_ask_price: (
        str | None
    )  # The best ask price of the instrument, expressed in `9` decimals
    best_ask_size: (
        str | None
    )  # The number of assets offered on the best ask price of the instrument, expressed in underlying asset decimal units
    funding_rate_8_h_curr: (
        str | None
    )  # The current funding rate of the instrument, expressed in centibeeps (1/100th of a basis point)
    funding_rate_8_h_avg: (
        str | None
    )  # The average funding rate of the instrument (over last 8h), expressed in centibeeps (1/100th of a basis point)
    interest_rate: (
        str | None
    )  # The interest rate of the underlying, expressed in centibeeps (1/100th of a basis point)
    forward_price: (
        str | None
    )  # [Options] The forward price of the option, expressed in `9` decimals
    buy_volume_24_h_u: (
        str | None
    )  # The 24 hour taker buy volume of the instrument, expressed in underlying asset decimal units
    sell_volume_24_h_u: (
        str | None
    )  # The 24 hour taker sell volume of the instrument, expressed in underlying asset decimal units
    buy_volume_24_h_q: (
        str | None
    )  # The 24 hour taker buy volume of the instrument, expressed in quote asset decimal units
    sell_volume_24_h_q: (
        str | None
    )  # The 24 hour taker sell volume of the instrument, expressed in quote asset decimal units
    high_price: (
        str | None
    )  # The 24 hour highest traded price of the instrument, expressed in `9` decimals
    low_price: (
        str | None
    )  # The 24 hour lowest traded price of the instrument, expressed in `9` decimals
    open_price: (
        str | None
    )  # The 24 hour first traded price of the instrument, expressed in `9` decimals
    open_interest: (
        str | None
    )  # The open interest in the instrument, expressed in underlying asset decimal units
    long_short_ratio: (
        str | None
    )  # The ratio of accounts that are net long vs net short on this instrument


@dataclass
class ApiTickerResponse:
    results: Ticker  # The mini ticker matching the request asset


@dataclass
class ApiPublicTradesRequest:
    """
    Retrieves up to 1000 of the most recent public trades in any given instrument. Do not use this to poll for data -- a websocket subscription is much more performant, and useful.
    This endpoint offers public trading data, use the Trading APIs instead to query for your personalized trade tape.
    """

    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    limit: int  # The limit to query for. Defaults to 500; Max 1000


@dataclass
class PublicTrade:
    event_time: int  # Time at which the event was emitted in unix nanoseconds
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    is_taker_buyer: bool  # If taker was the buyer on the trade
    size: str  # The number of assets being traded, expressed in underlying asset decimal units
    price: str  # The traded price, expressed in `9` decimals
    mark_price: str  # The mark price of the instrument at point of trade, expressed in `9` decimals
    index_price: str  # The index price of the instrument at point of trade, expressed in `9` decimals
    interest_rate: str  # The interest rate of the underlying at point of trade, expressed in centibeeps (1/100th of a basis point)
    forward_price: str  # [Options] The forward price of the option at point of trade, expressed in `9` decimals
    trade_id: int  # A trade identifier
    venue: Venue  # The venue where the trade occurred
    is_liquidation: bool  # If the trade was a liquidation


@dataclass
class ApiPublicTradesResponse:
    results: list[PublicTrade]  # The public trades matching the request asset


@dataclass
class ApiPublicTradeHistoryRequest:
    """
    Perform historical lookup of public trades in any given instrument.
    This endpoint offers public trading data, use the Trading APIs instead to query for your personalized trade tape.
    Only data from the last three months will be retained.
    """

    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    limit: int  # The limit to query for. Defaults to 500; Max 1000
    cursor: str  # The cursor to indicate when to start the query from


@dataclass
class ApiPublicTradeHistoryResponse:
    results: list[PublicTrade]  # The public trades matching the request asset


@dataclass
class ApiGetInstrumentRequest:
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """

    instrument: str


@dataclass
class Instrument:
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """

    instrument: str
    underlying: Currency  # The underlying currency
    quote: Currency  # The quote currency
    kind: Kind  # The kind of instrument
    expiry: int  # The expiry time of the instrument in unix nanoseconds
    strike_price: str  # The strike price of the instrument, expressed in `9` decimals
    venues: list[Venue]  # Venues that this instrument can be traded at
    settlement_period: (
        InstrumentSettlementPeriod  # The settlement period of the instrument
    )
    underlying_decimals: int  # The smallest denomination of the underlying asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)
    quote_decimals: int  # The smallest denomination of the quote asset supported by GRVT (+3 represents 0.001, -3 represents 1000, 0 represents 1)
    tick_size: str  # The size of a single tick, expressed in quote asset decimal units
    min_size: (
        str  # The minimum contract size, expressed in underlying asset decimal units
    )
    min_block_trade_size: (
        str  # The minimum block trade size, expressed in underlying asset decimal units
    )
    create_time: int  # Creation time in unix nanoseconds


@dataclass
class ApiGetInstrumentResponse:
    results: Instrument  # The instrument matching the request asset


@dataclass
class ApiGetFilteredInstrumentsRequest:
    kind: list[
        Kind
    ]  # The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
    underlying: list[
        Currency
    ]  # The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned
    quote: list[
        Currency
    ]  # The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
    is_active: bool  # Request for active instruments only
    limit: int  # The limit to query for. Defaults to 500; Max 100000


@dataclass
class ApiGetFilteredInstrumentsResponse:
    results: list[Instrument]  # The instruments matching the request filter


@dataclass
class ApiCandlestickRequest:
    """
    Kline/Candlestick bars for an instrument. Klines are uniquely identified by their instrument, type, interval, and open time.
    startTime and endTime are optional parameters. The semantics of these parameters are as follows:<ul><li>If both `startTime` and `endTime` are not set, the most recent candlesticks are returned up to `limit`.</li><li>If `startTime` is set and `endTime` is not set, the candlesticks starting from `startTime` are returned up to `limit`.</li><li>If `startTime` is not set and `endTime` is set, the candlesticks ending at `endTime` are returned up to `limit`.</li><li>If both `startTime` and `endTime` are set, the candlesticks between `startTime` and `endTime` are returned up to `limit`.</li></ul>
    """

    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    interval: CandlestickInterval  # The interval of each candlestick
    type: CandlestickType  # The type of candlestick data to retrieve
    start_time: int  # Start time of kline data in unix nanoseconds
    end_time: int  # End time of kline data in unix nanoseconds
    limit: int  # The limit to query for. Defaults to 500; Max 1500


@dataclass
class Candlestick:
    open_time: int  # Open time of kline bar in unix nanoseconds
    close_time: int  # Close time of kline bar in unix nanosecond
    open: str  # The open price, expressed in underlying currency resolution units
    close: str  # The close price, expressed in underlying currency resolution units
    high: str  # The high price, expressed in underlying currency resolution units
    low: str  # The low price, expressed in underlying currency resolution units
    volume_u: str  # The underlying volume transacted, expressed in underlying asset decimal units
    volume_q: str  # The quote volume transacted, expressed in quote asset decimal units
    trades: int  # The number of trades transacted
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str


@dataclass
class ApiCandlestickResponse:
    results: list[Candlestick]  # The candlestick result set for given interval


@dataclass
class ApiFundingRateRequest:
    """
    Lookup the historical funding rate of various pairs.
    startTime and endTime are optional parameters. The semantics of these parameters are as follows:<ul><li>If both `startTime` and `endTime` are not set, the most recent funding rates are returned up to `limit`.</li><li>If `startTime` is set and `endTime` is not set, the funding rates starting from `startTime` are returned up to `limit`.</li><li>If `startTime` is not set and `endTime` is set, the funding rates ending at `endTime` are returned up to `limit`.</li><li>If both `startTime` and `endTime` are set, the funding rates between `startTime` and `endTime` are returned up to `limit`.</li></ul>

    The instrument is also optional. When left empty, all perpetual instruments are returned.
    """

    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    start_time: int  # Start time of funding rate in unix nanoseconds
    end_time: int  # End time of funding rate in unix nanoseconds
    limit: int  # The limit to query for. Defaults to 90; Max 300


@dataclass
class FundingRate:
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """

    instrument: str
    funding_rate: int  # The funding rate of the instrument, expressed in centibeeps
    funding_time: (
        int  # The funding timestamp of the funding rate, expressed in unix nanoseconds
    )
    mark_price: int  # The mark price of the instrument at funding timestamp, expressed in `9` decimals


@dataclass
class ApiFundingRateResponse:
    results: list[FundingRate]  # The funding rate result set for given interval


@dataclass
class ApiSettlementPriceRequest:
    """
    Lookup the historical settlement price of various pairs.
    startTime and endTime are optional parameters. The semantics of these parameters are as follows:<ul><li>If both `startTime` and `endTime` are not set, the most recent settlement prices are returned up to `limit`.</li><li>If `startTime` is set and `endTime` is not set, the settlement prices starting from `startTime` are returned up to `limit`.</li><li>If `startTime` is not set and `endTime` is set, the settlement prices ending at `endTime` are returned up to `limit`.</li><li>If both `startTime` and `endTime` are set, the settlement prices between `startTime` and `endTime` are returned up to `limit`.</li></ul>

    The instrument is also optional. When left empty, all perpetual instruments are returned.
    """

    underlying: Currency  # The underlying currency to select
    quote: Currency  # The quote currency to select
    start_time: int  # Start time of kline data in unix nanoseconds
    end_time: int  # End time of kline data in unix nanoseconds
    expiration: int  # The expiration time to select in unix nanoseconds
    strike_price: str  # The strike price to select
    limit: int  # The limit to query for. Defaults to 30; Max 100


@dataclass
class APISettlementPrice:
    underlying: Currency  # The underlying currency of the settlement price
    quote: Currency  # The quote currency of the settlement price
    settlement_time: int  # The settlement timestamp of the settlement price, expressed in unix nanoseconds
    settlement_price: str  # The settlement price, expressed in `9` decimals


@dataclass
class ApiSettlementPriceResponse:
    results: list[APISettlementPrice]  # The funding rate result set for given interval


@dataclass
class WSRequestV1:
    stream: str  # The channel to subscribe to (eg: ticker.s / ticker.d
    feed: list[str]  # The list of feeds to subscribe to (eg:
    method: str  # The method to use for the request (eg: subscribe / unsubscribe)
    is_full: bool  # Whether the request is for full data or lite data


@dataclass
class WSOrderbookLevelsFeedSelectorV1:
    """
    Subscribes to aggregated orderbook updates for a single instrument. The `book.s` channel offers simpler integration. To experience higher publishing rates, please use the `book.d` channel.
    Unlike the `book.d` channel which publishes an initial snapshot, then only streams deltas after, the `book.s` channel publishes full snapshots at each feed.

    The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of all levels of the Orderbook.</li><li>After the snapshot, the server will only send levels that have changed in value.</li></ul>

    Field Semantics:<ul><li>[DeltaOnly] If a level is not updated, level not published</li><li>If a level is updated, {size: '123'}</li><li>If a level is set to zero, {size: '0'}</li><li>Incoming levels will be published as soon as price moves</li><li>Outgoing levels will be published with `size = 0`</li></ul>
    """

    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    """
    The minimal rate at which we publish feeds (in milliseconds)
    Delta (100, 200, 500, 1000, 5000)
    Snapshot (500, 1000, 5000)
    """
    rate: int
    depth: int  # Depth of the order book to be retrieved (API/Snapshot max is 100, Delta max is 1000)
    aggregate: int  # The number of levels to aggregate into one level (1 = no aggregation, 10/100/1000 = aggregate 10/100/1000 levels into 1)


@dataclass
class WSOrderbookLevelsFeedDataV1:
    stream: str  # Stream name
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: OrderbookLevels  # An orderbook levels object matching the request filter


@dataclass
class WSMiniTickerFeedSelectorV1:
    """
    Subscribes to a mini ticker feed for a single instrument. The `mini.s` channel offers simpler integration. To experience higher publishing rates, please use the `mini.d` channel.
    Unlike the `mini.d` channel which publishes an initial snapshot, then only streams deltas after, the `mini.s` channel publishes full snapshots at each feed.

    The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the mini ticker.</li><li>After the snapshot, the server will only send deltas of the mini ticker.</li><li>The server will send a delta if any of the fields in the mini ticker have changed.</li></ul>

    Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul>
    """

    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    """
    The minimal rate at which we publish feeds (in milliseconds)
    Delta (raw, 50, 100, 200, 500, 1000, 5000)
    Snapshot (200, 500, 1000, 5000)
    """
    rate: int


@dataclass
class WSMiniTickerFeedDataV1:
    stream: str  # Stream name
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: MiniTicker  # A mini ticker matching the request filter


@dataclass
class WSTickerFeedSelectorV1:
    """
    Subscribes to a ticker feed for a single instrument. The `ticker.s` channel offers simpler integration. To experience higher publishing rates, please use the `ticker.d` channel.
    Unlike the `ticker.d` channel which publishes an initial snapshot, then only streams deltas after, the `ticker.s` channel publishes full snapshots at each feed.

    The Delta feed will work as follows:<ul><li>On subscription, the server will send a full snapshot of the ticker.</li><li>After the snapshot, the server will only send deltas of the ticker.</li><li>The server will send a delta if any of the fields in the ticker have changed.</li></ul>

    Field Semantics:<ul><li>[DeltaOnly] If a field is not updated, {}</li><li>If a field is updated, {field: '123'}</li><li>If a field is set to zero, {field: '0'}</li><li>If a field is set to null, {field: ''}</li></ul>
    """

    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    """
    The minimal rate at which we publish feeds (in milliseconds)
    Delta (100, 200, 500, 1000, 5000)
    Snapshot (500, 1000, 5000)
    """
    rate: int


@dataclass
class WSTickerFeedDataV1:
    stream: str  # Stream name
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: Ticker  # A ticker matching the request filter


@dataclass
class ApiTickerFeedDataV1:
    results: Ticker  # The mini ticker matching the request asset


@dataclass
class WSPublicTradesFeedSelectorV1:
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """

    instrument: str
    limit: int  # The limit to query for. Defaults to 500; Max 1000


@dataclass
class WSPublicTradesFeedDataV1:
    stream: str  # Stream name
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: PublicTrade  # A public trade matching the request filter


@dataclass
class WSCandlestickFeedSelectorV1:
    """
    Subscribes to a stream of Kline/Candlestick updates for an instrument. A Kline is uniquely identified by its open time.
    A new Kline is published every interval (if it exists). Upon subscription, the server will send the 5 most recent Kline for the requested interval.
    """

    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """
    instrument: str
    interval: CandlestickInterval  # The interval of each candlestick
    type: CandlestickType  # The type of candlestick data to retrieve


@dataclass
class WSCandlestickFeedDataV1:
    stream: str  # Stream name
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: Candlestick  # A candlestick entry matching the request filters


@dataclass
class WSResponseV1:
    stream: str  # The channel to subscribe to (eg: ticker.s / ticker.d
    subs: list[str]  # The list of feeds subscribed to
    unsubs: list[str]  # The list of feeds unsubscribed to


@dataclass
class ApiGetAllInstrumentsRequest:
    is_active: bool | None  # Fetch only active instruments


@dataclass
class ApiGetAllInstrumentsResponse:
    instruments: list[Instrument]  # List of instruments


@dataclass
class OrderLeg:
    instrument: str  # The instrument to trade in this leg
    size: str  # The total number of assets to trade in this leg, expressed in underlying asset decimal units.
    """
    The limit price of the order leg, expressed in `9` decimals.
    This is the total amount of base currency to pay/receive for all legs.
    """
    limit_price: str
    """
    If a OCO order is specified, this must contain the other limit price
    User must sign both limit prices. Depending on which trigger condition is activated, a different limit price is used
    The smart contract will always validate both limit prices, by arranging them in ascending order
    """
    oco_limit_price: str
    is_buying_asset: bool  # Specifies if the order leg is a buy or sell


@dataclass
class Signature:
    signer: str  # The address (public key) of the wallet signing the payload
    r: str  # Signature R
    s: str  # Signature S
    v: int  # Signature V
    expiration: int  # Timestamp after which this signature expires, expressed in unix nanoseconds. Must be capped at 30 days
    """
    Users can randomly generate this value, used as a signature deconflicting key.
    ie. You can send the same exact instruction twice with different nonces.
    When the same nonce is used, the same payload will generate the same signature.
    Our system will consider the payload a duplicate, and ignore it.
    """
    nonce: int


@dataclass
class OrderMetadata:
    """
    Metadata fields are used to support Backend only operations. These operations are not trustless by nature.
    Hence, fields in here are never signed, and is never transmitted to the smart contract.
    """

    """
    A unique identifier for the active order within a subaccount, specified by the client
    This is used to identify the order in the client's system
    This field can be used for order amendment/cancellation, but has no bearing on the smart contract layer
    This field will not be propagated to the smart contract, and should not be signed by the client
    This value must be unique for all active orders in a subaccount, or amendment/cancellation will not work as expected
    Gravity UI will generate a random clientOrderID for each order in the range [0, 2^63 - 1]
    To prevent any conflicts, client machines should generate a random clientOrderID in the range [2^63, 2^64 - 1]

    When GRVT Backend receives an order with an overlapping clientOrderID, we will reject the order with rejectReason set to overlappingClientOrderId
    """
    client_order_id: int
    create_time: int  # [Filled by GRVT Backend] Time at which the order was received by GRVT in unix nanoseconds


@dataclass
class OrderState:
    status: OrderStatus  # The status of the order
    reject_reason: OrderRejectReason  # The reason for rejection or cancellation
    book_size: list[
        str
    ]  # The number of assets available for orderbook/RFQ matching. Sorted in same order as Order.Legs
    traded_size: list[
        str
    ]  # The total number of assets traded. Sorted in same order as Order.Legs
    update_time: (
        int  # Time at which the order was updated by GRVT, expressed in unix nanoseconds
    )


@dataclass
class Order:
    """
    Order is a typed payload used throughout the GRVT platform to express all orderbook, RFQ, and liquidation orders.
    GRVT orders are capable of expressing both single-legged, and multi-legged orders by default.
    This increases the learning curve slightly but reduces overall integration load, since the order payload is used across all GRVT trading venues.
    Given GRVT's trustless settlement model, the Order payload also carries the signature, required to trade the order on our ZKSync Hyperchain.

    All fields in the Order payload (except `id`, `metadata`, and `state`) are trustlessly enforced on our Hyperchain.
    This minimizes the amount of trust users have to offer to GRVT
    """

    order_id: str  # [Filled by GRVT Backend] A unique 128-bit identifier for the order, deterministically generated within the GRVT backend
    sub_account_id: int  # The subaccount initiating the order
    """
    If the order is a market order
    Market Orders do not have a limit price, and are always executed according to the maker order price.
    Market Orders must always be taker orders
    """
    is_market: bool
    """
    Four supported types of orders: GTT, IOC, AON, FOK:<ul>
    <li>PARTIAL EXECUTION = GTT / IOC - allows partial size execution on each leg</li>
    <li>FULL EXECUTION = AON / FOK - only allows full size execution on all legs</li>
    <li>TAKER ONLY = IOC / FOK - only allows taker orders</li>
    <li>MAKER OR TAKER = GTT / AON - allows maker or taker orders</li>
    </ul>Exchange only supports (GTT, IOC, FOK)
    RFQ Maker only supports (GTT, AON), RFQ Taker only supports (FOK)
    """
    time_in_force: TimeInForce
    """
    The taker fee percentage cap signed by the order.
    This is the maximum taker fee percentage the order sender is willing to pay for the order.
    Expressed in 1/100th of a basis point. Eg. 100 = 1bps, 10,000 = 1%

    """
    taker_fee_percentage_cap: int
    maker_fee_percentage_cap: int  # Same as TakerFeePercentageCap, but for the maker fee. Negative for maker rebates
    """
    If True, Order must be a maker order. It has to fill the orderbook instead of match it.
    If False, Order can be either a maker or taker order.

    |               | Must Fill All | Can Fill Partial |
    | -             | -             | -                |
    | Must Be Taker | FOK + False   | IOC + False      |
    | Can Be Either | AON + False   | GTC + False      |
    | Must Be Maker | AON + True    | GTC + True       |

    """
    post_only: bool
    reduce_only: bool  # If True, Order must reduce the position size, or be cancelled
    """
    The legs present in this order
    The legs must be sorted by Asset.Instrument/Underlying/Quote/Expiration/StrikePrice
    """
    legs: list[OrderLeg]
    signature: Signature  # The signature approving this order
    metadata: OrderMetadata  # Order Metadata, ignored by the smart contract, and unsigned by the client
    state: OrderState  # [Filled by GRVT Backend] The current state of the order, ignored by the smart contract, and unsigned by the client


@dataclass
class ApiCreateOrderRequest:
    order: Order  # The order to create


@dataclass
class ApiCreateOrderResponse:
    order: Order  # The created order


@dataclass
class ApiCancelOrderRequest:
    sub_account_id: int  # The subaccount ID cancelling the order
    order_id: str  # Cancel the order with this `order_id`
    client_order_id: int  # Cancel the order with this `client_order_id`


@dataclass
class ApiCancelOrderResponse:
    order: Order  # The cancelled order


@dataclass
class ApiCancelAllOrdersRequest:
    sub_account_id: int  # The subaccount ID cancelling all orders


@dataclass
class ApiCancelAllOrdersResponse:
    num_cancelled: int  # The number of orders cancelled


@dataclass
class ApiOpenOrdersRequest:
    sub_account_id: int  # The subaccount ID to filter by
    kind: list[
        Kind
    ]  # The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
    underlying: list[
        Currency
    ]  # The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned
    quote: list[
        Currency
    ]  # The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned


@dataclass
class ApiOpenOrdersResponse:
    orders: list[Order]  # The Open Orders matching the request filter


@dataclass
class ApiOrderHistoryRequest:
    sub_account_id: int  # The subaccount ID to filter by
    kind: list[
        Kind
    ]  # The kind filter to apply. If nil, this defaults to all kinds. Otherwise, only entries matching the filter will be returned
    underlying: list[
        Currency
    ]  # The underlying filter to apply. If nil, this defaults to all underlyings. Otherwise, only entries matching the filter will be returned
    quote: list[
        Currency
    ]  # The quote filter to apply. If nil, this defaults to all quotes. Otherwise, only entries matching the filter will be returned
    expiration: list[
        int
    ]  # The expiration time to apply in nanoseconds. If nil, this defaults to all expirations. Otherwise, only entries matching the filter will be returned
    strike_price: list[
        str
    ]  # The strike price to apply. If nil, this defaults to all strike prices. Otherwise, only entries matching the filter will be returned
    limit: int  # The limit to query for. Defaults to 500; Max 1000
    cursor: str  # The cursor to indicate when to start the query from


@dataclass
class ApiOrderHistoryResponse:
    total: int  # The total number of orders matching the request filter
    next: str  # The cursor to indicate when to start the query from
    orders: list[Order]  # The Open Orders matching the request filter


@dataclass
class EmptyRequest:
    pass


@dataclass
class AckResponse:
    acknowledgement: bool  # Gravity has acknowledged that the request has been successfully received and it will process it in the backend


@dataclass
class ApiOrderStateRequest:
    sub_account_id: int  # The subaccount ID to filter by
    order_id: str  # Filter for `order_id`
    client_order_id: int  # Filter for `client_order_id`


@dataclass
class ApiOrderStateResponse:
    state: OrderState  # The order state for the requested filter


@dataclass
class ApiGetOrderRequest:
    sub_account_id: int  # The subaccount ID to filter by
    order_id: str  # Filter for `order_id`
    client_order_id: int  # Filter for `client_order_id`


@dataclass
class ApiGetOrderResponse:
    order: Order  # The order object for the requested filter


@dataclass
class ApiGetUserEcosystemPointRequest:
    account_id: str  # The off chain account id
    calculate_from: int  # Start time of the epoch - phase
    include_user_rank: bool  # Include user rank in the response


@dataclass
class EcosystemPoint:
    account_id: str  # The off chain account id
    main_account_id: str  # The main account id
    total_point: int  # Total ecosystem point
    direct_invite_count: int  # Direct invite count
    indirect_invite_count: int  # Indirect invite count
    direct_invite_trading_volume: str  # Direct invite trading volume
    indirect_invite_trading_volume: str  # Indirect invite trading volume
    calculate_at: int  # The time when the ecosystem point is calculated
    calculate_from: int  # Start time of the epoch - phase
    calculate_to: int  # End time of the epoch - phase
    rank: int  # The rank of the account in the ecosystem


@dataclass
class ApiGetUserEcosystemPointResponse:
    points: list[EcosystemPoint]  # The list of ecosystem points


@dataclass
class ApiGetEcosystemLeaderboardRequest:
    calculate_from: int  # Start time of the epoch - phase
    limit: int  # The number of accounts to return


@dataclass
class ApiGetEcosystemLeaderboardResponse:
    points: list[EcosystemPoint]  # The list of ecosystem points


@dataclass
class ApiGetEcosystemReferralStatResponse:
    direct_invite_count: int  # Direct invite count
    indirect_invite_count: int  # Indirect invite count
    direct_invite_trading_volume: (
        str  # Total volume traded by direct invites multiple by 1e9
    )
    indirect_invite_trading_volume: (
        str  # Total volume traded by indirect invites multiple by 1e9
    )


@dataclass
class ApiResolveEpochEcosystemMetricResponse:
    epoch_name: str  # The name of the epoch
    point: (
        int  # Ecosystem points up to the most recently calculated time within this epoch
    )
    last_calculated_time: (
        int  # The time in unix nanoseconds when the ecosystem points were last calculated
    )


@dataclass
class EcosystemMetric:
    direct_invite_count: int  # Direct invite count
    indirect_invite_count: int  # Indirect invite count
    direct_invite_trading_volume: str  # Direct invite trading volume
    indirect_invite_trading_volume: str  # Indirect invite trading volume
    total_point: int  # Total ecosystem point of this epoch/phase


@dataclass
class ApiFindFirstEpochMetricResponse:
    phase_zero_metric: EcosystemMetric  # Phase zero metric
    phase_one_metric: EcosystemMetric  # Phase one metric
    rank: int  # The rank of the account in the ecosystem
    total: int  # The total number of accounts in the ecosystem
    total_point: int  # Total ecosystem point of the first epoch
    last_calculated_at: int  # The time when the ecosystem points were last calculated


@dataclass
class EcosystemLeaderboardUser:
    account_id: str  # The off chain account id
    rank: int  # The rank of the account in the ecosystem
    total_point: int  # Total ecosystem point
    twitter_username: str  # The twitter username of the account


@dataclass
class ApiFindEcosystemLeaderboardResponse:
    users: list[EcosystemLeaderboardUser]  # The list of ecosystem leaderboard users


@dataclass
class ApiGetListFlatReferralRequest:
    referral_id: str  # The off chain referrer account id to get all flat referrals
    start_time: int  # Optional. Start time in unix nanoseconds
    end_time: int  # Optional. End time in unix nanoseconds
    account_id: str  # The off chain account id to get all user's referrers


@dataclass
class FlatReferral:
    account_id: str  # The off chain account id
    referrer_id: str  # The off chain referrer account id
    referrer_level: int  # The referrer level; 1: direct referrer, 2: indirect referrer
    account_create_time: int  # The account creation time
    main_account_id: str  # The main account id
    referrer_main_account_id: str  # The referrer main account id


@dataclass
class ApiGetListFlatReferralResponse:
    flat_referrals: list[FlatReferral]  # The list of flat referrals


@dataclass
class ApiSubAccountTradeRequest:
    """
    The readable name of the instrument. For Perpetual: ETH_USDT_Perp [Underlying Quote Perp]
    For Future: BTC_USDT_Fut_20Oct23 [Underlying Quote Fut DateFormat]
    For Call: ETH_USDT_Call_20Oct23_4123 [Underlying Quote Call DateFormat StrikePrice]
    For Put: ETH_USDT_Put_20Oct23_4123 [Underlying Quote Put DateFormat StrikePrice]
    """

    instrument: str
    interval: SubAccountTradeInterval  # The interval of each sub account trade
    sub_account_i_ds: list[int]  # The list of sub account ids to query
    start_interval: int  # Optional. The starting time in unix nanoseconds of a specific interval to query
    start_time: int  # Optional. Start time in unix nanoseconds
    end_time: int  # Optional. End time in unix nanoseconds


@dataclass
class SubAccountTrade:
    start_interval: int  # Start of calculation epoch
    sub_account_id: int  # The sub account id
    instrument: str  # The instrument being represented
    total_fee: int  # Total fee paid
    total_trade_volume: str  # Total volume traded


@dataclass
class ApiSubAccountTradeResponse:
    results: list[SubAccountTrade]  # The sub account trade result set for given interval


@dataclass
class ApiSubAccountTradeAggregationRequest:
    interval: SubAccountTradeInterval  # The interval of each sub account trade
    sub_account_i_ds: list[int]  # The list of sub account ids to query
    start_interval: int  # Optional. The starting time in unix nanoseconds of a specific interval to query


@dataclass
class SubAccountTradeAggregation:
    start_interval: int  # Start of calculation epoch
    sub_account_id: int  # The sub account id
    total_fee: int  # Total fee paid
    total_trade_volume: str  # Total volume traded


@dataclass
class ApiSubAccountTradeAggregationResponse:
    results: list[
        SubAccountTradeAggregation
    ]  # The sub account trade aggregation result set for given interval


@dataclass
class ApiGetTraderStatResponse:
    total_fee: int  # Total fee paid


@dataclass
class TraderMetric:
    total_fee: int  # Total fee paid
    total_point: int  # Total trader point of this epoch/phase


@dataclass
class ApiFindTraderEpochMetricResponse:
    metric: TraderMetric  # Phase zero metric
    rank: int  # The rank of the account in the trader
    total: int  # The total number of accounts in the trader
    last_calculated_at: int  # The time when the trader points were last calculated


@dataclass
class TraderLeaderboardUser:
    account_id: str  # The off chain account id
    rank: int  # The rank of the account in the Trader
    total_point: int  # Total Trader point
    twitter_username: str  # The twitter username of the account


@dataclass
class ApiFindTraderLeaderboardResponse:
    users: list[TraderLeaderboardUser]  # The list of trader leaderboard users


@dataclass
class WSOrderFeedSelectorV1:
    """
    Subscribes to a feed of order updates pertaining to orders made by your account.
    Each Order can be uniquely identified by its `order_id` or `client_order_id` (if client designs well).
    Use `stateFilter = c` to only receive create events, `stateFilter = u` to only receive update events, and `stateFilter = a` to receive both.
    """

    sub_account_id: int  # The subaccount ID to filter by
    kind: Kind  # The kind filter to apply.
    underlying: Currency  # The underlying filter to apply.
    quote: Currency  # The quote filter to apply.
    state_filter: OrderStateFilter  # create only, update only, all


@dataclass
class WSOrderFeedDataV1:
    stream: str  # Stream name
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: Order  # The order object being created or updated


@dataclass
class WSOrderStateFeedSelectorV1:
    """
    Subscribes to a feed of order updates pertaining to orders made by your account.
    Unlike the Order Stream, this only streams state updates, drastically improving throughput, and latency.
    Each Order can be uniquely identified by its `order_id` or `client_order_id` (if client designs well).
    Use `stateFilter = c` to only receive create events, `stateFilter = u` to only receive update events, and `stateFilter = a` to receive both.
    """

    sub_account_id: int  # The subaccount ID to filter by
    kind: Kind  # The kind filter to apply.
    underlying: Currency  # The underlying filter to apply.
    quote: Currency  # The quote filter to apply.
    state_filter: OrderStateFilter  # create only, update only, all


@dataclass
class OrderStateFeed:
    order_id: str  # A unique 128-bit identifier for the order, deterministically generated within the GRVT backend
    order_state: OrderState  # The order state object being created or updated


@dataclass
class WSOrderStateFeedDataV1:
    stream: str  # Stream name
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: OrderStateFeed  # The Order State Feed


@dataclass
class WSPositionsFeedSelectorV1:
    sub_account_id: int  # The subaccount ID to filter by
    kind: Kind  # The kind filter to apply.
    underlying: Currency  # The underlying filter to apply.
    quote: Currency  # The quote filter to apply.


@dataclass
class WSPositionsFeedDataV1:
    stream: str  # Stream name
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: Positions  # A Position being created or updated matching the request filter


@dataclass
class WSPrivateTradeFeedSelectorV1:
    sub_account_id: int  # The sub account ID to request for
    kind: Kind  # The kind filter to apply.
    underlying: Currency  # The underlying filter to apply.
    quote: Currency  # The quote filter to apply.


@dataclass
class WSPrivateTradeFeedDataV1:
    stream: str  # The websocket channel to which the response is sent
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: PrivateTrade  # A private trade matching the request filter


@dataclass
class Transfer:
    from_account_id: str  # The account to transfer from
    from_sub_account_id: (
        int  # The subaccount to transfer from (0 if transferring from main account)
    )
    to_account_id: str  # The account to deposit into
    to_sub_account_id: (
        int  # The subaccount to transfer to (0 if transferring to main account)
    )
    token_currency: Currency  # The token currency to transfer
    num_tokens: str  # The number of tokens to transfer
    signature: Signature  # The signature of the transfer


@dataclass
class WSTransferFeedDataV1:
    stream: str  # The websocket channel to which the response is sent
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: Transfer  # The Transfer object


@dataclass
class Deposit:
    tx_hash: str  # The hash of the bridgemint event producing the deposit
    to_account_id: str  # The account to deposit into
    token_currency: Currency  # The token currency to deposit
    num_tokens: str  # The number of tokens to deposit


@dataclass
class WSDepositFeedDataV1:
    stream: str  # The websocket channel to which the response is sent
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: Deposit  # The Deposit object


@dataclass
class Withdrawal:
    from_account_id: str  # The subaccount to withdraw from
    to_eth_address: str  # The ethereum address to withdraw to
    token_currency: Currency  # The token currency to withdraw
    num_tokens: str  # The number of tokens to withdraw
    signature: Signature  # The signature of the withdrawal


@dataclass
class WSWithdrawalFeedDataV1:
    stream: str  # The websocket channel to which the response is sent
    sequence_number: int  # A running sequence number that determines global message order within the specific stream
    feed: Withdrawal  # The Withdrawal object


@dataclass
class ApiDepositRequest:
    """
    GRVT runs on a ZKSync Hyperchain which settles directly onto Ethereum.
    To Deposit funds from your L1 wallet into a GRVT SubAccount, you will be required to submit a deposit transaction directly to Ethereum.
    GRVT's bridge verifier will scan Ethereum from time to time. Once it receives proof that your deposit has been confirmed on Ethereum, it will initiate the deposit process.

    This current payload is used for alpha testing only.
    """

    to_account_id: str  # The main account to deposit into
    token_currency: Currency  # The token currency to deposit
    num_tokens: str  # The number of tokens to deposit, quoted in token_currency decimals


@dataclass
class ApiWithdrawalRequest:
    """
    Leverage this API to initialize a withdrawal from GRVT's Hyperchain onto Ethereum.
    Do take note that the bridging process does take time. The GRVT UI will help you keep track of bridging progress, and notify you once its complete.

    If not withdrawing the entirety of your balance, there is a minimum withdrawal amount. Currently that amount is ~25 USDT.
    Withdrawal fees also apply to cover the cost of the Ethereum transaction.
    Note that your funds will always remain in self-custory throughout the withdrawal process. At no stage does GRVT gain control over your funds.
    """

    from_account_id: str  # The main account to withdraw from
    to_eth_address: str  # The Ethereum wallet to withdraw into
    token_currency: Currency  # The token currency to withdraw
    num_tokens: (
        str  # The number of tokens to withdraw, quoted in tokenCurrency decimal units
    )
    signature: Signature  # The signature of the withdrawal


@dataclass
class ApiTransferRequest:
    """
    This API allows you to transfer funds in multiple different ways<ul>
    <li>Between SubAccounts within your Main Account</li>
    <li>Between your MainAccount and your SubAccounts</li>
    <li>To other MainAccounts that you have previously allowlisted</li>
    </ul>
    """

    from_account_id: str  # The main account to transfer from
    from_sub_account_id: (
        int  # The subaccount to transfer from (0 if transferring from main account)
    )
    to_account_id: str  # The main account to deposit into
    to_sub_account_id: (
        int  # The subaccount to transfer to (0 if transferring to main account)
    )
    token_currency: Currency  # The token currency to transfer
    num_tokens: (
        str  # The number of tokens to transfer, quoted in tokenCurrency decimal units
    )
    signature: Signature  # The signature of the transfer


@dataclass
class ApiDepositHistoryRequest:
    """
    The request to get the historical deposits of an account
    The history is returned in reverse chronological order
    """

    limit: int  # The limit to query for. Defaults to 500; Max 1000
    cursor: str  # The cursor to indicate when to start the next query from
    token_currency: list[
        Currency
    ]  # The token currency to query for, if nil or empty, return all deposits. Otherwise, only entries matching the filter will be returned
    start_time: int  # The start time to query for in unix nanoseconds
    end_time: int  # The end time to query for in unix nanoseconds


@dataclass
class DepositHistory:
    tx_id: int  # The transaction ID of the deposit
    tx_hash: str  # The txHash of the bridgemint event
    to_account_id: str  # The account to deposit into
    token_currency: Currency  # The token currency to deposit
    num_tokens: str  # The number of tokens to deposit
    event_time: int  # The timestamp of the deposit in unix nanoseconds


@dataclass
class ApiDepositHistoryResponse:
    total: int  # The total number of deposits matching the request account
    next: str  # The cursor to indicate when to start the next query from
    results: list[DepositHistory]  # The deposit history matching the request account


@dataclass
class ApiTransferHistoryRequest:
    """
    The request to get the historical transfers of an account
    The history is returned in reverse chronological order
    """

    limit: int  # The limit to query for. Defaults to 500; Max 1000
    cursor: str  # The cursor to indicate when to start the next query from
    token_currency: list[
        Currency
    ]  # The token currency to query for, if nil or empty, return all transfers. Otherwise, only entries matching the filter will be returned
    start_time: int  # The start time to query for in unix nanoseconds
    end_time: int  # The end time to query for in unix nanoseconds


@dataclass
class TransferHistory:
    tx_id: int  # The transaction ID of the transfer
    from_account_id: str  # The account to transfer from
    from_sub_account_id: (
        int  # The subaccount to transfer from (0 if transferring from main account)
    )
    to_account_id: str  # The account to deposit into
    to_sub_account_id: (
        int  # The subaccount to transfer to (0 if transferring to main account)
    )
    token_currency: Currency  # The token currency to transfer
    num_tokens: str  # The number of tokens to transfer
    signature: Signature  # The signature of the transfer
    event_time: int  # The timestamp of the transfer in unix nanoseconds


@dataclass
class ApiTransferHistoryResponse:
    total: int  # The total number of transfers matching the request account
    next: str  # The cursor to indicate when to start the next query from
    results: list[TransferHistory]  # The transfer history matching the request account


@dataclass
class ApiWithdrawalHistoryRequest:
    """
    The request to get the historical withdrawals of an account
    The history is returned in reverse chronological order
    """

    limit: int  # The limit to query for. Defaults to 500; Max 1000
    cursor: str  # The cursor to indicate when to start the next query from
    token_currency: list[
        Currency
    ]  # The token currency to query for, if nil or empty, return all withdrawals. Otherwise, only entries matching the filter will be returned
    start_time: int  # The start time to query for in unix nanoseconds
    end_time: int  # The end time to query for in unix nanoseconds


@dataclass
class WithdrawalHistory:
    tx_id: int  # The transaction ID of the withdrawal
    from_account_id: str  # The subaccount to withdraw from
    to_eth_address: str  # The ethereum address to withdraw to
    token_currency: Currency  # The token currency to withdraw
    num_tokens: str  # The number of tokens to withdraw
    signature: Signature  # The signature of the withdrawal
    event_time: int  # The timestamp of the withdrawal in unix nanoseconds


@dataclass
class ApiWithdrawalHistoryResponse:
    total: int  # The total number of withdrawals matching the request account
    next: str  # The cursor to indicate when to start the next query from
    results: list[
        WithdrawalHistory
    ]  # The withdrawals history matching the request account
