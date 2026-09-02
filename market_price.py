def get_market_price(card_name):
    """
    Midlertidig funktion.

    Senere skal den hente rigtig markedspris
    fra PriceCharting / Cardmarket / andre kilder.
    """

    test_prices = {
        "Umbreon VMAX 215/203": 2000,
        "Charizard ex 199/165": 1000,
        "Pikachu ex 238/191": 900,
    }

    return test_prices.get(card_name)