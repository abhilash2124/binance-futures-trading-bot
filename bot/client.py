from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        api_key=os.getenv("API_KEY"),
        api_secret=os.getenv("API_SECRET"),
        # testnet=True
    )

    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client


if __name__ == "__main__":
    client = get_client()
    
    try:
        balance = client.futures_account_balance()
        print("✅ Connected successfully!")
        print(balance[:2])  # show first 2 entries
    except Exception as e:
        print("❌ Error:", e)