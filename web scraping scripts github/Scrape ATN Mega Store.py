import pandas as pd
import requests
from bs4 import BeautifulSoup 

url = 'https://atnmegastore.ca/products/books/page/{x}/'

books = []

for x in range(1,175):
    response = requests.get(url.format(x=x))

    soup = BeautifulSoup(response.content,'html.parser')

    for item in soup.select('.product .product-details'):
        book = {}
        book['title'] = item.select('h3 a')[0].text.strip()
        book['price'] = item.select('.price')[0].text
        book['url'] = item.select('h3 a')[0]['href']
        book['image url'] = item.parent.parent.select('img')[0]['src']
        books.append(book)

books = pd.DataFrame(books)

books.to_csv('/Users/rakeenahmed/Library/CloudStorage/GoogleDrive-rakeenaahmed@gmail.com/My Drive/Learning/Web Scraping/books.csv')