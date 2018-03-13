import requests
from bs4 import BeautifulSoup


def _load_page(url):
    request = requests.get('http://' + url)
    page = BeautifulSoup(request.text, 'html.parser')

    return page


def _wtih_header(table):
    header = table[0]
    header = [h.lower() for h in header]
    return (table, header)


def _clean_table(table):
    table.pop(0)

    return table


def _scrap_table(page):
    table = []

    for tr in page.find_all('tr'):
        row = []
        for td in tr.find_all('td'):
            row.append(td.text.strip())

        table.append(row)

    return _clean_table(table)


def _map_columns_names(col, official_header):
    for h in official_header:
        if col in official_header[h]:
            return h
    return '--'


def crawl(url, official_header):
    page = _load_page(url)
    table = _scrap_table(page)
    table, header = _wtih_header(table)
    header = [_map_columns_names(h, official_header) for h in header]
    table[0] = header

    return table
