from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.ceneo.pl/')
bs = BeautifulSoup(html.read(), 'html.parser')
naglowki = bs.find_all('div')
for nr,x in enumerate(naglowki):
    print(nr, x.get_text())