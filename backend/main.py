from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Checkout:
    def __init__(self):
        self.individual_pricing = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        self.special_pricing = {'A': (3, 130), 'B': (2, 45)}

    def calculate_total(self, items):
        total_price = 0
        item_counts = {}
        for item in items:
            item_counts[item] = item_counts.get(item, 0) + 1
        for item, count in item_counts.items():
            if item in self.special_pricing:
                bundle_count, bundle_price = self.special_pricing[item]
                num_of_bundles = count // bundle_count
                remainder = count % bundle_count
                total_price += (num_of_bundles * bundle_price) + (remainder * self.individual_pricing[item])
            else:
                total_price += count * self.individual_pricing.get(item, 0)
        return total_price


class Items(BaseModel):
    items: Optional[str] = ""


@app.post("/checkout/")
def checkout(item_list: Items):
    checkout_system = Checkout()
    total = checkout_system.calculate_total(item_list.items)
    return {"total": total}
