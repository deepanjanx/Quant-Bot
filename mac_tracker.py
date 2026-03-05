import pandas as pd
import numpy as np

def tracker(df):
    buy_signal=(df["FastMA"] > df["SlowMA"]) & (df["FastMA"].shift(1) <= df["SlowMA"].shift(1)) #create a list where buy signal i.e. we should buy we have t else f
    sell_signal=(df["FastMA"] < df["SlowMA"]) & (df["FastMA"].shift(1) >= df["SlowMA"].shift(1)) #create a list where sell signal i.e. we should sell we have t else f
    df["Signal"]=np.nan
    df.loc[buy_signal,"Signal"]=1 
    df.loc[sell_signal,"Signal"]=0 
    df['Position'] = df['Signal'].ffill().fillna(0).astype(int) 
    return df