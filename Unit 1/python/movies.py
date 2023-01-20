import numpy as np
import string

with open('movies2.txt', 'r', encoding = "utf-8") as fp:
    v = fp.read()

v = v.lower()

docs = v.split('\n')[:1000]

words = " ".join(docs)

words = words.translate(str.maketrans('', '', string.punctuation))

dicti = list(set(words.split(" ")))

file = open('dict.txt', 'w', encoding="utf-8")
file.write("\n".join(dicti))
file.close()

title = []

print(len(dicti), len(docs))
for i in docs:
    title.append(i.split('\t')[0])

file = open('titles.txt', 'w', encoding="utf-8")
file.write("\n".join(title))
file.close()

matrix = np.zeros((len(dicti), len(docs)), dtype=int)

for ind1, i in enumerate(dicti):
    print(ind1*100/len(dicti))
    for ind2, j in enumerate(docs):
        if i in j:
            matrix[ind1, ind2] = 1
print(matrix)


np.savetxt("incidenceMatrix.txt", matrix, delimiter="", fmt ="%d")