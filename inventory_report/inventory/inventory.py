from abc import abstractmethod

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

# mode_types= ['simples', 'completo']
# referencias:
#   https://pt.stackoverflow.com/questions/429465/como-verificar-se-
#   parte-de-uma-string-esta-contida-em-uma-lista-python
#   https://stackoverflow.com/questions/1747817/create-a-dictionary-with-comprehension


class Inventory:
    @abstractmethod
    def import_data(path: str, report_mode: str):
        content = []
        if path.endswith('.csv'):
            content = CsvImporter(path)
        if path.endswith('.json'):
            content = JsonImporter(path)
        if path.endswith('.xml'):
            content = XmlImporter(path)

        if report_mode == 'completo':
            return CompleteReport.generate(content)
        return SimpleReport.generate(content)
