import matplotlib.pyplot as plt
import numpy as np
import json

class charts():
    def __init__(self, product_code):
        plt.rcdefaults()
        self.fig, self.ax = plt.subplots()
        self.file = open(f'products/{product_code}.json', 'r', encoding="utf-8")

    def counter(self):
        data = json.load(self.file)
        people = set({})
        for el in data:
            people.add(el['score'])
        people = sorted(list(people))
        print(people)
        y_pos = np.arange(len(people))
        print(people)
        performance = []
        for i in range(len(people)):
            performance.append(0)
        for el in people:
            for i in data:
                if el == i['score']:
                    performance[people.index(el)] += 1

        self.ax.barh(y_pos, performance, align='center')
        self.ax.set_yticks(y_pos)
        self.ax.set_yticklabels(people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        return plt