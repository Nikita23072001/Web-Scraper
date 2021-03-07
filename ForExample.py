from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

product_code = 84069007

html = Request(f'https://www.ceneo.pl/{product_code}/opinie-{i}')
webpage = urlopen(html)
bs = BeautifulSoup(webpage.read(), 'html.parser')
blocks = bs.find_all('div', class_='user-post user-post__card js_product-review')
print(webpage.geturl())