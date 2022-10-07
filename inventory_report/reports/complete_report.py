from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(lst):
        compilado = ''
        all_manu = (
            Counter([prod['nome_da_empresa'] for prod in lst]))
        for row in all_manu:
            compilado += f'- {row[0]}: {row[1]}\n'

        return (
            f"{SimpleReport.generate(lst)}\n"
            f"Produtos estocados por empresa:\n"
            f"{compilado}"
        )
