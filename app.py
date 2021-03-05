# from urllib.request import urlopen
# from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# a = '96231488' # Zmienić w przypadku gotowej strony
# html = urlopen('https://www.ceneo.pl/'+a+'tab=reviews')
# bs = BeautifulSoup(html.read(), 'html.parser')
# naglowki = bs.find_all('.user-post user-post__card js_product-review')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scrap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class article(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<article %r>' % self.id 


# for nr,x in enumerate(naglowki):
#     print(nr, x.get_text())

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/extract')
def extract():
    return render_template('extract.html')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)