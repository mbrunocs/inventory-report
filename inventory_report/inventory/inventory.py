import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

# mode_types= ['simples', 'completo']
# referencias:
#   https://pt.stackoverflow.com/questions/429465/como-verificar-se-
#   parte-de-uma-string-esta-contida-em-uma-lista-python
#   https://stackoverflow.com/questions/1747817/create-a-dictionary-with-comprehension


class Inventory:
    def import_data(path: str, report_mode):
        content = []
        if path.endswith('.csv'):
            with open(path) as file:
                content = list(csv.DictReader(file))
        if path.endswith('.json'):
            with open(path) as file:
                content = json.load(file)
        if path.endswith('.xml'):
            file = ET.parse(path).getroot()
            content = [{data.tag: data.text for data in elem} for elem in file]

        if report_mode == 'completo':
            return CompleteReport.generate(content)
        return SimpleReport.generate(content)
