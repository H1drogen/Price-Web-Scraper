import requests
from bs4 import BeautifulSoup
import urllib.parse

def ebay_title_and_price(product_name):
    search_url = f"https://www.ebay.com/sch/i.html?_nkw={urllib.parse.quote_plus(product_name)}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'accept-language': 'en-GB,en;q=0.5',
    }

    search_response = requests.get(search_url, headers=headers)
    search_soup = BeautifulSoup(search_response.text, 'html.parser')

    product_url = search_soup.find("a", {"class": "s-item__link"})['href']

    product_response = requests.get(product_url, headers=headers)
    product_soup = BeautifulSoup(product_response.text, 'html.parser')

    title = product_soup.find("h1", {"class": "it-ttl"}).text.strip()
    price = product_soup.find("span", {"class": "notranslate"}).text.strip()

    return title, price

product_name = 'iphone 12'
title, price = ebay_title_and_price(product_name)
print(f'Title: {title}\nPrice: {price}')