from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
import json

URL = 'https://www.pelando.com.br'
options = Options()
options.add_argument('--headless')
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH, options=options)
driver.get(URL)  # abre a url


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def reductor(link=''):
    link = link.replace(' ', '.')
    return link


def get_names():
    list_names = []
    names = driver.find_elements_by_class_name(reductor(link='flex--grow-1 text--b overflow--wrap-break size--all-s overflow--clamp-s-4 aGrid'))
    for name in names:
        name = cleanhtml(name.get_attribute('innerHTML'))
        str(name)
        a = name.split('  ', 2)
        product_name = [a[1]]
        if not 'GRÁTIS' or 'R$' in product_name:  # essa porra nao ta funcionando
            product_name[0] = [product_name[0] + '|R$0']
        list_names += product_name
        list_names = list_names[:5]
    return list_names


def get_links():
    list_link = []
    links = driver.find_elements_by_tag_name('a')
    for link in links:
        link = cleanhtml(link.get_attribute('href'))
        list_link += [link]
    list_link = list_link[27:32]
    return list_link


def _button(c):
    a = 0
    # c 1 day | c 2 month | c  3 year
    options = driver.find_elements_by_tag_name('option')
    for option in options:
        if a == c:
            break
        option.click()
        a += 1


def clear_json():
    with open('data.json', 'w') as f:
        f.write('')


def get_promos(c):
    counter = 0
    json_data = None
    product = {}
    _button(c)
    time.sleep(1)
    name_price_link = list((zip(get_names(), get_links())))
    clear_json()
    for column in name_price_link:
        product['name'] = column[0]
        product['link'] = column[1]
        json_data = json.dumps(product, indent=2, ensure_ascii=False)
        with open('data.json', 'a+', encoding='utf-8') as f:
            if counter == 0:
                f.write('[' + json_data + ',\n')
                counter += 1
                continue
            if counter == 4:
                f.write(json_data + ']')
                counter += 1
                continue
            else:
                f.write(json_data + ',\n')
                counter += 1
                continue
    return json_data
