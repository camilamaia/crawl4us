import requests
import logging
import time

from bs4 import BeautifulSoup
import pandas as pd


log = logging.getLogger(__name__)


def _load_page(url):
    request = requests.get('http://' + url)
    page = BeautifulSoup(request.text, 'html.parser')

    return page


def _find_table(page, index, whole_page):
    if whole_page:
        return page

    return page.find_all('table')[index]


def _crawl_table(html_table):
    table = []

    for tr in html_table.find_all('tr'):
        row = []
        for th in tr.find_all('th'):
            row.append(th.text.strip())

        for td in tr.find_all('td'):
            row.append(td.text.strip())

        table.append(row)

    return table


def _map_columns_names(col, official_header):
    for h in official_header:
        if col in official_header[h]:
            return h
    return '--'


def _parse_header(table, official_header):
    header = table[0]
    header = [_map_columns_names(h.lower(), official_header) for h in header]
    table[0] = header

    return table


def crawl(url, official_header, index=0, whole_page=False):
    started_at = time.time()
    log.warning('### Loading table from %s ###' % url)

    page = _load_page(url)
    html_table = _find_table(page, index, whole_page)
    table = _crawl_table(html_table)
    table = _parse_header(table, official_header)

    log.warning('### Finished in %.2f seconds ###' % (time.time() - started_at))
    log.warning('### Total of rows %s ###' % len(table))

    return pd.DataFrame(table[1:], columns=table[0])
