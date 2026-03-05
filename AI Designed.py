import pandas as pd
import matplotlib.pyplot as plt
import market_data_fetch as mdf
import ma_calc as mc
import mac_tracker as mt
import backtester as bt


# This is an AI generated file for the purposes of showcasing capabilities of the rest of the modules designed by me, to see a basic code demonstration check out main.py
def run_optimization():
    Tickers = ["TCS.NS", "NVDA", "BTC-USD"]
    TimePeriods = ["1000d", "5y", "max"] # Simplified for a cleaner chart
    fast_slow = [[5,20], [10,50], [50,200]]

    master_results = []
    print("Initializing Data Analytics Engine... Please wait.\n")

    # Phase 1: Grid Search to find the optimal metrics
    for ticker in Tickers:
        for time in TimePeriods:
            for r in fast_slow:
                raw = mdf.fetch(ticker, time)
                if raw is None or raw.empty:
                    continue
                    
                enriched = mc.MA(raw, r[0], r[1])
                final = mt.tracker(enriched)
                rep = bt.report(final)
                
                master_results.append({
                    "Ticker": ticker,
                    "Time_Period": time,
                    "Fast_MA": r[0],
                    "Slow_MA": r[1],
                    "Total_ROI_%": rep[0],
                    "CAGR_%": rep[1],
                    "Win_Rate_%": rep[2],
                    "Total_Trades": rep[3]
                })

    df = pd.DataFrame(master_results)
    basket = []

    print(f"{'='*80}\nOPTIMIZATION REPORT\n{'='*80}")

    # Phase 2: Extracting the absolute best configurations
    for ticker in Tickers:
        ticker_df = df[df["Ticker"] == ticker]
        if ticker_df.empty:
            continue
            
        overall_best_idx = ticker_df["CAGR_%"].idxmax()
        overall_best = ticker_df.loc[overall_best_idx]
        
        print(f"[{ticker}] Optimal: {overall_best['Time_Period']} | Fast: {overall_best['Fast_MA']} | Slow: {overall_best['Slow_MA']} | CAGR: {overall_best['CAGR_%']:.2f}% | Win Rate: {overall_best['Win_Rate_%']:.2f}%")
        
        basket.append(overall_best.to_dict())

    # Phase 3: Visualizing the optimal strategies
    print(f"\n{'='*80}\nGENERATING EQUITY CURVE VISUALIZATIONS\n{'='*80}")
    
    plt.figure(figsize=(14, 8))
    plt.style.use('dark_background') # Gives it a professional quantitative terminal look
    
    for best in basket:
        ticker = best["Ticker"]
        time = best["Time_Period"]
        fast = best["Fast_MA"]
        slow = best["Slow_MA"]
        
        # Re-fetch and process only the winning configurations to get the daily Equity data
        raw = mdf.fetch(ticker, time)
        enriched = mc.MA(raw, fast, slow)
        tracked = mt.tracker(enriched)
        
        # Call impdataadder directly to get access to the "Equity" column
        final_data = bt.impdataadder(tracked, EqIn=10000)
        
        # Plot the equity curve over time
        plt.plot(final_data.index, final_data["Equity"], label=f"{ticker} (MA {fast}/{slow}) - CAGR: {best['CAGR_%']:.1f}%", linewidth=2)

    # Formatting the Chart
    plt.title("Moving Average Crossover Strategy - Optimal Configurations", fontsize=16, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Portfolio Value ($)", fontsize=12)
    plt.legend(loc="upper left", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Automatically formats dates nicely on the X-axis
    plt.gcf().autofmt_xdate() 
    
    print("Plot generated. Displaying window...")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_optimization()