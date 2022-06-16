# %%
# Dependencies
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import time
import pandas as pd


# %%
# Define database and collection
#db = client.cycling_db
#collection = db.articles
def get_GPUCost():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit ple.com.au
    url = 'https://www.ple.com.au/Categories/259/Graphics-Cards'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Retrieve the parent divs for product
    results = soup.find_all('div', class_="itemGridTileWrapper tileStandard")

    

    # Create empty dataframe with defined name
    df = pd.DataFrame(columns = ['GPU_name', 'GPU_cost'])

    # Iterate through the results, based on soup 
    for result in results:
        #scarpe the item & price of each product
        item_ = result.find_all('div', class_= 'itemGridTileDescription')[0].text
        price_ = result.find_all('div', class_= 'itemGridTilePrice')[0].find('span').get_text().strip('$')

        df.loc[len(df),'GPU_name'] = item_
        df.loc[len(df)-1,'GPU_cost'] = price_
    
    # TRANSFORM: Split string to put into different columns & rename columns 
    df1 = df['GPU_name'].str.split(" ", n =1, expand=True)
    df1 = df1.rename(columns={0:'GPU_make',1:'GPU_name'})

    # Assign new column to 'df' from the split and Update the name column
    df['GPU_name'] = df1['GPU_name']
    df['GPU_make'] = df1['GPU_make']

    #Pass back dataframe
    return df

