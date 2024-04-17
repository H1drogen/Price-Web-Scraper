import requests
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

def AmazonScraper(url):
    url = 'https://www.amazon.co.uk/Intel%C2%AE-CoreTM-i9-12900F-Desktop-Processor/dp/B09MDFH5HY/ref=sr_1_1_sspa?crid=15BOJBU34RP30&dib=eyJ2IjoiMSJ9.aG27SdaOhKl1C6IQGZWQVIBNrZVqDLlVVgNSaRcPdeVpPBg9zUyhnrYcprQqFl2Tsb_rqqN0W5rISuUYRaH3wskxImq3l-ziOfwzCMB0P79aMi2m5IjuXNPm-50o8CWuedSS63RcJP3KwjU9syH1uOzWsYbarI2uh4nn-NqnCBPEotNrXx7zkOacnLk1ck5iinEpX5PZHEvymcAunlBM8dsGPrBgJ-etlphMEZ6Fw2I.HJjDesTgG4xAiH2KhPhQB_v5HwPWwuCU7tLjhq7cpgs&dib_tag=se&keywords=intel+cpu&qid=1711734105&sprefix=intel+cpu%2Caps%2C70&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'accept-language': 'en-GB,en;q=0.5',
    }

    response = requests.get(url, headers=custom_headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.select_one('#productTitle').text.strip()
    price = soup.select_one('span.a-offscreen').text

    print(title, price)

AmazonScraper('https://www.amazon.co.uk/Intel%C2%AE-CoreTM-i9-12900F-Desktop-Processor/dp/B09MDFH5HY/ref=sr_1_1_sspa?crid=15BOJBU34RP30&dib=eyJ2IjoiMSJ9.aG27SdaOhKl1C6IQGZWQVIBNrZVqDLlVVgNSaRcPdeVpPBg9zUyhnrYcprQqFl2Tsb_rqqN0W5rISuUYRaH3wskxImq3l-ziOfwzCMB0P79aMi2m5IjuXNPm-50o8CWuedSS63RcJP3KwjU9syH1uOzWsYbarI2uh4nn-NqnCBPEotNrXx7zkOacnLk1ck5iinEpX5PZHEvymcAunlBM8dsGPrBgJ-etlphMEZ6Fw2I.HJjDesTgG4xAiH2KhPhQB_v5HwPWwuCU7tLjhq7cpgs&dib_tag=se&keywords=intel+cpu&qid=1711734105&sprefix=intel+cpu%2Caps%2C70&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')


# async def AmazonURL(product_name):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#
#         # Navigate to Amazon's homepage
#         await page.goto('https://www.amazon.com')
#
#         # Find the search bar, type in the product name, and submit the search
#         await page.fill('#twotabsearchtextbox', product_name)
#         await page.press('#twotabsearchtextbox', 'Enter')
#
#         # Wait for the search results page to load
#         await page.wait_for_load_state('networkidle')
#
#         # Collect the URL of the first product in the search results
#         first_product = await page.query_selector('.s-result-item .a-link-normal')
#         first_product_url = await first_product.get_attribute('href')
#
#         await browser.close()
#
#         return first_product_url
#

# product_url = asyncio.run(AmazonURL('Intel Core i9 12900F'))
