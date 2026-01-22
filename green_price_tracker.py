import requests
import pandas as pd

# List of 'Green' or Sustainability-focused Crypto Assets (Example IDs)
green_tokens = ['cardano', 'algorand', 'solarcoin', 'power-ledger']

def fetch_green_prices():
    print("Fetching current market data for Green Wizard Project...")
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(green_tokens),
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Convert to a professional DataFrame for Economic Analysis
    df = pd.DataFrame(data).T
    df.columns = ['Price_USD', '24h_Change_%']
    return df

if __name__ == "__main__":
    market_data = fetch_green_prices()
    print("\n--- Current Sustainable Asset Overview ---")
    print(market_data)
