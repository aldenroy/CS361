import yfinance as yf
import pandas as pd
 
 
msft = yf.Ticker("MSFT")
 
print(msft.info)