from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

html = urlopen('https://www.ceneo.pl/96961305/opinie-1')
bs = BeautifulSoup(html.read(), 'html.parser')

# class scrapper():
    # def __init__(self):
id = bs.find_all('div', class_='user-post')
naglowki = bs.find('h1').get_text()
file = open('scrapped.json', 'a', encoding='utf-8')

    # def scrap(self):
array =[]
for i in range(1):
    author = id[i].find(class_='user-post__author-name').get_text()
    recomend = id[i].find(class_='user-post__author-recomendation').get_text()
    score = id[i].find(class_='user-post__score-count').get_text()
    time = id[i].find(class_='user-post__published').get_text()
    text = id[i].find(class_='user-post__text').get_text()
    if id[i].find(class_='review-feature') == None:
        pluses = 0
    else:
        pluses = id[i].find(class_='review-feature').get_text()
    usefulness = id[i].find(class_='js_product-review-usefulness vote').get_text()
    bought = id[i].find('em').get_text()
    array.append(author)
    array.append(recomend)
    array.append(score)
    array.append(time)
    array.append(text)
    array.append(pluses)
    array.append(usefulness)
    array.append(bought)
    file.write(str(array))
    file.close()

def chomps(s):
    return s.rstrip('\n')

# for i in range(1):

    # t = list(map(lambda x:x.strip(), list(author[i].get_text())))
    # a = ''
    # array.append(author[0].get_text().replace("\n", ""))
    # array.append(recomend[0].get_text().replace("\n", ""))
    # array.append(text[0].get_text().replace("\n", ""))
    # array.append(usefulness[0].get_text().replace("\n", ""))

    # for j in t:
    #     a += str(j)
    # array.append(a)

    # t = list(map(lambda x:x.strip(), list(recomend[i].get_text())))
    # a = ''

    # for j in t:
    #     a += str(j)
    # array.append(a)

    # t = list(map(lambda x:x.strip(), list(score[i].get_text())))
    # a = ''

    # for j in t:
    #     a += str(j)
    # array.append(a)

    # t = list(map(lambda x:x.strip(), list(time[i].get_text())))
    # a = ''

    # for j in t:
    #     a += str(j)
    # array.append(a)

    # t = list(map(lambda x:x.strip(), list(text[i].get_text())))
    # a = ''

    # for j in t:
    #     a += str(j)
    # array.append(a)

    # t = list(map(lambda x:x.strip(), list(pluses[i].get_text())))
    # a = ''

    # for j in t:
    #     a += str(j)
    # array.append(a)

    # t = list(map(lambda x:x.strip(), list(usefulness[i].get_text())))
    # a = ''

    # for j in t:
    #     a += ' ' + str(j)
    # array.append(a)

    # if bought[i] == '':
    #     array.append('0')
    # else:
    #     array.append('1')


# file.write('1')
# file.close()

