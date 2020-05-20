from KamusReader import *
from Parser import *
from AlgKMP import *
from AlgBM import *
from AlgRegex import *
import re
import sys

# # text = 'nami abdi Riyugan'
# text = 'nama adik kamu siapa?'
# text = 'saya tidak bisa bahasa Sunda'
# text = 'abdi teh sanes jalma Bandung'

global mark, kamus, stopwords
mark = ['?', ',', '.', ';', '/']
stopwords = ['abdi', 'aing', 'dewek', 'kaula', 'kuring', 'urang', 'anjeun', 'hidep', 'maneh', 'sia', 'anjeunna', 'manehna', 'ini', 'itu']

def translateAll(alg, text, translate) :
    trans_container = []
    i = 0
    for i in range(len(text)) :
        found = False
        temp = []
        for line in kamus:
            if (text[i] in mark):
                break
            else:
                if (alg.match(line[0], text[i]) != -1 and len(text[i]) == len(line[0])):
                    temp.append(line[1])
                    found = True
        if (found):
            stream = temp[0]
            if (len(temp) > 1):
                for i in range(1, len(temp)):
                    stream += '/' + temp[i]
            trans_container.append(stream)
            # 'Teh' adder
            if (translate == 'Indonesia' and any(elm in temp for elm in stopwords) and len(text) != 1) :
                trans_container.append('teh')
        else:
            # 'Teh' remover
            if (translate == 'Sunda' and text[i-1] in stopwords) :
                if (text[i] != 'teh') :
                    trans_container.append(text[i])
            # If word not in kamus
            else :
                trans_container.append(text[i])
        i += 1
    result = trans_container[0]
    for i in range(1, len(trans_container)) :
        result += " " + trans_container[i]
    return(result)

def translateFirst(alg, text, translate) :
    trans_container = []
    i = 0
    for i in range(len(text)) :
        found = False
        temp = []
        for line in kamus:
            if (text[i] in mark):
                break
            else:
                if (alg.match(line[0], text[i]) != -1 and len(text[i]) == len(line[0])):
                    trans_container.append(line[1])
                    found = True
                    break
        if (found):
            # 'Teh' adder
            if (translate == 'Indonesia' and any(elm in temp for elm in stopwords) and len(text) != 1) :
                trans_container.append('teh')
        else:
            # 'Teh' remover
            if (translate == 'Sunda' and text[i-1] in stopwords) :
                if (text[i] != 'teh') :
                    trans_container.append(text[i])
            # If word not in kamus
            else :
                trans_container.append(text[i])
        i += 1
    result = trans_container[0]
    for i in range(1, len(trans_container)) :
        result += " " + trans_container[i]
    return(result)

def getTextFromArg(arg) :
    text = sys.argv[4]
    i = 5
    while (i < (len(sys.argv))) :
        text += " " + sys.argv[i]
        i += 1
    return text

def getAlgorithmFromArg(arg) :
    algorithm = sys.argv[2]
    if (algorithm == 'KMP') :
        alg = AlgKMP()
    elif (algorithm == 'BM') :
        alg = AlgBM()
    else :
        alg = AlgRegex()
    return alg

def getTranslateFromArg(arg) :
    translate = sys.argv[1]
    return translate

def getFindMethodFromArg(arg) :
    find = sys.argv[3]
    if (find == 'All') :
        return 'All'
    return 'First'

text = getTextFromArg(sys.argv)
alg = getAlgorithmFromArg(sys.argv)
translate = getTranslateFromArg(sys.argv)
findMethod = getFindMethodFromArg(sys.argv)

reader = KamusReader()
kamus = reader.readKamus(translate.lower())

parser = Parser()
text = parser.parse(text)

if (findMethod == 'All') :
    result = translateAll(alg, text, translate)
else :
    result = translateFirst(alg, text, translate)
print(result)