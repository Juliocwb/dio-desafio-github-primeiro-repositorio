import pandas_datareader.data as web
import yfinance as yf

yf.pdr_override()

df_ibov = web.get_data_yahoo('^BVSP')

df_ibov.tail()