import re
import numpy as np
from scipy.spatial.distance import cosine

file = open('text.txt', 'r')
text = file.read().lower()
file.close()


text = [i.strip() for i in list(filter(('').__ne__, text.split('.')))]

words = []

for i in text:
    string = re.split(r'[^a-z]+', i.lower())
    string = list(filter(('').__ne__, list(set(string))))
    for i in string:
        if i not in words:
            words.append(i)

matrix = np.zeros((len(text), len(words)))

for word in enumerate(words):
    j = word[0]
    for i in range(len(text)):
        matrix[i][j] = re.split(r'[^a-z]+', text[i].lower()).count(word[1])

cos_dis = {}

for string in enumerate(matrix[1:len(matrix)+1]):
    cos_dis[string[0] + 1] = cosine(matrix[0], string[1])

print(cos_dis)


