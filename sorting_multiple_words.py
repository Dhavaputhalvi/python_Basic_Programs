word=input("Enter comma-seperated strings:")
words=word.split(",")
words.sort()
for i in words:
    if i==(len(words)-2):
       print(i)
    else:
       print(i,",")
