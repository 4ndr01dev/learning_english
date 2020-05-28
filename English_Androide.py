# *               0ANDROIDEV
# *                 2020
# * _____________________________________________________________
'''                                                  
                                #                   
                               ###                  
                              #####                 
                             #######                
                            ###### ##               
                           ###### ####              
                          ##### #######             
                         ####     ######            
                        ####        #####           
                       ###           #####          
                      ###              ####         
                     ##                  ###        
                    #                      ##       
                   #                         #      
'''
import sys
# insert at 1, 0 is the script path (or '' in REPL)
from jsonPy import jsonPy
import os

def addWord(word:str = None):

    defined = False

    while word == None:
        word = input('❔ Enter a new word:    ')
        if findWordName(word): 
            
            concept = findWordName(word)
            for key in concept:
                print(key,'----->',concept[key])
                if concept[key] == None:
                    auxConcept = input('if you want to learn more, you could add now')
                    concept[key] = auxConcept
            print(concept)
            jsonPy.editItem(currJson,currDict,concept)
            return False


    mean = askMening(word)

    esp = askSpanishTranslation()

    sent = askSentence()

    dic = {'word': word, 'defined': defined, 'meaning': mean,'translation': esp, 'example': sent}

    if jsonPy.findField(currJson,currDict):
        if jsonPy.addItem(currJson,currDict,item = dic): print(dic['word'],' was added')

    else:
        if jsonPy.addField(currJson,currDict):
            if jsonPy.addItem(currJson, currDict, item = dic):
                print(dic['word'], ' was added')


def askMening(word):
    mean = input("❔ What does it mean? Or don't have a meaning yet ?:    ")
    if mean:
        print("✔️ We have a meaning now !")
        defined = True
        return mean
    else:
        print("⌚We need a mean later ...")
        return None


def askSpanishTranslation():

    esp = input("❔In spanish it's ... :    ")
    if esp:
        print("✔️ We have a spanish translation now !")
        defined = True
        return esp
    else:
        print("⌚We need a mean later ...")
        return None



def askSentence():

    sent = input("✍️ Make a sentence with that word, pal:    ")
    if sent:
        print("✔️ We have a sentence now !")
        defined = True
        return sent
    else:
        print("⌚We need a mean later ...")
        return None

def findWordName(word:str=None):
    item = jsonPy.findItem(currJson , itemValue=word)
    if item != None:
        return item
    else:
        print('you must create a new concept')
        return None

def findWord():
    word = input('You are looking for a word ?')
    return findWordName(word)


if 'data' in os.listdir(os.getcwd()):
    print('data folder allready exist')

currJson = 'words'
currDict = 'dictionary'
#!hacer una cuncion de menu para regresar aca
if jsonPy.findJson(currJson):
    print('allready exist a json')
else: 
    jsonPy.addNewJson(currJson)

print('1️⃣     add a new word')
print('2️⃣     find a word in my dictionary \n ')
x = input('Chose an option:     ')
if x == '1':
    addWord()
if x == '2':
    word = input('❔ word to find :    ')
    concept = findWordName(word)
    if concept == None:
        print("❌ We dont found it ! ")
        add = input('❔ Would you like to add it now ?  [y/n] ')
        if add == 'y':
            print("❕ lets added it ! ")
            addWord(word)
        if add == 'n':
            print("❌ Bye bye ")
    else:
        print("✔️  We found it ! \n ")
        for key in concept:

            print('     ⚜️   ', key, '----->', concept[key])


