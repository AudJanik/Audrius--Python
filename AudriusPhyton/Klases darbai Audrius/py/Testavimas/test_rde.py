import os
import pytest
from rde_sukos_db import create_db, prideti_produkta, gauti_produktus
from rde_sukos import istraukti_produktus
import requests_mock
@pytest.fixture(scope="module")

def db_setup():
    create_db()
    yield
    os.remove('produktai.db')


class TestProduktai:
    def test_prideti_ir_gauti_produktus(self, db_setup):
        testiniai_produktai = [{'pavadinimas' : 'produktas1', 'kaina': '10,99', 'kiekis' : 5}]

        prideti_produkta(testiniai_produktai)
        produktai_db = gauti_produktus()
        assert any (p[1] == 'produktas1' for p in produktai_db)
        # assert (2, 'produktas2', '11,99', 3) in produktai_db

mock_html = '''
<!DOCTYPE html>
<html lang="en">
<body>
<li class ='col col--xs-4 product js-product js-touch-hover' >
<h3 class='product__title'>produktas1</h3>
<p class = 'price'>10,99</p>
</li>
<li class ='col col--xs-4 product js-product js-touch-hover' >
<h3 class='product__title'>produktas2</h3>
<p class = 'price'>3,33</p>
</li>
</body>
</html>'''

def test_istraukti_produktus():
    test_url = 'https://www.labadiena.lt/produktai/produktai.html'
    expected_response = [{'pavadinimas' : 'produktas1', 'kaina': '10,99', 'kiekis': 1},
                         {'pavadinimas' : 'produktas2', 'kaina': '3,33', 'kiekis': 1}]
    with requests_mock.Mocker() as m:
        m.get(test_url, text=mock_html)
        result = istraukti_produktus(test_url)
    assert result == expected_response