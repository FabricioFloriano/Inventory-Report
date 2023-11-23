from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        report = super().generate()

        get_products = []
        for inventory in self.inventories:
            get_products.extend(inventory.data)

        get_by_company = {}
        for product in get_products:
            get_by_company[product.company_name] = (
                get_by_company.get(product.company_name, 0) + 1
            )

        stocked_products_by_company = "\nStocked products by company:\n"
        for company, stocked in get_by_company.items():
            stocked_products_by_company += f"- {company}: {stocked}\n"

        return f"{report}{stocked_products_by_company}"
