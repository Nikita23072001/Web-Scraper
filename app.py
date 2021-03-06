from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scrap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class database_scrap(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    product_code = db.Column(db.Integer, nullable=False)
    revies = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    # html = urlopen('https://www.ceneo.pl/'+product_code)
    # bs = BeautifulSoup(html.read(), 'html.parser')

    def __repr__(self):
        return '<database_scrap %r>' % self.id 

    # def name_scrap(self):
    #     return bs.find_all('h1')[0].get_text()

    # def reviews(self):
        



# for nr,x in enumerate(naglowki):
#     print(nr, x.get_text())

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

# @app.route('/extract', methods=['POST','GET'])
# def extract():
#     if request.method == "POST":
#         product_code = request.form['product_code']
#         name = 
#     else:
#         return render_template('extract.html')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)