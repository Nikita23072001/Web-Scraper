from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json, math, re, sys


class Scrapper():
    def __init__(self, product_code):

        self.product_code = int(product_code)
        try:
            self.html_first = urlopen(f'https://www.ceneo.pl/{self.product_code}')
            self.bs = BeautifulSoup(self.html_first.read(), 'html.parser')
            self.error = self.bs.find('abbr', title="Błąd 404")
            self.ops = self.bs.find_all('span', class_="page-tab__title js_prevent-middle-button-click")
            print(self.ops)
            if re.findall('\d+', self.ops[2].get_text()) == []:
                print("Nie ma")
                self.pages_number = 0
            else:
                self.pages_number = math.ceil(int(re.findall('\d+', self.ops[2].get_text())[0])/10)

            self.naglowki = self.bs.find('h1').get_text()


            self.file = open(f'{self.product_code}.json', 'a', encoding='utf-8')

            self.array =[]
        except:
            print("Strona nie istnieje, lub podałeś błędny kod produktu")
            sys.exit(1)

    def data(self, block):
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

        post_time = ''
        buy_time = ''
        for i in range(len(block.find_all('time'))):
            if i == 0:
                post_time = block.find_all('time')[i]["datetime"]
            elif i==1:
                buy_time = block.find_all('time')[i]["datetime"]

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

        vote_y = block.find('span', id=f"votes-yes-{id}").get_text().replace("\n", '')
        vote_n = block.find('span', id=f"votes-no-{id}").get_text().replace("\n", '')

        if block.find(class_='review-pz') == None:
            bought = 0
        else:
            bought = True

        self.array.append({"id":id, "Author":author, "recomend":recomend, "score":score, "text":text,
        "post_time":post_time, "buy_time":buy_time, "positives":pluses, "negatives":minus,
        "vote_y":int(vote_y), "vote_n":int(vote_n), "bought":bought})

    
    def main_func(self):
        for i in range(1, self.pages_number+1):
            html = Request(f'https://www.ceneo.pl/{self.product_code}/opinie-{i}')
            webpage = urlopen(html)
            self.bs = BeautifulSoup(webpage.read(), 'html.parser')
            blocks = self.bs.find_all('div', class_='user-post user-post__card js_product-review')
            print(webpage.geturl())

            # if blocks[i].find(class_='user-post__author-name') == None:
            for block in blocks:
                    self.data(block)


        self.array = json.dumps(self.array, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

        self.file.write(str(self.array))
        self.file.close()


Scrapper('12321').main_func()