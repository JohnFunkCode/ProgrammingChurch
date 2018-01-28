


from src import textanalytics as ta
# userwords1=input("enter some words:")
# userwords2=input("enter some words:")
# d1=ta.wordcount(userwords1)
# d2=ta.wordcount(userwords2)
# print("Words from the first sentence are: ",d1)
# print("Words from the second sentence are: ",d2)

userwords1=input("enter some words:")
userwords2=input("enter some words:")
u=ta.union(userwords1, userwords2)
print("THe common words are:")
for word in u:
    print(word)
