from django.shortcuts import render,HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import Product
# from assignment import models

def scrape_product(request):
    product_details = []
    url=[]

    # loop through product URLs and extract product details
    # for url in product_urls:
        # send GET request and parse HTML with BeautifulSoup

    headers = {'User-Agent': 'Mozilla/5.0'}
    url='https://www.amazon.in//ADISA-BP005-Weight-Casual-Backpack/dp/B07F3X45WZ'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify)
    results=soup.find_all('div',{'class':'a-section feature detail-bullets-wrapper bucket'})
    print(results,"results")
    # asin = soup.find('span', {'class': 'a-text-bold'}).text
    
    description = soup.find('div')
    print(description)
    # asin = soup.find('span', {'class': 'a-icon-alt'})#.find_next_sibling('td').get_text().strip()
    # product_description=soup.find('div', {'id': 'product_Description'}).get_text().strip()
    # manufacturer = soup.find('th', text='Manufacturer').find_next_sibling('td').get_text().strip()
    # print(description,asin,product_description,manufacturer)
    # print("ASIN", asin)
    
    return HttpResponse("updated")    

def scrape_products(request):
    base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'
    for page in range(1, 21):       
        url = base_url.format(page)        
        response = requests.get(url)        
        soup = BeautifulSoup(response.content, 'html.parser')        
        products = soup.find_all('div', {'data-component-type': 's-search-result'})        
        for product in products:
            url = 'https://www.amazon.in/'+product.find('a', {'class': 'a-link-normal s-no-outline'})['href']            
            name = product.find('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).text.strip()            
            price = float(product.find('span', {'class': 'a-price-whole'}).text.replace(',', ''))           
            rating = float(product.find('span', {'class': 'a-icon-alt'}).text.split()[0])
            reviews = float(product.find('span', {'class': 'a-size-base'}).text.replace(',', '').split()[0])
            
            Product.objects.create(url=url, name=name, price=price, rating=rating, reviews=reviews)
        
    return HttpResponse("added")
