from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json, codecs
import math
import re

product_code = 84069007

html_first = urlopen(f'https://www.ceneo.pl/{product_code}/opinie-1')
bs = BeautifulSoup(html_first.read(), 'html.parser')
ops = bs.find_all('span', class_="page-tab__title js_prevent-middle-button-click")
print (ops[2].get_text())

pages_number = round(int(re.findall('\d+', ops[2].get_text())[0])/10)



naglowki = bs.find('h1').get_text()
file = open('scrapped.json', 'a', encoding='utf-8')

array =[]

def data(block):
    # for block in blocks:
    id = int(block["data-entry-id"])
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

    # pluses = [item.text for item in block.find(class_='review-feature__title--positives').parent(class_='review-feature__item')] if block.find(class_='review-feature__title--positives') else []
    pluses = []
    minus = []
    for col in block(class_='review-feature__col'):
        features = [item.text for item in col.find_all(class_='review-feature__item')]
        if col.find(class_='review-feature__title--positives'):
            pluses = features
        elif col.find(class_='review-feature__title--negatives'):
            minus = features

    if block.find(class_='js_product-review-usefulness vote') == None:
        usefulness = 0
    else:
        usefulness = block.find(class_='js_product-review-usefulness vote').get_text().replace('\n', ' ')

    if block.find(class_='review-pz') == None:
        bought = 0
    else:
        bought = block.find(class_='review-pz').get_text().replace('\n', '')

    array.append({"id":id, "Author":author, "recomend":recomend, "score":score, "time":time, "text":text, "positives":pluses, "negatives":minus, "usefulness":usefulness,"bought":bought})


for i in range(1, pages_number+1):
    html = Request(f'https://www.ceneo.pl/{product_code}/opinie-{i}')
    webpage = urlopen(html)
    bs = BeautifulSoup(webpage.read(), 'html.parser')
    blocks = bs.find_all('div', class_='user-post user-post__card js_product-review')
    print(webpage.geturl())
    if blocks[i].find(class_='user-post__author-name') == None:
        break
        # if page_number > pages_number:
        #     break
    else:
        for block in blocks:
            data(block)

print(len(blocks))

array = json.dumps(array, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

file.write(str(array))
file.close()

for i in range(10):
        if block.findNextSibling(attrs={"class" : 'review-feature__title--negatives'}) == None:
            None
        else:
            print(block.findNextSibling(attrs={"class" : 'review-feature__title--negatives'}).get_text())
