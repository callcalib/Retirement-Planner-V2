import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def load_json(filename):

    path = BASE_DIR / "data" / filename

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)



def load_database():

    return {

        "countries":
            load_json("countries.json"),

        "tax":
            load_json("tax_rules.json"),

        "exchange":
            load_json("exchange_rates.json"),

        "houses":
            load_json("house_prices.json"),

        "visas":
            load_json("visas.json"),

        "prices":
            load_json("product_prices.json")

    }
