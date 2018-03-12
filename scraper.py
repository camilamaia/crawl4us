import requests
from bs4 import BeautifulSoup

headers = {
    'ADM': ['administradora', 'admin', 'adm', 'admin.'],
    'CRE': ['crédito', 'credito'],
    'ENT': ['entrada'],
    'SAL': ['saldo'],
    'COM': ['complemento'],
    'OBS': ['observações', 'observacoes', 'observaçoes', 'observacões', 'obs'],
    'SIT': ['situação', 'situacao', 'situaçao', 'situacão']
}

def load_page():
    url = ''
    request = requests.get('http://' + url)
    page = BeautifulSoup(request.text, 'html.parser')

    return page


def wtih_header(table):
    header = table.pop(0)
    header = [h.lower() for h in header]
    return (table, header)


def clean_table(table):
    table.pop(0)

    return table


def scrap_table(page):
    table = []

    for tr in page.find_all('tr'):
        row = []
        for td in tr.find_all('td'):
            row.append(td.text.strip())

        table.append(row)

    return clean_table(table)


def map_columns_names(col):
    if col in headers['ADM']:
        return 'adm'
    elif col in headers['CRE']:
        return 'crédito'
    elif col in headers['ENT']:
        return 'entrada'
    elif col in headers['SAL']:
        return 'saldo'
    elif col in headers['COM']:
        return 'complemento'
    elif col in headers['OBS']:
        return 'observações'
    elif col in headers['SIT']:
        return 'situação'
    else:
        return '--'


def main():
    page = load_page()
    table = scrap_table(page)
    table, header = wtih_header(table)
    header = list(map(map_columns_names, header))


if __name__ == "__main__":
    main()
