from utils.parser import (
    is_blocked_title,
    is_english_listing,
    detect_grade,
    has_required_terms,
)
import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("EBAY_CLIENT_ID")
CLIENT_SECRET = os.getenv("EBAY_CLIENT_SECRET")


def get_access_token():
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    encoded = base64.b64encode(credentials.encode()).decode()

    response = requests.post(
        "https://api.ebay.com/identity/v1/oauth2/token",
        headers={
            "Authorization": f"Basic {encoded}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        },
    )

    response.raise_for_status()
    return response.json()["access_token"]

def search_ebay(query, limit=20):
    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
    }

    params = {
        "q": query,
        "limit": limit,
        "filter": "buyingOptions:{FIXED_PRICE}",
    }

    response = requests.get(
        "https://api.ebay.com/buy/browse/v1/item_summary/search",
        headers=headers,
        params=params,
    )

    response.raise_for_status()
    data = response.json()

    listings = []

    required_terms = [
        "umbreon",
        "vmax",
        "215/203",
    ]

    for item in data.get("itemSummaries", []):
        title = item.get("title", "")
        condition = item.get("condition", "Unknown")

        if not has_required_terms(title, required_terms):
            continue

        if is_blocked_title(title):
            continue

        if not is_english_listing(title):
            continue

        price_data = item.get("price", {})
        shipping_data = item.get("shippingOptions", [])

        shipping_cost = 0.0

        if shipping_data:
            shipping_cost_data = shipping_data[0].get("shippingCost", {})
            shipping_cost = float(
                shipping_cost_data.get("value", 0)
            )

        seller = item.get("seller", {})

        listing = {
            "title": title,
            "price": float(
                price_data.get("value", 0)
            ),
            "currency": price_data.get(
                "currency",
                ""
            ),
            "shipping": shipping_cost,
            "condition": condition,
            "grade": detect_grade(
                title,
                condition
            ),
            "seller_username": seller.get(
                "username",
                "Unknown"
            ),
            "seller_feedback": float(
                seller.get(
                    "feedbackPercentage",
                    0
                )
            ),
            "url": item.get(
                "itemWebUrl",
                ""
            ),
        }

        listings.append(listing)

    return listings


if __name__ == "__main__":
    results = search_ebay(
        "Umbreon VMAX 215/203 English",
        limit=20
    )

    print(f"\n✅ {len(results)} relevante listings fundet\n")

    for listing in results:
        print("-" * 60)
        print(f'Title: {listing["title"]}')
        print(
            f'Price: {listing["price"]} '
            f'{listing["currency"]}'
        )
        print(
            f'Shipping: {listing["shipping"]} '
            f'{listing["currency"]}'
        )
        print(f'Condition: {listing["condition"]}')
        print(
            f'Seller: {listing["seller_username"]} '
            f'({listing["seller_feedback"]}%)'
        )
        print(f'URL: {listing["url"]}')