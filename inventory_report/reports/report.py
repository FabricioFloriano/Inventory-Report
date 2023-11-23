from abc import abstractmethod
from typing import Protocol
from inventory_report.inventory import Inventory


class Report(Protocol):
    @abstractmethod
    def add_inventory(self, inventory: Inventory) -> None:
        pass

    @abstractmethod
    def generate(self) -> str:
        pass
