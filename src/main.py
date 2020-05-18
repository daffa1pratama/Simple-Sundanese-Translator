from KamusReader import *
from Parser import *
from kmp import *
from bm import *
from reg import *
import re

# # text = 'nami abdi Riyugan'
# text = 'nama adik kamu siapa?'
# text = 'saya tidak bisa bahasa Sunda'
text = 'abdi teh sanes jalma Bandung'

tanda = ['?', ',', '.', ';', '/']

reader = KamusReader()
container = reader.readKamus('sunda')

parser = Parser()
new_container = parser.parse(text)

trans_container = []

alg = kmp()
# alg = bm()
# alg = reg()

for word in new_container:
    found = False
    temp = []
    for line in container:
        if (word in tanda):
            break
        else:
            if (alg.match(line[0], word) != -1 and len(word) == len(line[0])):
                print(line[0])
                temp.append(line[1])
                found = True
    if (found):
        stream = temp[0]
        if (len(temp) > 1):
            for i in range(1, len(temp)):
                stream += '/' + temp[i]
        trans_container.append(stream)
    else:
        trans_container.append(word)

print(trans_container)