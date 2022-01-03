
from pycoingecko import CoinGeckoAPI
import pandas as pd
import numpy as np

cg = CoinGeckoAPI()

def get_price_history(crypto,s,e):

    '''
    Grabs the prices for a certain crypto and will transform as necessary
    
    args:
        Crypto: Ticker symbol of crypto_currency
        s: Start Date
        e: End Date

    returns:
        pd.DataFrame

    '''

    #Grab prices from API
    price = cg.get_coin_market_chart_range_by_id(id=crypto,from_timestamp=s,to_timestamp=e,vs_currency='gbp')
    
    #Turn into pandas df object
    df = pd.DataFrame.from_dict(price.get('prices'))

    #Set cypto as column
    df['crypto'] = crypto 

    #Rename columns
    df.columns = ['dt','price_gbp','crypto']

    #Set datetime
    df['dt'] = pd.to_datetime(df['dt'],unit='ms')

    return df

