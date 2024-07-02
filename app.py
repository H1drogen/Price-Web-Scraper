from flask import Flask
from Scrapers.Amazon import AmazonScraper
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/tech/<product_url>')
def amazon_scraper(product_url):
    # product_url = asyncio.run(run('product name'))
    amazon_title, amazon_price = AmazonScraper(product_url)


if __name__ == '__main__':
    app.run()
