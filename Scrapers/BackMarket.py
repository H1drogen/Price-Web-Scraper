import requests
from bs4 import BeautifulSoup
import urllib.parse

def backmarket_title_and_price(product_name):
    search_url = f"https://www.backmarket.com/search?q={urllib.parse.quote_plus(product_name)}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'accept-language': 'en-GB,en;q=0.5',
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # These selectors depend on the actual structure of the BackMarket website and may need adjustment
    htmlTitles = soup.find_all("a", {"class": "product-item-link"})
    htmlPrices = soup.find_all("span", {"class": "price"})

    titles = [title.text.strip() for title in htmlTitles]
    prices = [price.text.strip() for price in htmlPrices]

    return titles, prices

product_name = 'iphone 12'
title, price = backmarket_title_and_price(product_name)
print(f'Title: {title}\nPrice: {price}')
