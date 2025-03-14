from dotenv import load_dotenv
import os

load_dotenv()

# API Configuration
YAHOO_FINANCE_API = "FREE"  # No API key needed
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
FMP_API_KEY = os.getenv("FMP_API_KEY")

# Technical Analysis Settings
TIMEFRAMES = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "max"]
DEFAULT_SYMBOL = "AAPL"

# Indicator Settings
RSI_PERIOD = 14
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
