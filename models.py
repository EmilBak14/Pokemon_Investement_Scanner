from dataclasses import dataclass

@dataclass
class CardListing:
    title: str
    price: float
    shipping: float
    seller: str
    seller_score: float
    condition: str
    url: str