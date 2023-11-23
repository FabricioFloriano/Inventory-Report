from inventory_report.product import Product
import abc
import json
import csv

from typing import Dict, Type


class Importer(abc.ABC):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path
        self._import_data: list[Product] = []

    @abc.abstractmethod
    def import_data(self) -> list[Product]:
        return self._import_data


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            self.data = [Product(**product) for product in json.load(file)]

        return self.data


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, encoding="utf-8") as file:
            reader_csv = csv.reader(file, delimiter=",", quotechar='"')
            _, *data = reader_csv
            self.data = [
                Product(
                    id=product[0],
                    product_name=product[1],
                    company_name=product[2],
                    manufacturing_date=product[3],
                    expiration_date=product[4],
                    serial_number=product[5],
                    storage_instructions=product[6],
                )
                for product in data
            ]

        return self.data


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
