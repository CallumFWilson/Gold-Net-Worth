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

    # Convert troy ounce to gram
    price_per_ounce = data["price"]
    price_per_gram = price_per_ounce / 31.1035
    return price_per_gram 

def calculate_purity_value(weight, karat):
    return weight * (karat / 24.0)

def calculate_total_value(jewellery, gold_price):
    total = 0
    for item in jewellery:
        pure_weight = calculate_purity_value(item["weight_grams"], item["karat"])
        value = pure_weight * gold_price
        total += value
        print(f"{item['description']:<15}  ${value:>8.2f}   ({pure_weight:>6.2f}g pure gold)")
    print(f"\nTotal Net Value: ${total:.2f}")

def main():
    config = load_config()
    items = load_gold_items()
    gold_price = fetch_gold_price(config["api_url"], config["api_key"])

    print(f"Gold Price: ${gold_price:.2f} per gram\n")
    calculate_total_value(items, gold_price)

if __name__ == "__main__":
    main()
    