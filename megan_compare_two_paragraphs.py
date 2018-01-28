#Compare 2 paragraphs

from src import textanalytics as ta

p1=input("Enter paragraph one: ")

p2=input("Enter paragraph two: ")

d1 = ta.wordcount(p1)
d2 = ta.wordcount(p2)

#print("Words in paragraph one: ", d1)
#print("Words in paragraph two: ", d2)

d3=ta.a_union_b(p1,p2)
print("The words those two paragraphs have in common are: ")
for k,v in d3.items():
    print(k,"\t",v)

l1=ta.in_a_not_b(d1,d2)
l2=ta.in_a_not_b(d2,d1)

print("The words in the first paragraph that are not in the second are: ")
for i in l1:
    print(i)
print("The words in the second paragraph that are not in the first are: ")
for i in l2:
    print(i)
