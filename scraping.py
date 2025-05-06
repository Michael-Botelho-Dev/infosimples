import requests
import json
from bs4 import BeautifulSoup

# request
url = 'https://infosimples.com/vagas/desafio/commercia/product.html'
response = requests.get(url)

# parsing with BeautfulSoup
soup = BeautifulSoup(response.text, 'html.parser')

final_response = {}

# title
final_response["title"] = soup.select_one('h2#product_title').get_text()

# brand
final_response["brand"] = soup.select_one('.brand').get_text()

# categories
categories = soup.select("nav.current-category a")
final_response["categories"] = [cat.get_text() for cat in categories]

# description 
final_response["description"] = soup.select_one('.proddet p').get_text()


# url
final_response["url"] = url 

# export
with open ('produto.json', 'w',encoding='utf-8') as f:
    json.dump(final_response, f, indent=2)

print("✅ Sucesso.")


