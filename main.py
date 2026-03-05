import market_data_fetch as mdf
import ma_calc as mc
import mac_tracker as mt
import backtester as bt

Tickers=["TCS.NS","NVDA","BTC-USD"]
TimePeriods=["1000d","5y","max"]
fast_slow=[[5,20], [10,50], [50,200]]

for ticker in Tickers:
    for time in TimePeriods:
        raw=mdf.fetch(ticker,time)
        if raw is None:
            continue
        for r in fast_slow:
            print(f"For the ticker {ticker} over a time period of {time} with FastMA for {r[0]} days and SlowMA for {r[1]} days the report is:")
            enriched=mc.MA(raw,r[0],r[1])
            final=mt.tracker(enriched)
            rep=bt.report(final)
            print(f"Total RoI over the Time Period: {rep[0]:.2f}%")
            print(f"CAGR over the Time Period of {time}: {rep[1]:.2f}%")
            print(f"WinRate over the Time Period of {time}: {rep[2]:.2f}%")
            print(f"Total trades made over the Time Period of {time}: {rep[3]}")
            print("----------------X----------------")
        print("----------------X----------------")
    print("----------------X----------------")