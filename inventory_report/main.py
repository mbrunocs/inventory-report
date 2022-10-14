import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    _, path, type = sys.argv

    try:
        if '.csv' in path:
            importer = InventoryRefactor(CsvImporter)
        elif '.json' in path:
            importer = InventoryRefactor(JsonImporter)
        else:
            importer = InventoryRefactor(XmlImporter)
        return sys.stdout.write(importer.import_data(path, type))
    except ValueError:
        sys.stderr.write('Verifique os argumentos\n')
