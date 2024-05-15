import requests
from bs4 import BeautifulSoup
import urllib.parse

def ebay_title_and_price(product_name):
    search_url = f"https://www.ebay.com/sch/i.html?_nkw={urllib.parse.quote_plus(product_name)}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'accept-language': 'en-GB,en;q=0.5',
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    htmlTitles = soup.find_all("div", {"class": "s-item__title"})
    htmlPrices = soup.find_all("span", {"class": "s-item__price"})
    # htmlUndiscountedPrice = soup.find_all("span", {"class": "STRIKETHROUGH"})
    # htmlCondition = soup.find_all("class", {"class": "SECONDARY_INFO"})
    # htmlShipping = soup.find_all("class", {"class": "s-item__shipping s-item__logisticsCost"})

    title = []
    price = []

    # collect the first 3 titles and prices
    for i in range(1, 3):
        title.append(htmlTitles[i].text)
        price.append(htmlPrices[i].text)

    return title, price

product_name = 'iphone 12'
title, price = ebay_title_and_price(product_name)
print(f'Title: {title}\nPrice: {price}')