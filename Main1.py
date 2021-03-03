from urllib.request import urlopen
from bs4 import BeautifulSoup
a = '96231488' # Zmienić w przypadku gotowej strony
html = urlopen('https://www.ceneo.pl/'+a+'tab=reviews')
bs = BeautifulSoup(html.read(), 'html.parser')
naglowki = bs.find_all('.user-post user-post__card js_product-review')
for nr,x in enumerate(naglowki):
    print(nr, x.get_text())