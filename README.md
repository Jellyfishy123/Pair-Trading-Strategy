# 🔁 Pair Trading Strategy – `demo_PairTrade`

This repository showcases a simple **pair trading algorithm** using the AlgoAPI backtesting framework. The strategy demonstrates a market-neutral trading approach by analyzing the relative price movement between **SP500 (SPXUSD)** and **NASDAQ100 (NSXUSD)**.

---

## 📘 Strategy Concept

**Pair trading** is a popular market-neutral strategy that dates back to the 1980s. It exploits the **spread between two correlated instruments** — profiting not from directional market moves, but from **relative mispricing** between the two assets.

Key characteristics:
- Profit is generated when the spread between two assets **converges**.
- It is designed to be **market neutral**, meaning it can perform well in **bull, bear, or sideways markets**.

---

## 🔍 Strategy Logic

This implementation assumes that **SPXUSD** and **NSXUSD** are a statistically viable trading pair.

### ✅ Core logic steps:

1. **Model**: Use **Simple Linear Regression (SLR)** without intercept  
   \[
   \text{SPXUSD} = b \times \text{NSXUSD}
   \]

2. **Determine trade size**:
   - Coefficient \( b \) is used as the **position size multiplier** for the second asset.
   - This aligns trade size to maintain **market neutrality**.

3. **Divergence detection**:
   - The residual \( e = Y - bX \) is computed daily.
   - If the residual exceeds a **threshold**, the strategy opens a pair of trades:
     - Long the underpriced asset
     - Short the overpriced asset
   - Positions are closed once **profit target** is met.

4. **Execution & Monitoring**:
   - Strategy runs on **daily data** using the `on_bulkdatafeed` method.
   - Unfilled orders and net positions are constantly checked to maintain balance.

---

## 🧮 Strategy Highlights

- Uses **Statsmodels** for regression
- Automatically calculates and rebalances **pair trade sizing**
- **Trade reset logic** to manage misaligned or stale positions
- Handles **daily data** for simplified testing and interpretation

---

## ⚙️ Backtest Configuration

| Setting             | Value                    |
|---------------------|--------------------------|
| Strategy Name       | `demo_PairTrade`         |
| Instruments         | `['SPXUSD', 'NSXUSD']`   |
| Backtest Period     | `2017-01` to `2017-12`   |
| Data Interval       | 1 day                    |
| Initial Capital     | 1,000,000 USD            |
| Base Currency       | USD                      |
| Leverage            | 1                        |
| Transaction Cost    | 0                        |
| Allow Short Selling | Yes                      |

---


