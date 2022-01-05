
from pycoingecko import CoinGeckoAPI
import pandas as pd
import numpy as np
from datetime import date, timedelta
import time
from crypgains.prices.price_updater import get_price_history
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

    print("---Portfolio---")
    for crypto in cryptos:
        print(crypto, " - token volume: ", portfolio[crypto])

    print("Running Historical price updater...")

    dfs = []

    for crypto in cryptos:  
        df = get_price_history(crypto,sunixtime,eunixtime)
        dfs.append(df)

    comb = pd.concat(dfs)
    
    print(f"Number of months found: {np.round((len(comb) / len(portfolio))/12,1)}")
    print(f"Minimum Date found: {comb.dt.min()}")
    print(f"Maximum Date found: {comb.dt.max()}")

    write_data(comb,'crypgains/data/prices_historical')
    print("Historical price updater complete.")
