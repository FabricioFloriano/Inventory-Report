from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory
from datetime import datetime
from collections import Counter


class SimpleReport(Report):
    def __init__(self):
        self.inventories = []

    def add_inventory(self, inventory: Inventory):
        self.inventories.append(inventory)

    def generate(self) -> str:
        all_products = []
        for inventory in self.inventories:
            all_products.extend(inventory.data)

        if not all_products:
            return "No products in inventory."

        manufacturing_dates = [
            datetime.strptime(product.manufacturing_date, "%Y-%m-%d")
            for product in all_products
        ]
        oldest_manufacturing_date = min(manufacturing_dates).strftime(
            "%Y-%m-%d"
        )
        valid_products = [
            product
            for product in all_products
            if datetime.strptime(product.expiration_date, "%Y-%m-%d")
            > datetime.now()
        ]
        closest_expiration_date = min(
            valid_products,
            key=lambda x: datetime.strptime(x.expiration_date, "%Y-%m-%d"),
        ).expiration_date

        company_counter = Counter(
            product.company_name for product in all_products
        )
        company_with_largest_inventory = company_counter.most_common(1)[0][0]

        report = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: "
            f"{company_with_largest_inventory}"
        )
        return report
