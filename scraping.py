import json

final_response = {
    "title": "",
    "brand": "",
    "categorie": [],
    "description": "",
    "skus": [],
    "properties": [],
    "reviews": [],
    "reviews_average_score": 0.0,
    "url":  "https://infosimples.com/vagas/desafio/commercia/product.html"

}

with open ('produto.json', 'w',encoding='utf-8') as f:
    json.dump(final_response, f, indent=2)