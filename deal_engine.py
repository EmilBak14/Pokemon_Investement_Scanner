def deal_score(listing_price, market_price):

    difference = market_price - listing_price

    discount = difference / market_price

    if discount >= 0.80:
        rating = "⚠️ SUSPICIOUSLY CHEAP"

    elif discount >= 0.30:
        rating = "🔥 MEGA DEAL"

    elif discount >= 0.20:
        rating = "✅ GOD DEAL"

    elif discount >= 0.10:
        rating = "⚠️ MULIG DEAL"

    else:
        rating = "❌ PASS"

    return {
        "difference": difference,
        "discount": round(discount*100,1),
        "rating": rating
    }

if __name__ == "__main__":
    test = deal_score(1800, 2500)
    print(test)

def seller_trust(feedback):

    if feedback >= 99.5:
        return "⭐ TRUSTED SELLER"

    elif feedback >= 97:
        return "✅ GOOD SELLER"

    elif feedback >= 90:
        return "⚠️ USE CAUTION"

    else:
        return "❌ HIGH RISK SELLER"

def price_risk(listing_price, market_price):
    ratio = listing_price / market_price

    if ratio < 0.10:
        return "🚨 EXTREME PRICE ANOMALY"

    elif ratio < 0.25:
        return "⚠️ VERY SUSPICIOUS"

    elif ratio < 0.50:
        return "🟡 CHECK CAREFULLY"

    else:
        return "✅ PRICE LOOKS PLAUSIBLE"