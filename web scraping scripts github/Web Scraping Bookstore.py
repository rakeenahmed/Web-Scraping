import pandas as pd
import requests
from bs4 import BeautifulSoup 

url = 'http://books.toscrape.com/catalogue/page-{x}.html'

products = [] #products list needs to be outside the for loop to prevent creating empty lists for each page

#the whole script has to be inside a giant for loop
#looping through the pages
for x in range(1,50):
    response = requests.get(url.format(x=x))    

    #creating the beautiful soup object
    soup = BeautifulSoup(response.content,'html.parser')

    #grabbing all titles that have a minimum 2 star rating and above
    for item in soup.find_all('article',class_='product_pod'):
        if item.find('p',class_=['star-rating Two', 'star-rating Three', 'star-rating Four', 'star-rating Five']):
            products.append(item.h3.a['title'])
        else:
            continue
    products

#creating a dataframe for books
books = pd.DataFrame(products,columns=['Title'])

#saving dataframe as csv file
books.to_csv('/Users/rakeenahmed/Library/CloudStorage/GoogleDrive-rakeenaahmed@gmail.com/My Drive/Learning/Web Scraping/books.csv')
