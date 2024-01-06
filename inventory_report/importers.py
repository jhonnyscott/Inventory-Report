from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str):
        super().__init__(path)

    def import_data(self) -> list[Product]:
        product_list = []
        with open(self.path, "r") as file:
            product_data = json.load(file)
            for product in product_data:
                product_list.append(Product(**product))
            return product_list


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
