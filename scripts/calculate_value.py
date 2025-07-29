from pathlib import Path
import json
import requests

def load_config():
    config_path = Path(__file__).parent.parent / "config" / "config.json"
    with open(config_path) as f:
        return json.load(f)

def load_gold_items():
    with open(Path(__file__).parent.parent / "data" / "gold_items.json") as f:
        return json.load(f)

def fetch_gold_price(api_url, api_key):
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()
    return data["price"] 
