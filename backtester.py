import pandas as pd
from datetime import date

def impdataadder(df,EqIn:int=10000):
    df["ROI"]=(df["Adj Close"]-df["Adj Close"].shift(1))/(df["Adj Close"].shift(1))
    df["ROIStrat"] = df["ROI"] * df["Position"].shift(1)
    df["Equity"] = EqIn * (1 + df["ROIStrat"].fillna(0)).cumprod()
    df["Peak"]=df["Equity"].cummax()
    df["Drawdown"]=((df["Peak"]-df["Equity"])/(df["Peak"]))*100
    return df

def calc_winRate(df):
    df['Trade Change']=df["Position"].diff()
    entries=df[df['Trade Change']==1]['Adj Close']
    exits=df[df['Trade Change']==-1]['Adj Close']
    if len(entries)>len(exits):
        exits=pd.concat([exits, pd.Series([df['Adj Close'].iloc[-1]])])
    trade_returns=(exits.values - entries.values)/entries.values
    wins=(trade_returns>0).sum()
    total_trades=len(trade_returns)
    win_rate=(wins/total_trades)*100 if total_trades>0 else 0
    return win_rate,total_trades

def report(df):
    df=impdataadder(df)
    EqIn= df['Equity'].iloc[0]
    EqFin= df['Equity'].iloc[-1]
    TRoI=(EqFin-EqIn)/EqIn*100
    CAGRoI=((EqFin/EqIn)**(365/((df.index[-1] - df.index[0]).days))-1)*100
    win_rate,total_trades=calc_winRate(df)
    return [float(TRoI),float(CAGRoI),float(win_rate),int(total_trades)]