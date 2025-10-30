string=str(input("Enter string"))
arr=string.split(" ")
frequency=[]
for word in arr:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency.append(word)
print(frequency)
for i in arr:
    print(i,":",frequency[i])
