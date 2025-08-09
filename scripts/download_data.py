import yfinance as yf
import pandas as pd
from pathlib import Path
import pytz
from datetime import datetime

def download_gold_history(start_date="2025-08-01", interval="60m", save_path="data/gold_price_history.csv"):
    # Convert input start_date (UTC) string to datetime
    utc = pytz.utc
    ny_tz = pytz.timezone('America/New_York')
    
    start_utc = datetime.strptime(start_date, "%Y-%m-%d")
    start_ny = utc.localize(start_utc).astimezone(ny_tz)
    start_ny_naive = start_ny.replace(tzinfo=None)
    start_ny_str = start_ny_naive.strftime("%Y-%m-%d")
    
    df = yf.download("GC=F", interval=interval, start=start_ny_str)
    df = df[["Close"]].rename(columns={"Close": "Gold Price"})
    
    if df.index.tz is None:
        df.index = df.index.tz_localize('America/New_York').tz_convert('UTC')
    else:
        df.index = df.index.tz_convert('UTC')
    
    # Create a complete hourly datetime index from start to end
    full_index = pd.date_range(start=df.index[0], end=df.index[-1], freq='60min', tz='UTC')
    
    # Reindex to full index and forward fill missing data
    df = df.reindex(full_index).ffill()
    
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(save_path)
    
    return df
    