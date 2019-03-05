from splinter import Browser
from bs4 import BeautifulSoup 
import time
import numpy as np
import pandas as pd

def init_browser():
    browser = Browser("chrome", headless=False)

# File to Load- obtain brewery csv
file_to_load2 = "breweries.csv"

#Make into dataframe
brewery_pd = pd.read_csv(file_to_load2, encoding="utf-8")
brewery_pd.head()


#Drop unnecessary columns. We want the brewery name
brewery1_df = brewery_pd.drop(columns=['Unnamed: 0'])
brewery1_df['rating'] = ''

def scrape_info():

#Create a random sample of 20 breweries
brewery2_df = brewery1_df.sample(20, random_state=0).copy()

base_url = 'https://untappd.com/'


for index, record in brewery2_df.iterrows():
    try:
        brewery = record['name']
        search_url = base_url + f'search?q={brewery}&type=brewery&sort='
        browser.visit(search_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        rating = soup.find('span', class_="num").get_text()
        brewery2_df.loc[index, 'rating'] = rating.strip("(").strip(")")
    except (AttributeError):
        print('No Values')
    
print(brewery2_df)


