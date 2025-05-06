import requests
import json
from bs4 import BeautifulSoup

# request
url = 'https://infosimples.com/vagas/desafio/commercia/product.html'
response = requests.get(url)

# parsing with BeautfulSoup
soup = BeautifulSoup(response.text, 'html.parser')

final_response = {}

final_response["title"] = soup.select_one('h2#product_title').get_text()

final_response["brand"] = soup.select_one('.brand').get_text()

# export
with open ('produto.json', 'w',encoding='utf-8') as f:
    json.dump(final_response, f, indent=2)

print("✅ Sucesso.")