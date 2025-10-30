string=str(input("Enter a string:"))
letter_count=0
digit_count=0
for i in string:
    if i.isalpha():
        letter_count+=1
    if i.isdigit():
        digit_count+=1
print("LETTERS : ",letter_count)
print("DIGITS COUNT : ",digit_count)
