import streamlit as st
import pandas as pd
from scripts.calculate_value import get_total_gold_value, load_gold_items, calculate_purity_value
from scripts.download_data import download_gold_history

download_gold_history()

# Load data
@st.cache_data
def load_data(path="data/gold_price_history.csv"):
    df = pd.read_csv(path, index_col=0, parse_dates=True, skiprows=[1])
    return df

df = load_data()

items = load_gold_items()
total_pure_grams = sum(
    calculate_purity_value(item["weight_grams"], item["karat"]) for item in items
)

df["Gold Price (per gram)"] = df["Gold Price"] / 31.1035
df["My Gold Value"] = df["Gold Price (per gram)"] * total_pure_grams

# Show current gold price (last available)
current_price = round(df["Gold Price"].iloc[-1], 2)
current_value = round(get_total_gold_value(), 2)

# Layout
st.title("Gold Price Dashboard")

# Display current price top-left
st.markdown(f"### Current Gold Price: ${current_price}")

# Display current price top-left
st.markdown(f"### Current Gold Value: ${current_value}")

# Line chart of Gold Price over time
st.line_chart(df["Gold Price"])
st.line_chart(df["My Gold Value"])