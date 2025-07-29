# Gold Net Worth

This project helps you retrieve the current gold price using the [GoldAPI.io](https://www.goldapi.io/) service.

## Features

- 🔐 Loads your private API key and URL from a local config file
- 📈 Fetches the current gold price (XAU/USD)

## Setup

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
Then edit config/config.json and add your GoldAPI key:
  ```json
  {
  "api_url": "https://www.goldapi.io/api/XAU/USD",
  "api_key": "your-api-key-here"
  }
  ```