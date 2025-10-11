punctuation=["!","-","@","$","%","&",":",";",".",",","#","(",")","[","]","{","?","|","/","<",">"]
string=str(input("Enter a string:" ))
without_Punctuation=""
for i in string:
    if i not in punctuation:
          without_Punctuation=without_Punctuation+i
print(without_Punctuation)
