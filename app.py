from flask import Flask, render_template, url_for, request, redirect, Response, send_file
import Scrapper, math, json, io, matplotlib, glob, re, module, os, time
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__) #Flask

products_dict = {} #słownik typu numer:imie
for files in glob.glob('products/*.json', recursive=False):
    products_dict.update({re.findall('\d+', files)[0]:Scrapper.Scrapper(int(re.findall('\d+', files)[0])).naglowki})


class charts(): #tworzenie wykresów

    def __init__(self, product_code):
        file = open(f'products/{product_code}.json', 'r', encoding="utf-8")
        self.data = json.load(file)

    def bar(self): #Słupkowy
        plt.rcdefaults()
        fig, ax = plt.subplots()
        people = set({})
        for el in self.data:
            people.add(el['score'])
        people = sorted(list(people))
        y_pos = np.arange(len(people))
        performance = []
        for i in range(len(people)):
            performance.append(0)
        for el in people:
            for i in self.data:
                if el == i['score']:
                    performance[people.index(el)] += 1

        ax.barh(y_pos, performance, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Ilość opinii')
        ax.set_title('Wpływ poszczególnych ocen na średnią')
        bar = plt
        return bar
    
    def pie(self): #kołowy
        labels = ['Brak rekomendacji', 'Polecam', 'Nie polecam']
        explode = (0, 0, 0.3)
        sizes = [0, 0, 0]
        for i in self.data:
            if i['recomend'] == 0:
                sizes[0] += 1
            elif i['recomend'] == "Polecam":
                sizes[1] += 1
            elif i['recomend'] == "Nie polecam":
                sizes[2] += 1

        fig, ax = plt.subplots(figsize=(9, 5), subplot_kw=dict(aspect="equal"))

        def func(pct, allvals):
            absolute = int(pct/100.*np.sum(allvals))
            return "{:.1f}%\n({:d} opinii)".format(pct, absolute)


        wedges, texts, autotexts = ax.pie(sizes, autopct=lambda pct: func(pct, sizes),
                                                textprops=dict(color="black"), explode=explode)

        ax.legend(wedges, labels,
                        title="Legenda",
                        loc="center left",
                        bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=10, weight="bold")

        ax.set_title("Udział poszczególnych rekomendacji w ogólnej liczbie opinii")
        pie = plt

        return pie

@app.template_filter('count')
def count(key): #liczba opinii, wad, zalet, srednia
    score_sum = 0
    minus = 0
    plus = 0
    file1 = open(f'products/{key}.json', 'r', encoding='utf-8')
    data = [el for el in json.load(file1)]
    try:
        opinions = int(Scrapper.Scrapper(key).ops[0])
    except:
        return "Żadnych opinii!"
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


@app.route('/<path>.json')
def jsonfile(path):
    return send_file(f'products/{path}.json', as_attachment=True)

@app.route('/<path>.csv')
def csv(path):
    module.Convertising(path).convert_csv()
    return send_file(f'products/{path}.csv', as_attachment=True)
   
@app.route('/<path>.xlsx')
def xlsx(path):
    module.Convertising(path).convert_xlsx()
    return send_file(f'products/{path}.xlsx', as_attachment=True)

def delete_files():
    files1 = glob.glob('products/*.csv', recursive=False)
    files2 = glob.glob('products/*.xlsx', recursive=False)
    for file in files1:
        os.remove(file)

    for file in files2:
        os.remove(file)



@app.route('/')
@app.route('/home')
def index():#podstawowy
    return render_template('index.html')

@app.route('/products')
def products():#lista produkty
    delete_files()
    return render_template('products.html', count = count, products_dict=products_dict)

@app.route('/bar<int:key>.png')
def bar_png(key):#plik png jest przechowywany w bufforze w postaci Binarnej(zazwyczaj)
    fig = charts(key).bar()
    output = io.BytesIO()
    fig.savefig(output)
    return Response(output.getvalue(), mimetype="image/png")

@app.route('/pie<int:key>.png')
def pie_png(key):#plik png jest przechowywany w bufforze w postaci Binarnej(zazwyczaj)
    fig = charts(key).pie()
    output = io.BytesIO()
    fig.savefig(output)
    return Response(output.getvalue(), mimetype="image/png")


@app.route('/products/<int:product_code>', methods=['POST','GET'])
def product_detail(product_code):
    p_file = open(f'products/{product_code}.json', 'r', encoding="utf-8")  #W przypadku otwarcia pliku
    data = json.load(p_file)
    return render_template("product_detail.html", data=data, 
                                name=Scrapper.Scrapper(product_code).naglowki, 
                                bar=url_for('.bar_png', key=product_code), 
                                pie=url_for('.pie_png', key=product_code), 
                                jsonfile = url_for('.jsonfile', path=product_code), 
                                csv=url_for('.csv', path=product_code), 
                                xlsx=url_for('.xlsx', path=product_code))


@app.route('/extract', methods=['POST','GET'])
def extract(): #Scrapping
    if request.method == "POST":
        try:
            product_code = request.form['product_code']
            Scrapper.Scrapper(product_code).main_func()
            products_dict.update({product_code:Scrapper.Scrapper(product_code).naglowki})
            return redirect(url_for('.product_detail', product_code=product_code))
        except:
            return redirect(url_for('.error'))
    else:
        return render_template('extract.html')

@app.route('/ERROR')
def error(): #W przypadku błędu instaluje wirusa(np. Korone)
    return render_template("error.html")

@app.route('/about')
def about():# O nas
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=False)