# Import Class and Library
from KamusReader import *
from Parser import *
from AlgKMP import *
from AlgBM import *
from AlgRegex import *
import sys

# Global Variables
global mark, kamus, stopwords
mark = ['?', ',', '.', ';', '/']
stopwords = ['abdi', 'aing', 'dewek', 'kaula', 'kuring', 'urang', 'anjeun', 'hidep', 'maneh', 'sia', 'anjeunna', 'manehna', 'ini', 'itu']

# translateAll Function
# Translate with Find All method, giving all possible word in Kamus 
def translateAll(alg, text, translate) :
    trans_container = []
    i = 0
    # Translate word
    for i in range(len(text)) :
        found = False
        temp = []
        # Search word in kamus
        for line in kamus:
            # Ignore mark
            if (text[i] in mark):
                break
            # Adding all possible translation
            else :
                if (alg.match(line[0], text[i]) != -1 and len(text[i]) == len(line[0])):
                    temp.append(line[1])
                    found = True
        # Found translation in kamus
        if (found):
            stream = temp[0]
            if (len(temp) > 1):
                for i in range(1, len(temp)):
                    stream += '/' + temp[i]
            trans_container.append(stream)
            # 'Teh' adder
            # 'Teh' word added after any word in stopwords
            if (translate == 'Indonesia' and any(elm in temp for elm in stopwords) and len(text) != 1) :
                trans_container.append('teh')
        # Word not in Kamus
        else:
            # 'Teh' remover
            # 'Teh' word removed after any word in stopwords
            if (translate == 'Sunda' and text[i-1] in stopwords) :
                if (text[i] != 'teh') :
                    trans_container.append(text[i])
            # If word not in kamus just add it
            else :
                trans_container.append(text[i])
        i += 1

    # Construct output
    result = trans_container[0]
    for i in range(1, len(trans_container)) :
        result += " " + trans_container[i]
    return(result)

# translateFirst Function
# Translate with Find First method. It will return first translation found in Kamus 
def translateFirst(alg, text, translate) :
    trans_container = []
    i = 0
    for i in range(len(text)) :
        found = False
        temp = []
        # Translate word
        for line in kamus:
            # Ignore mark
            if (text[i] in mark):
                break
            # Adding first translation
            else :
                if (alg.match(line[0], text[i]) != -1 and len(text[i]) == len(line[0])):
                    trans_container.append(line[1])
                    found = True
                    break
        # Found translation in kamus
        if (found):
            # 'Teh' adder
            # 'Teh' word added after any word in stopwords
            if (translate == 'Indonesia' and line[1] in stopwords and len(text) != 1) :
                trans_container.append('teh')
        else:
            # 'Teh' remover
            # 'Teh' word removed after any word in stopwords
            if (translate == 'Sunda' and text[i-1] in stopwords) :
                if (text[i] != 'teh') :
                    trans_container.append(text[i])
            # If word not in kamus just add it
            else :
                trans_container.append(text[i])
        i += 1

    # Construct output
    result = trans_container[0]
    for i in range(1, len(trans_container)) :
        result += " " + trans_container[i]
    return(result)

# getTextFromArg Function
# Return text from given argument
def getTextFromArg(arg) :
    text = sys.argv[4]
    i = 5
    while (i < (len(sys.argv))) :
        text += " " + sys.argv[i]
        i += 1
    return text

# getAlgorithmFromArg Function
# Return algorithm from given argument (KMP/BM/Regex)
def getAlgorithmFromArg(arg) :
    algorithm = sys.argv[2]
    if (algorithm == 'KMP') :
        alg = AlgKMP()
    elif (algorithm == 'BM') :
        alg = AlgBM()
    else :
        alg = AlgRegex()
    return alg

# getTranslateFromArg Function
# Return translate from given argument (Indonesia/Sunda)
def getTranslateFromArg(arg) :
    translate = sys.argv[1]
    return translate

# getFindFromArg Function
# Return find method from given argument (All/First)
def getFindMethodFromArg(arg) :
    return sys.argv[3]

# === Main Program ===

# Load all given argument
text = getTextFromArg(sys.argv)
alg = getAlgorithmFromArg(sys.argv)
translate = getTranslateFromArg(sys.argv)
findMethod = getFindMethodFromArg(sys.argv)

# Load kamus
reader = KamusReader()
kamus = reader.readKamus(translate.lower())

# Parse given text
parser = Parser()
text = parser.parse(text)

# Translate given text
if (findMethod == 'All') :
    result = translateAll(alg, text, translate)
else :
    result = translateFirst(alg, text, translate)

# Print output
print(result)