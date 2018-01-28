def wordcount(userwords):

    wordlist=userwords.split()

    wordcount = dict()
    for word in wordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return(wordcount)

    #for key,value in wordcount.items():
      #print(key,"\t",value)

def union(paragraph1, paragraph2):
    common_words = list()
    wordcount1 = wordcount(paragraph1)
    wordcount2 = wordcount(paragraph2)

    keys1 = wordcount1.keys()
    keys2 = wordcount2.keys()

    for word in keys1:
        if word in keys2:
            #print("Supermatch! {} was found!".format(word))
            common_words.append(word)
        #else:
            #print("Sorry! {} was not found.".format(word))
    return common_words

def test_union():
    s1 = ("one two")
    s2 = ("two three four")
    common_words = union(s1, s2)


    assert(len(common_words) == 1)

    assert(common_words[0] == 'two')



def test_union2():
    s2 = ("one two")
    s1 = ("two three four")
    common_words = union(s1, s2)


    assert(len(common_words) == 1)

    assert(common_words[0] == 'two')


if __name__ == "__main__":
    print("This is test analytics")
    test_union()
    test_union2()
    print('All good, bro!')
