from statistics import mean, median


def analyze_prices(listings):
    prices = []

    for listing in listings:
        total_price = listing["price"] + listing["shipping"]
        prices.append(total_price)

    prices.sort()

    if not prices:
        return None

    return {
        "lowest": round(min(prices), 2),
        "highest": round(max(prices), 2),
        "average": round(mean(prices), 2),
        "median": round(median(prices), 2),
        "count": len(prices),
    }