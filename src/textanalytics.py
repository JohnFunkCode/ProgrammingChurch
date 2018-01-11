
def wordcount(userwords):

    wordlist=userwords.split()

    wordcount = dict()
    for word in wordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount

def inanotinb(da, db):
    anotb = list()
    keysa=da.keys()
    keysb=db.keys()
    for word in keysa:
        if word not in keysb:
#            print("count not find :" + word)
            anotb.append(word)
#        else:
#            print("found :" + word)
    return anotb
