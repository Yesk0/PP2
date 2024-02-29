import re

def zeroOrMoreB():
    txt = input()
    x = re.findall("ab*", txt)
    print(x)

def twoORthree():
    txt = input()
    x = re.findall("ab{2,3}", txt)
    print(x)

def sequenceOfLowerLetters():
    txt = input()
    l = []
    txt = txt.split('_')
    for i in range(0, len(txt) - 1):
        x1 = re.search("[a-z]", txt[i])
        x2 = re.search("[a-z]", txt[i + 1])
        if x1 and x2:
            l.append(txt[i] + "_" + txt[i + 1])
    print(l)

def findAa():
    txt = input()
    x = re.findall("[A-Z][a-z]+", txt)
    print(x)

def startWithAEndWithB():
    txt = input()
    x = re.findall("^a.*b$", txt)
    print(x)
startWithAEndWithB()

def replace():
    txt = input()
    x = txt
    x = re.sub("\\s", ":", txt)
    x = re.sub("[.]", ":", x)
    x = re.sub(",", ":", x)

def snakeToCamel():
    txt = input()
    x = txt.split("_")
    for i in range(1, len(x)):
        x[i] = x[i].capitalize()
    for x in x:
        print(x, end='')

def splitUpper():
    txt = input()
    x = txt
    for i in range(0, len(x)):
        if x[i].isupper():
            x1 = x[:i]
            x2 = x[i + 1:]
            x = x1 + ' ' + x2
    l = re.split("\\s", x)
    l2 = []
    for i in l:
        if len(i) != 0:
            l2.append(i)
    print(l) 
    print(l2)

def splitUpper2():
    txt = input()
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    print(x)

def camelToSnake():
    txt = input()    
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    x = x.split(' ')
    s = ''
    for i in range(0, len(x)):
        s += x[i].lower() + '_'
    print(s[:-1]) 
camelToSnake()