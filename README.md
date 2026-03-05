# Quant Bot: Vectorized MAC Backtesting Engine

A professional-grade, highly modular, and fully vectorized quantitative backtesting engine built in Python. This system evaluates Moving Average Crossover (MAC) strategies across multiple assets, timeframes, and moving average lengths to identify statistically optimal trading configurations.

## 🤖 Prompt Engineering & AI Collaboration

This project was built to showcase a hybrid approach to modern software engineering, translating strict Technical Requirements into a production-ready pipeline:

- **The Core Engine** (`market_data_fetch.py`, `ma_calc.py`, `mac_tracker.py`, `backtester.py`, and `main.py`) was engineered entirely by me. My focus here was on strict vectorization, data architecture, and squashing quantitative bugs like Look-Ahead Bias.
    
- **The Showcase Wrapper** (`AI Designed.py`) is a product of **prompt engineering**. After building the core logic, I directed an AI to design a visualization wrapper that imports my modules, runs grid-search optimizations, and plots Matplotlib equity curves. This demonstrates my ability to build robust foundational systems and leverage AI to rapidly develop UI and data-visualization layers on top of them.
    

## 🏗️ Architecture & Pipeline

This project is built with strict separation of concerns, ensuring that data ingestion, state calculation, signal tracking, and performance accounting are isolated into functional modules.

- **`market_data_fetch.py` (Data Boundary):** Interfaces with the Yahoo Finance API (`yfinance`) to pull historical time-series data, ensuring fallback handlers for missing tickers.
    
- **`ma_calc.py` (State Calculation):** Enriches the tabular data with parameterized Fast and Slow Moving Averages using the `Adjusted Close` to protect against corporate actions (stock splits/dividends).
    
- **`mac_tracker.py` (Logic Engine):** Identifies Golden Crosses and Death Crosses using **100% vectorized Pandas operations**. It entirely avoids `for`-loops for maximum computational efficiency across massive datasets.
    
- **`backtester.py` (Accounting Engine):** Simulates a trading portfolio, accurately calculating geometric compounding (Equity), Total ROI, CAGR, Maximum Drawdown, and Win Rates, while strictly preventing Look-Ahead Bias via shifted positional alignment.
    
- **`main.py` (Core Orchestrator):** The primary execution script that links the modules together and runs discrete backtests.
    
- **`AI Designed.py` (Optimization Showcase):** The prompt-engineered wrapper that conducts automated grid-search optimization across various ticker and MA combinations, outputting the most profitable strategies and generating Matplotlib equity curves.
    

## 🚀 Key Engineering Features

- **Zero `for`-loops in Data Tracking:** Utilizes boolean masking and `.shift()` operations to process decades of daily price data in milliseconds.
    
- **Look-Ahead Bias Prevention:** Positions are mathematically shifted by $t+1$ to ensure trades are executed _after_ a signal is generated, simulating realistic market constraints.
    
- **Burn-in Period Handling:** Safely manages the initial `NaN` values required to calculate long-term moving averages, ensuring the portfolio strictly starts in a 100% Cash state.
    

## 💻 Installation & Usage

1. Clone the repository:
    

```
git clone [https://github.com/yourusername/quant-bot.git](https://github.com/yourusername/quant-bot.git)
cd quant-bot
```

2. Install the required dependencies:
    

```
pip install pandas yfinance matplotlib numpy
```

3. Run the core engine for discrete testing:
    

```
python main.py
```

4. Run the AI-designed optimizer to test assets and view the generated equity curves:
    

```
python "AI Designed.py"
```

## 📊 Results & Optimal Configurations

The engine ran an automated grid search across `TCS.NS`, `NVDA`, and `BTC-USD` to find the highest-yielding Moving Average combinations.

**Optimal Strategy Basket:** | Asset | Time Period | Fast MA | Slow MA | CAGR (%) | Win Rate (%) | | :--- | :--- | :--- | :--- | :--- | :--- | | **NVDA** | 1000 Days | 50 | 200 | 63.72% | 100.00% | | **BTC-USD** | Max (All-Time) | 10 | 50 | 65.68% | 48.98% | | **TCS.NS** | Max (All-Time) | 50 | 200 | 16.04% | 63.64% |

### Equity Curve Visualization

_The chart below is generated automatically by `AI Designed.py`, comparing the $10,000 starting portfolio growth across the optimal configurations._
