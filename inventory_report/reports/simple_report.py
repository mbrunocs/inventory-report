from collections import Counter


class SimpleReport:
    def generate(lst):
        oldest_maked_date = min([prod['data_de_fabricacao'] for prod in lst])
        latest_maked_date = min([prod['data_de_validade'] for prod in lst])
        most_prod_manu = (
            Counter([prod['nome_da_empresa'] for prod in lst]).most_common())

        return (
            f"Data de fabricação mais antiga: {oldest_maked_date}\n"
            f"Data de validade mais próxima: {latest_maked_date}\n"
            f"Empresa com mais produtos: {str(most_prod_manu[0][0])}"
        )

# referencias:
# https://pt.stackoverflow.com/questions/456224/obter-o-elemento-
# mais-frequente-e-menos-frequente-de-uma-lista-al%C3%A9m-do-maior
# -e#:~:text=most_common%20retorna%20uma%20lista%20de,menos%20
# frequente%20%C3%A9%20o%20%C3%BAltimo.
