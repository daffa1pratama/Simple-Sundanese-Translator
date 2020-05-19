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

global tanda, kamus, stopwords

def doTranslate(alg, text, translate) :
    trans_container = []
    i = 0
    for i in range(len(text)) :
        found = False
        temp = []
        for line in kamus:
            if (text[i] in tanda):
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
        else:
            if (translate == 'Sunda' and text[i-1] in stopwords) :
                if (text[i] != 'teh') :
                    trans_container.append(text[i])
            else :
                trans_container.append(text[i])
        i += 1
    stream = trans_container[0]
    for i in range(1, len(trans_container)) :
        stream += " " + trans_container[i]
    return(stream)

def getTextFromArg(arg) :
    text = sys.argv[2]
    i = 3
    while (i < (len(sys.argv))) :
        text += " " + sys.argv[i]
        i += 1
    return text

translate = sys.argv[1]
text = getTextFromArg(sys.argv)

tanda = ['?', ',', '.', ';', '/']
stopwords = ['abdi', 'aing', 'dewek', 'kaula', 'kuring', 'urang', 'anjeun', 'hidep', 'maneh', 'sia', 'anjeunna', 'manehna']

reader = KamusReader()
kamus = reader.readKamus(translate.lower())

parser = Parser()
text = parser.parse(text)

alg = AlgKMP()
# alg = AlgBM()
# alg = AlgRegex()

result = doTranslate(alg, text, translate)
print(result)