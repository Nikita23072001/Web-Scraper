from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

html = urlopen('https://www.ceneo.pl/96961305/opinie-1')
bs = BeautifulSoup(html.read(), 'html.parser')

class scrapper():
    id = bs.find_all('div', class_='user-post')

    def scrap(self)
    # naglowki = bs.find_all('h1')
    # author = bs.find_all(class_='user-post__author-name')
    # recomend = bs.find_all(class_='user-post__author-recomendation')
    # score = bs.find_all(class_='user-post__score-count')
    # time = bs.find_all(class_='user-post__published')
    # text = bs.find_all(class_='user-post__text')
    # pluses = bs.find_all(class_='review-feature')
    # usefulness = bs.find_all(class_='js_product-review-usefulness vote')
    # bought = bs.find_all('em')

file = open('scrapped.json', 'a', encoding='utf-8')
array = []



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

