
def wordcount(userwords):

    wordlist=userwords.split()

    wordcount = dict()
    for word in wordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount

def a_union_b(a,b):
    union = list()
    keysa=a.keys()
    keysb=b.keys()
    for word in keysa:
        if word in keysb:
#            print("found :" + word)
            union.append(word)
    return union


def in_a_not_in_b(a, b):
    a_not_b = list()
    keysa=a.keys()
    keysb=b.keys()
    for word in keysa:
        if word not in keysb:
#            print("count not find :" + word)
            a_not_b.append(word)
#        else:
#            print("found :" + word)
    return a_not_b

def main():
    #One Word Tests
    d1=wordcount("one")
    assert len(d1)==1   # test there is only 1 word in the result
    assert d1["one"]==1 # test count of the word "one" is 1

    #Three Word Tests
    d2=wordcount("one two three")
    assert len(d2)==3  # test there are 3 words in the result
    assert d2["one"]==1 # test each word has a count of 1
    assert d2["two"]==1
    assert d2["three"]==1

    #test that a_union_b(['one','two','three'],['one']) returns 'one'
    u=ta.a_union_b(d1,d2)
    assert(u==['one'])

    #test that in_a_not_in_b of "one", "one" return an empty set
    assert in_a_not_in_b(d1,d1)==[]

    #test that in_a_not_in_b of ['one','two','three'],['one'] returns a set with both 'two' and 'three' in it
    l=in_a_not_in_b(d2,d1)
    assert("two" in l)
    assert("three" in l)


if __name__ == "__main__":
    main()
