from inventory_report.inventory.product import Product
# from functools import


def test_cria_produto():
    cadeira = Product(
        10,
        'Cadeira gamer',
        'GamerCompany',
        '2020',
        '2022',
        845120956230,
        'Longe de umidade')

    assert cadeira.__repr__().__contains__('GamerCompany')
