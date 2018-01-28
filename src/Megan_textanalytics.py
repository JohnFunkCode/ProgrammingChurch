#This is text analytics.py
# a complete program to split words
def wordcount(userwords):
    wordlist=userwords.split()

    wordcount = dict()
    for word in wordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    '''
    for key,value in wordcount.items():
      print(key,"\t",value)
      '''
    return wordcount

def wordcount_test():
    s1="1"
    s2="1 2 3"

    assert(len(wordcount(s1))==1)
    assert(len(wordcount(s2))==3)




#create a union function (the words from two dictionaries that match)

def a_union_b(d1,d2):
    union = dict()

    wordlist1=d1.split()
    wordlist2=d2.split()

#    print("** input d1: ",d1)
#    print("** input d2: ",d2)

    for word1 in wordlist1:
        if word1 in wordlist2:
#            print("** ", word1," is in the set ", wordlist2)
            if word1 in union:
#                print("** ", word1," occured again")
                union[word1] += 1
            else:
#                print("** ", word1," occured the first time")
                union[word1] = 1
    return union


def a_union_b_test():
    p1="1 2 3"
    p2="2 3 4"
    d3=a_union_b(p1,p2)
    len(d3)
    assert(len(d3)==2)
    l=d3.keys()
    assert(len(l)==2)
#    assert(len(d3)==3)

    p1="1 2 1"
    p2="1 2 3"
    d3=a_union_b(p1,p2)
    l=d3.keys()
    assert(len(l)==2)


#create a function to find words in 1st dictionary that are not in the second

def in_a_not_b(d1,d2):
    l=list()
    for word in d1:
        if word not in d2:
            l.append(word)
    return l

def in_a_not_b_test():
    d1={"1":1,"2":1,"3":1}
    d2={"2":1,"3":1,"4":1}
    l=in_a_not_b(d1,d2)
    assert(len(l)==1)
    assert(l == ["1"])

if __name__ == "__main__":
    print("this is textanalytics")
    wordcount_test()
    a_union_b_test()
    in_a_not_b_test()
    print("all tests executed successfully")
