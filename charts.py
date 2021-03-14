import json
import matplotlib.pyplot as plt
import numpy as np

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

        return plt
    
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

        return plt
