
from pycoingecko import CoinGeckoAPI
import pandas as pd
import numpy as np
from datetime import date, timedelta
import time
from crypgains.prices.price_updater import get_price_current
from crypgains.utils.write_data import write_data
from crypgains.utils.yaml_loader import yaml_loader
import yaml


def run():
    cg = CoinGeckoAPI()

    print("Running current price updater...")
    
    df = get_price_current('crypgains/resources/portfolio.yaml')

    write_data(df,'crypgains/data/prices_current')

    print("Current price updater complete.")

