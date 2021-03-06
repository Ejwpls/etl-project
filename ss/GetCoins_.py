# %%
# import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json
from io import StringIO
from bs4 import BeautifulSoup

def get_coins_():
    url = "https://whattomine.com/coins.json?eth=true&factor%5Beth_hr%5D=90.0&factor%5Beth_p%5D=420.0&e4g=true&factor%5Be4g_hr%5D=90.0&factor%5Be4g_p%5D=420.0&zh=true&factor%5Bzh_hr%5D=63.0&factor%5Bzh_p%5D=360.0&cnh=true&factor%5Bcnh_hr%5D=2880.0&factor%5Bcnh_p%5D=330.0&cng=true&factor%5Bcng_hr%5D=2280.0&factor%5Bcng_p%5D=360.0&cnf=true&factor%5Bcnf_hr%5D=4950.0&factor%5Bcnf_p%5D=330.0&cx=true&factor%5Bcx_hr%5D=3.3&factor%5Bcx_p%5D=360.0&eqa=true&factor%5Beqa_hr%5D=285.0&factor%5Beqa_p%5D=360.0&cc=true&factor%5Bcc_hr%5D=7.8&factor%5Bcc_p%5D=390.0&cr29=true&factor%5Bcr29_hr%5D=7.2&factor%5Bcr29_p%5D=390.0&ct31=true&factor%5Bct31_hr%5D=1.8&factor%5Bct31_p%5D=360.0&ct32=true&factor%5Bct32_hr%5D=0.48&factor%5Bct32_p%5D=360.0&eqb=true&factor%5Beqb_hr%5D=46.5&factor%5Beqb_p%5D=420.0&rmx=true&factor%5Brmx_hr%5D=1410.0&factor%5Brmx_p%5D=270.0&ns=true&factor%5Bns_hr%5D=2460.0&factor%5Bns_p%5D=450.0&al=true&factor%5Bal_hr%5D=177.0&factor%5Bal_p%5D=390.0&ops=true&factor%5Bops_hr%5D=14.7&factor%5Bops_p%5D=360.0&eqz=true&factor%5Beqz_hr%5D=42.0&factor%5Beqz_p%5D=390.0&zlh=true&factor%5Bzlh_hr%5D=42.0&factor%5Bzlh_p%5D=360.0&kpw=true&factor%5Bkpw_hr%5D=39.0&factor%5Bkpw_p%5D=510.0&ppw=true&factor%5Bppw_hr%5D=28.2&factor%5Bppw_p%5D=420.0&x25x=true&factor%5Bx25x_hr%5D=2.49&factor%5Bx25x_p%5D=240.0&fpw=true&factor%5Bfpw_hr%5D=43.5&factor%5Bfpw_p%5D=510.0&vh=true&factor%5Bvh_hr%5D=1.32&factor%5Bvh_p%5D=360.0&factor%5Bcost%5D=0.1&factor%5Bcost_currency%5D=USD&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset="

    # Build partial query URL
    _response = requests.get(url)
    _json = _response.json()

    coins = _json['coins']
    
    # Convert to dataframe and transpose
    _json_df = pd.DataFrame(coins).T

    df = _json_df[['id','tag','algorithm','block_time','block_reward','nethash','timestamp']]
    
    return df

# %%
def get_hashrate_():
    #Get GPU hasrates
    page = requests.get('https://whattomine.com/gpus')

    b = page.content
    df_list = pd.read_html(b)
    df = df_list[-1]

    df2 = df[['Model','Hashrate']]

    df123 = df2['Hashrate'].str.split(" ", expand=True)

    return df2

# %%
def get_hashrate2_():
    # URL of page to be scraped with pandas
    url = 'https://www.hashrate.no/'
    tables = pd.read_html(url)
    df3 = tables[1]
    df3 = df3[['Model','Coin','Hashrate','Power','Efficiency']]
    return df3

#%%
df= get_coins_()
print(df)