
# a = {}
# b = ['boolean', 'boolean', 'id']
# c = [2, 2, 2]       
        
        
# for i in range(len(b)):
#     a.update({b[i]:c[i]})

# print(a)

# for (key,value) in a.items():
#     print({key:value})
import math

import json
file = open('products/66746140.json')
score = [el for el in json.load(file)]
score_sum = 0
for i in score:
    score_sum += eval(i['score'])

print(score_sum)
print(len(score))
print(score_sum/len(score)*5)
print(round(score_sum/len(score)*5, 2))
