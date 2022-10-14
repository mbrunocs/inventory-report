import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path: str):
        try:
            if path.endswith('.xml'):
                file = ET.parse(path).getroot()
                return [{
                  data.tag: data.text for data in elem} for elem in file]
            else:
                raise ValueError('Arquivo inválido')
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path}")
