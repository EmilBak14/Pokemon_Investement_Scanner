from ebay import search_ebay
from price_analyzer import analyze_prices
from deal_engine import deal_score, seller_trust, price_risk
from market_price import get_market_price
from utils.cache import load_cache, save_cache
from datetime import datetime

QUERY = "Umbreon VMAX 215/203 English"


def main():
    cache = load_cache()

    print(cache)

    print(f"\n🔎 Scanner eBay efter: {QUERY}\n")

    listings = search_ebay(
        QUERY,
        limit=50
    )

    if not listings:
        print("❌ Ingen relevante listings fundet.")
        return

    stats = analyze_prices(listings)
    market_price = get_market_price("Umbreon VMAX 215/203")

    if stats is None:
        print("❌ Kunne ikke analysere priserne.")
        return

    card_name = "Umbreon VMAX 215/203"

    scan_data = {
        "scanned_at": datetime.now().isoformat(timespec="seconds"),
        "reference_market_price": market_price,
        "lowest": stats["lowest"],
        "average": stats["average"],
        "median": stats["median"],
        "highest": stats["highest"],
        "listings": stats["count"],
    }

    if card_name not in cache:
        cache[card_name] = []

    cache[card_name].append(scan_data)

    save_cache(cache)

    print("=" * 60)
    print("MARKET ANALYSIS")
    print("=" * 60)

    print(f"Reference market price: {market_price:.2f} USD")
    print(f'Listings: {stats["count"]}')
    print(f'Lowest:   {stats["lowest"]:.2f}')
    print(f'Average:  {stats["average"]:.2f}')
    print(f'Median:   {stats["median"]:.2f}')
    print(f'Highest:  {stats["highest"]:.2f}')

    print("\n" + "=" * 60)
    print("DEALS")
    print("=" * 60)

    listings_sorted = sorted(
        listings,
        key=lambda listing: listing["price"] + listing["shipping"]
    )

    for listing in listings_sorted:
        total_price = (
            listing["price"]
            + listing["shipping"]
        )

        deal = deal_score(
            total_price,
            market_price
        )

        risk = price_risk(
            total_price,
            market_price
        )

        trust = seller_trust(
            listing["seller_feedback"]
        )

        print("\n" + "-" * 60)
        print(listing["title"])

        print(
            f'Price: {listing["price"]:.2f} '
            f'{listing["currency"]}'
        )

        print(
            f'Shipping: {listing["shipping"]:.2f} '
            f'{listing["currency"]}'
        )

        print(
            f'Total: {total_price:.2f} '
            f'{listing["currency"]}'
        )

        print(f'Condition: {listing["condition"]}')

        print(
            f'Seller: {listing["seller_username"]} '
            f'({listing["seller_feedback"]}%)'
        )

        print(f"Seller Trust: {trust}")

        print(
            f'Reference market price: '
            f'{market_price:.2f} '
            f'{listing["currency"]}'
        )

        print(
            f'Discount: '
            f'{deal["discount"]:.1f}%'
        )

        print(deal["rating"])
        print(f"Price Risk: {risk}")
        print(listing["url"])


if __name__ == "__main__":
    main()