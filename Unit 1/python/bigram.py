import string

def makeDictionary(text):

    docs = text.split('\n')[:1000]

    # title = []

    # for i in docs:
    #     title.append(i.split('\t')[0])

    words = " ".join((" ".join(docs)).split('\t'))

    words = words.translate(str.maketrans('', '', string.punctuation))

    dicti = list(set(words.split(" ")))

    dicti.sort()

    return dicti

def makeBiGram(dicti):

    bigram = dict()

    for i in dicti:
        if len(i)>0:
            if i[0] not in bigram.keys():
                bigram[i[0]] = [i]
            else:
                bigram[i[0]].append(i)
            if i[-1] not in bigram.keys():
                bigram[i[-1]] = [i]
            else:
                bigram[i[-1]].append(i)
        
        i = i[1:len(i)]
        
        for j in range(2, len(i)):
            if i[j-2:j] not in bigram.keys():
                bigram[i[j-2:j]] = [i]
            else:
                bigram[i[j-2:j]].append(i)
    
    return bigram




if __name__ == "__main__":
    with open('../text files/movies2.txt', 'r', encoding = "utf-8") as fp:
        v = fp.read()

    v = v.lower()

    dicti = makeDictionary(v)

    bigram = makeBiGram(dicti)

    file = open('../text files/bigram.txt', 'w', encoding="utf-8")
    file.write(str(bigram))
    file.close()