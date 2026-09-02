import re


BLOCKED_WORDS = [
    "proxy",
    "custom",
    "digital",
    "reprint",
    "replica",
    "damaged",
    "empty box",
    "lot",
    "slab skin",
    "skin",
    "bumper",
    "insert",
    "metal",
    "stainless steel",
    "gold foil",
    "blanket",
    "mystery",
    "grab",
    "fan art",
    "display",
    "fake",
    "replica",
    "orica",
    "frame",
    "extended art frame",
    "picture frame",
    "poster",
    "print",
    "art print", 
]


NON_ENGLISH_WORDS = [
    "spanish",
    "español",
    "japanese",
    "japan",
    "german",
    "deutsch",
    "french",
    "français",
    "italian",
    "korean",
    "chinese",
]


def is_blocked_title(title):
    title_lower = title.lower()

    return any(
        word in title_lower
        for word in BLOCKED_WORDS
    )


def is_english_listing(title):
    title_lower = title.lower()

    return not any(
        word in title_lower
        for word in NON_ENGLISH_WORDS
    )


def detect_grade(title, condition):
    title_upper = title.upper()

    patterns = {
        "PSA 10": r"\bPSA\s*10\b",
        "PSA 9": r"\bPSA\s*9\b",
        "PSA 8": r"\bPSA\s*8\b",
        "BGS 10": r"\bBGS\s*10\b",
        "BGS 9.5": r"\bBGS\s*9\.5\b",
        "CGC 10": r"\bCGC\s*10\b",
        "CGC 9.5": r"\bCGC\s*9\.5\b",
    }

    for grade, pattern in patterns.items():
        if re.search(pattern, title_upper):
            return grade

    if condition.lower() == "graded":
        return "GRADED_UNKNOWN"

    return "RAW"


def has_required_terms(title, required_terms):
    title_lower = title.lower()

    return all(
        term.lower() in title_lower
        for term in required_terms
    )