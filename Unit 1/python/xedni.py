import string

def makeDictionary(docs):

    words = " ".join((" ".join(docs)).split('\t'))

    words = words.translate(str.maketrans('', '', string.punctuation))

    dicti = list(set(words.split(" ")))

    dicti.sort()

    return dicti

def makeXedni(dicti, docs):
    xedni = dict()

    for i in dicti:
        xedni[i] = [0,[]]
        for jind, j in enumerate(docs):
            if i in j:
                xedni[i][0]+=1
                xedni[i][1].append(jind)

    return xedni


if __name__ == "__main__":
    with open('../text files/movies2.txt', 'r', encoding = "utf-8") as fp:
        v = fp.read()

    v = v.lower()

    docs = v.split('\n')[:1000]

    dicti = makeDictionary(docs)

    xedni = makeXedni(dicti, docs)

    file = open('../text files/invertedIndex.txt', 'w', encoding="utf-8")
    file.write(str(xedni))
    file.close()