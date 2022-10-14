import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path: str):
        try:
            if path.endswith('.json'):
                with open(path) as file:
                    return json.load(file)
            else:
                raise ValueError('Arquivo inválido')
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path}")
