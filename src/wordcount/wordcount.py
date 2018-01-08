# a complete program to split words
userwords=input("enter some words:")

wordlist=userwords.split()

wordcount = dict()
for word in wordlist:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1

for key,value in wordcount.items():
  print(key,"\t",value)
