from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import Scrapper, math, json

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
@app.template_filter('count')
def count(key):
    score_sum = 0
    minus = 0
    plus = 0
    file = open(f'products/{key}.json')
    data = [el for el in json.load(file)]
    try:
        opinions = int(Scrapper.Scrapper(key).ops[0])
    except:
        return 0, 0, 0, 0
    for i in data:
        score_sum += eval(i['score'])

        if i['negatives'] == []:
            minus += 0
        else:
            minus += len(i['negatives'])

        if i['positives'] == []:
            plus += 0
        else:
            plus += len(i['positives'])
        
    # score_sum = round(score_sum/len(data)*5, 2)

    return f"Liczba Opinii: {opinions} Średnia Ocena:  {round(score_sum/len(data)*5, 2)}, Liczba Wad: {minus}, Liczba Zalet: {plus}"


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html', count = count, products_dict=products_dict)


@app.route('/extract', methods=['POST','GET'])
def extract():
    if request.method == "POST":
        try:
            product_code = request.form['product_code']
            Scrapper.Scrapper(product_code).main_func()
            products_dict.update({product_code:Scrapper.Scrapper(product_code).naglowki})
            return redirect('/products')
        except:
            return redirect('/ERROR')
    else:
        return render_template('extract.html')

@app.route('/ERROR')
def error():
    return render_template("error.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)