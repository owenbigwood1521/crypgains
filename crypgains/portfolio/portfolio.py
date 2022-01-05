import yaml
from crypgains.utils.yaml_loader import yaml_loader
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 99999)

def calculate_total(loc):

    #Loads Portfolio    
    config = yaml_loader(loc)
    portfolio = pd.DataFrame.from_dict(config,orient='index')
    portfolio.reset_index(level=0, inplace=True)
    portfolio.columns = ['crypto','holdings']

    #Loads prices currently of Crytos in portfolio
    prices = pd.read_csv('crypgains/data/prices_current.csv')

    #Merging them together
    result = pd.merge(portfolio, prices, on="crypto")

    #Calculates for each Crypto an overall value
    result['value'] = result['holdings'] * result['price_gbp']

    result.style.set_properties(**{'text-align': 'center'})

    print('Individual holdings:')
    print(tabulate(result.sort_values(by=['value'],ascending=False), headers='keys', tablefmt='fancy_grid'))

    print('Overall Value:')
    print("£",np.round(result.value.sum(),-1))



