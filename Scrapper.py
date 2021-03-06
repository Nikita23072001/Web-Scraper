from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json, codecs
import math

product_code = 96961305

html_first = urlopen(f'https://www.ceneo.pl/{product_code}/opinie-1')
bs = BeautifulSoup(webpage.read(), 'html.parser')

page_number = 1

html = Request(f'https://www.ceneo.pl/{product_code}/opinie-{page_number}')
webpage = urlopen(html)
print(webpage.geturl())
bs = BeautifulSoup(webpage.read(), 'html.parser')


blocks = bs.find_all('div', class_='user-post user-post__card js_product-review')
naglowki = bs.find('h1').get_text()
file = open('scrapped.json', 'a', encoding='utf-8')
print(blocks)

array =[]

def data():
    for block in blocks:
        id = block["data-entry-id"]
        author = block.find(class_='user-post__author-name').get_text().replace('\n', '')

        if block.find(class_='user-post__author-recomendation') == None:
            recomend = 0
        else:
            recomend = block.find(class_='user-post__author-recomendation').get_text().replace('\n', '')
        
        if block.find(class_='user-post__score-count') == None:
            score = 0
        else:
            score = block.find(class_='user-post__score-count').get_text().replace('\n', '')

        time = block.find(class_='user-post__published').get_text().replace('\n', '')

        text = block.find(class_='user-post__text').get_text().replace('\n', '')

        if block.find(class_='review-feature') == None:
            pluses = 0
        else:
            pluses = block.find(class_='review-feature').get_text().replace('\n', '')
        if block.find(class_='js_product-review-usefulness vote') == None:
            usefulness = 0
        else:
            usefulness = block.find(class_='js_product-review-usefulness vote').get_text().replace('\n', ' ')

        if block.find(class_='review-pz') == None:
            bought = 0
        else:
            bought = block.find(class_='review-pz').get_text().replace('\n', '')

        array.append({"id":id, "Author":author, "recomend":recomend, "score":score, "time":time, "text":text, "pluses":pluses, "usefulness":usefulness,"bought":bought})

print(len(blocks))

for block in blocks:
    if block.find(class_='user-post__author-name') == None:
        page_number += 1
        html = Request(f'https://www.ceneo.pl/{product_code}/opinie-{page_number}')
        webpage = urlopen(html)
        if webpage.geturl() == f'https://www.ceneo.pl/{product_code}#tab=reviews':
            break
    else:
        data()


array = json.dumps(array, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

file.write(str(array))
file.close()




