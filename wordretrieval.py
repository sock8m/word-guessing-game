import json
import random

def newword( previouswords ):
    f = open('words_dictionary.json')
    data = json.load(f)
    wordlist = list(data.keys())

    for word in previouswords:
        wordlist.remove(word)

    if len(wordlist)==0:
        return 0
    else:
        selection = random.choice(wordlist)
        return selection