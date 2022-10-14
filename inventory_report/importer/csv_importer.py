import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path: str):
        try:
            if path.endswith('.csv'):
                with open(path) as file:
                    content = list(csv.DictReader(file))
                    return content
            else:
                raise ValueError('Arquivo inválido')
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path}")
