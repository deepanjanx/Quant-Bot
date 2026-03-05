import yfinance as yf

#the fetch function
def fetch(tic:str,tp:str):
    stc=yf.Ticker(tic)
    his=stc.history(period=tp,auto_adjust=False)
    if his.empty:
        return None
    else:
        if "Adj Close" not in his.columns:
            his["Adj Close"] = his["Close"]
        return his