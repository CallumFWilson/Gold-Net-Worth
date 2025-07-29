# Gold Value Calculator

This project helps you retrieve the current value of your gold using the [GoldAPI.io](https://www.goldapi.io/) service.

## 📁 Structure
```text
gold-value-calculator/
├── scripts/
│   └── calculate_value.py          # Contains core logic functions
├── config/
│   ├── config.json                 # Actual config 
│   └── config.example.json         # Sample config
├── data/
│   ├── gold_items.json             # Actual gold data
│   └── gold_items.example.json     # Sample gold data
├── .gitignore
└── README.md
```

## ✨ Features

- 🔐 Loads your private API key and URL from a local config file

- 📈 Fetches the current gold price (XAU/USD) and converts it from troy ounces to grams

- 🧮 Calculates the pure gold value of each item based on its karat

- 🧾 Prints a clean, aligned breakdown of item values and total net worth

## ⚙️ Setup

### 1. Clone the repository
   ```bash
   git clone https://github.com/CallumFWilson/Gold-Net-Worth.git
   cd Gold-Net-Worth 
   ```
### 2. Set Up Your Config
Create your local config file by copying the example:
  ```bash
  cp config/config.example.json config/config.json
  ```
Then edit `config/config.json` and add your GoldAPI key:
  ```json
  {
  "api_url": "https://www.goldapi.io/api/XAU/USD",
  "api_key": "your-api-key-here"
  }
  ```
### 3. Set Up Your Gold Items
Create your local gold items file by copying the example:
  ```bash
  cp data/gold_items.example.json data/gold_items.json
  ```
Then edit `data/gold_items.json` and add your items:
  ```json
  [
     {
       "name": "Gold Necklace",
       "weight_grams": 50,
       "karat": 22
     },
     {
       "name": "Gold Ring",
       "weight_grams": 10,
       "karat": 24
     }
  ]
  ```
Each item should include:

`name`: A label for the item

`weight_grams`: Total weight in grams

`karat`: Gold purity (e.g. 24 for pure gold, 18 for 75%)

## 🧪 Running the Script

After setup, run the script to calculate the value of your gold:
  ```bash
  python scripts/calculate_value.py
  ```
or,
```python
from scripts.calculate_value import (
    load_config,
    load_gold_items,
    fetch_gold_price,
    calculate_total_value
)

config = load_config()
items = load_gold_items()
gold_price = fetch_gold_price(config["api_url"], config["api_key"])

calculate_total_value(items, gold_price)
```
This will:

- Fetch the current gold price per gram (converted from troy ounces)

- Calculate the pure gold content for each item

- Print an itemised and aligned breakdown with total net worth

## 🧾 Example Output

```ruby
Gold Price: $62.80 per gram

`Wedding Ring`        $ 1507.20   ( 24.00g pure gold)
`Pendant`             $ 1040.70   ( 18.00g pure gold)
`Cufflinks`           $  837.60   ( 13.33g pure gold)
`Bangle`              $ 1674.90   ( 26.66g pure gold)

Total Net Value: $5060.40
```