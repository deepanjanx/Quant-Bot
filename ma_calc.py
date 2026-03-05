import pandas as pd

# Adds the MAs into the dataframe
def MA(df,fast=50,slow=200):
    df["FastMA"]=df["Adj Close"].rolling(window=fast).mean()
    df["SlowMA"]=df["Adj Close"].rolling(window=slow).mean()
    return df