from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import Scrapper, math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scrap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

products_dict = {}


# class database_scrap(db.Model):
#     id  = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     product_code = db.Column(db.Integer, nullable=False)
#     revies = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<database_scrap %r>' % self.id 

class posts():
    def __init__(self):
        self.score_sum = 0
         self.data = []
         self.minus = 0
         self.plus = 0

    def count(self):
        for (key,value) in products_dict.items():
            file = open('products/' + key + '.json')
            self.data = [el for el in json.load(file)["score"]]
            for i in self.data:
                self.score_sum += eval(i['score'])

                if i['negatives'] == []:
                    continue
                else:
                    self.minus += len(i['negatives'])

                if i['positives'] == []:
                    continue
                else:
                    self.plus += len(i['positives'])


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    # opinions = int(Scrapper.Scrapper(key).ops[0])
    return render_template('products.html')


@app.route('/extract', methods=['POST','GET'])
def extract():
    if request.method == "POST":
        product_code = request.form['product_code']
        Scrapper.Scrapper(product_code).main_func()
        products_dict.update({product_code:Scrapper.Scrapper(product_code).naglowki})
    # return render_template("extract.html")
        return redirect('/products')
    else:
        return render_template('extract.html')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)