import requests
from bs4 import BeautifulSoup
import urllib.parse

def gumtree_title_and_price(product_name):
    search_url = f"https://www.gumtree.com/search?search_category=all&q={urllib.parse.quote_plus(product_name)}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'accept-language': 'en-GB,en;q=0.5',
    }

    search_response = requests.get(search_url, headers=headers)
    search_soup = BeautifulSoup(search_response.text, 'html.parser')

product_name = 'iphone 12'
title, price = gumtree_title_and_price(product_name)
print(f'Title: {title}\nPrice: {price}')