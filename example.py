"""Minimal eBay item details API call — one typed row per product.

Docs & schema: https://quanticdata.io/collectors/ebay-product-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/ebay_product/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "items": [
            "158070397228"
        ],
        "max_results": 1
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("url"), row.get("title"), row.get("subtitle"))
print(f"{len(data['results'])} products, cost ${data['cost']}")
