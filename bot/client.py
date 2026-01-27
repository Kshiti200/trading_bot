import os
from dotenv import load_dotenv
from binance.client import Client

# Load API keys from .env file
load_dotenv()


class BinanceFuturesClient:
    """
    A small wrapper around the Binance Futures Testnet client.

    This keeps API setup separate from order logic,
    making the project easier to maintain.
    """

    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        secret_key = os.getenv("BINANCE_SECRET_KEY")

        if not api_key or not secret_key:
            raise ValueError(
                "API credentials not found. Please check your .env file."
            )

        # Create Binance client instance
        self.client = Client(api_key, secret_key)

        # Point client to Futures Testnet instead of real Binance
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        print("✅ Connected to Binance Futures Testnet!")
