import random
string=str(input("Enter a string:"))
rand_Number=random.randint(0,len(string))
print(rand_Number)
string=string[:rand_Number]+string[rand_Number+1:]
print(string)
