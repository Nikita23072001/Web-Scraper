# from urllib.request import urlopen
# from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for

# a = '96231488' # Zmienić w przypadku gotowej strony
# html = urlopen('https://www.ceneo.pl/'+a+'tab=reviews')
# bs = BeautifulSoup(html.read(), 'html.parser')
# naglowki = bs.find_all('.user-post user-post__card js_product-review')
app = Flask(__name__)
host='0.0.0.0'
port=5000

# for nr,x in enumerate(naglowki):
#     print(nr, x.get_text())


@app.route('/home')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)