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
final_response["description"] = soup.select_one('.proddet').get_text(strip=True)

# skus
final_response["skus"] = []

for card in soup.select(".card"):

    final_response["skus"].append({
        "name": card.select_one(".prod-nome").get_text(strip=True),
        "current_price": float(card.select_one(".prod-pnow").get_text(strip=True).replace("R$", "").replace(",", ".")) if card.select_one(".prod-pnow") else None,
        "old_price": float(card.select_one(".prod-pold").get_text(strip=True).replace("R$", "").replace(",", ".")) if card.select_one(".prod-pold") else None,
        "available": "not-avaliable" not in card.get("class", [])
    })

# properties
final_response["properties"] = []

for row in soup.select(".pure-table tr"):

    tds = row.select("td")
    if len(tds) == 2:
        label = tds[0].get_text(strip=True)
        value = tds[1].get_text(strip=True)
        final_response["properties"].append({
            "label": label,
            "value": value
        })

# reviews
final_response["reviews"] = []

for review in soup.select(".analisebox"):
    final_response["reviews"].append({
        "name": review.select_one(".analiseusername").get_text(strip=True),
        "date": review.select_one(".analisedate").get_text(strip=True),
        "score": review.select_one(".analisestars").get_text(strip=True).count("★"),
        "text": review.select("p")[-1].get_text(strip=True)
    })



# reviews_average_score
score = soup.select_one('#comments h4')
final_response["reviews_average_score"] = float(score.get_text().split(":")[1].split("/")[0].strip())

# url
final_response["url"] = url 

# export
with open ('produto.json', 'w',encoding='utf-8') as f:
    json.dump(final_response, f, indent=2, ensure_ascii=False)

print("✅ Sucesso.")