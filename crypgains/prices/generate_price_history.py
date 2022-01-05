
from pycoingecko import CoinGeckoAPI
import pandas as pd
import numpy as np
from datetime import date, timedelta
import time
from crypgains.prices.get_price_history import get_price_history
from crypgains.utils.write_data import write_data
from crypgains.utils.yaml_loader import yaml_loader
import yaml


def run():
    cg = CoinGeckoAPI()

    sdate = date(2017,1,1) # start date
    edate = date.today() # end date

    sunixtime = time.mktime(sdate.timetuple())
    eunixtime = time.mktime(edate.timetuple())

    # Read YAML file
    portfolio = yaml_loader('crypgains/resources/portfolio.yaml')

    cryptos = list(portfolio.keys())

    for crypto in cryptos:
        print("Crypto found: ",crypto)

    dfs = []

    for crypto in cryptos:  
        df = get_price_history(crypto,sunixtime,eunixtime)
        dfs.append(df)

    write_data(pd.concat(dfs),'crypgains/data/historical_prices')

