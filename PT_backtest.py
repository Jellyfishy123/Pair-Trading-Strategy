from AlgoAPI import AlgoAPI_Backtest
from strategy import AlgoEvent  # Make sure this matches your filename
import os

if __name__ == "__main__":
    # Initialize the backtest environment
    print("Starting Pair Trading Backtest...")

    backtest = AlgoAPI_Backtest.AlgoBacktest()

    # === CONFIGURATION ===
    strategy_name = "demo_PairTrade"
    start_date = "2017-01"
    end_date = "2017-12"
    instruments = ['SPXUSD', 'NSXUSD']  # SP500 and NASDAQ100
    data_interval = "1d"  # Daily data
    base_currency = "USD"
    initial_capital = 1_000_000  # USD
    leverage = 1
    commission = 0.0
    allow_short = True

    # === Setup ===
    backtest.setStrategyName(strategy_name)
    backtest.setStartDate(start_date)
    backtest.setEndDate(end_date)
    backtest.setDataInterval(data_interval)
    backtest.setBaseCurrency(base_currency)
    backtest.setInitialCash(initial_capital)
    backtest.setLeverage(leverage)
    backtest.setCommission(commission)
    backtest.setAllowShortSell(allow_short)

    # Load data for both instruments
    for instrument in instruments:
        data_path = os.path.join("data", f"{instrument}_1day.csv")  # Update path if needed
        backtest.loadMarketDataFromFile(data_path, instrument)

    # Subscribe instruments
    backtest.setSubscribeInstrumentList(instruments)

    # Run the strategy
    strategy = AlgoEvent()
    strategy.start(backtest)

    # Run backtest
    backtest.runBacktest()

    # === Results ===
    print("Backtest Complete.")
    print("Final Cash:", backtest.getCash())
    print("Total P&L:", backtest.getTotalPL())
    print("Open Positions:", backtest.getOpenPositions())

    # Export performance (optional)
    backtest.exportPL("pair_trade_results.csv")
