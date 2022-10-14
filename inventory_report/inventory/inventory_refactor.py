from abc import abstractmethod

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    @abstractmethod
    def import_data(self, path: str, report_mode: str):
        new_data = self.importer.import_data(path)
        [self.data.append(data) for data in new_data]
        if report_mode == 'completo':
            return CompleteReport.generate(self.data)
        return SimpleReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
