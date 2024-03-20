import requests
from bs4 import BeautifulSoup

def istraukti_produktus(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    produktai = []
    for produktas in soup.find_all('li', class_='col col--xs-4 product js-product js-touch-hover'):
        pavadinimas = produktas.find('h3', class_='product__title').text.strip()
        kaina = produktas.find('p', class_='price').text.strip()
        kiekis = 1
        produktai.append({
            'pavadinimas': pavadinimas,
            'kaina': kaina,
            'kiekis': kiekis
        })
    return produktai
print(istraukti_produktus("https://www.rde.lt/categories/lt/277/sort/5/filter/0_0_0_0/page/1/Plauk%C5%B3-formavimo-%C5%A1ukos.html"))
