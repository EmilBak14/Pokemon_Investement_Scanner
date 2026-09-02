from dotenv import load_dotenv
import os

load_dotenv()

EBAY_CLIENT_ID = os.getenv("EBAY_CLIENT_ID")
EBAY_CLIENT_SECRET = os.getenv("EBAY_CLIENT_SECRET")

MIN_DISCOUNT = 20      # %
MIN_SELLER_SCORE = 99.5