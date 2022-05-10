from email import header
import urllib
from numpy import product
from pyparsing import Combine
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import csv


url = "https://yoshops.com/t/food"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,'html.parser')

lists = soup.find_all('div',class_ = 'col-sm-3 col-xs-6')
fieldnames = ['product name','product link','product price']
with open('newshop.csv','w',encoding='UTF8',newline='')as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for list in lists:
        product = list.find('span',class_='product-title').text
        product_link = list.find('a',class_='product-link').get('href')
        root_url = 'https://yoshops.com'
        Combine_link = root_url + product_link
        product_price = list.find('div',class_='product-price')
        product_price_a = product_price.find('span').text
        product_price_O = product_price.find('span').text
        image_link = list.find('img').get('src')
        if image_link == '//onlinestore.wsimg.com/assets/noimage/product-5fec99477aebb10bac85d82665ec1497de4536cda3279e59089555c45cf589fa.png':
        #info = [product,Combine_link,product_price_a]
            info = [{'product name': product,
                    'product link': Combine_link,
                    'product price': product_price_a
                    }]
            writer.writerows(info)
print("File create sucessfull")