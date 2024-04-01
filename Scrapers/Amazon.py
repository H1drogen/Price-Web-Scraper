import requests

url = 'https://www.amazon.co.uk/Intel%C2%AE-CoreTM-i9-12900F-Desktop-Processor/dp/B09MDFH5HY/ref=sr_1_1_sspa?crid=15BOJBU34RP30&dib=eyJ2IjoiMSJ9.aG27SdaOhKl1C6IQGZWQVIBNrZVqDLlVVgNSaRcPdeVpPBg9zUyhnrYcprQqFl2Tsb_rqqN0W5rISuUYRaH3wskxImq3l-ziOfwzCMB0P79aMi2m5IjuXNPm-50o8CWuedSS63RcJP3KwjU9syH1uOzWsYbarI2uh4nn-NqnCBPEotNrXx7zkOacnLk1ck5iinEpX5PZHEvymcAunlBM8dsGPrBgJ-etlphMEZ6Fw2I.HJjDesTgG4xAiH2KhPhQB_v5HwPWwuCU7tLjhq7cpgs&dib_tag=se&keywords=intel+cpu&qid=1711734105&sprefix=intel+cpu%2Caps%2C70&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'accept-language': 'en-GB,en;q=0.5',
}

response = requests.get(url, headers=custom_headers)

print(response.text)