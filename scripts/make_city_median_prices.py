#!/usr/bin/env python3
"""Create the city median sale price summary used by index.html."""

import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "college_town_home_sales.csv"
OUTPUT = ROOT / "data" / "city_median_sale_prices.json"
MINIMUM_SALE_PRICE = 10_000


def median(values):
    values = sorted(values)
    middle = len(values) // 2
    if len(values) % 2:
        return values[middle]
    return (values[middle - 1] + values[middle]) / 2


def main():
    prices_by_city = defaultdict(list)
    with INPUT.open(newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            sale_price = int(row["sale_price"])
            if sale_price >= MINIMUM_SALE_PRICE:
                prices_by_city[(row["city"], row["state"])].append(sale_price)

    summary = [
        {
            "city": city,
            "state": state,
            "qualifying_sales": len(prices),
            "median_sale_price": median(prices),
        }
        for (city, state), prices in sorted(prices_by_city.items())
    ]
    OUTPUT.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
