# Compare Two Paragraphs
from src import textanalytics as ta

#get input from user
p1=input("Enter paragraph 1: ")
p2=input("Enter paragraph 2: ")

#get the wordcount dictionaries from the textanalytics pacakge
d1=ta.wordcount(p1)
d2=ta.wordcount(p2)

# Show the union - words in paragraph 1 that are in paragraph 2
l=ta.a_union_b(d1,d2)
print("Words in both paragraphs")
print(l)

# Show words in Paragraph 1 that aren't in Paragraph 2
l=ta.in_a_not_in_b(d1,d2)
print("Words in Paragraph 1 that aren't in Paragraph 2")
print(l)


# Show words in Paragraph 2 that aren't in Paragraph 1
l=ta.in_a_not_in_b(d2,d1)
print("Words in Paragraph 2 that aren't in Paragraph 1")
print(l)
