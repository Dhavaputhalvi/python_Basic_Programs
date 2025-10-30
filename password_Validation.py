import re
password=str(input("Enter a string:"))
if re.match(r"^(?=.*[a-z])(?=.*[A-Z})(?=.*[0-9])(?=.*[#@$%&]).{6,12}$",password):
    print("Password is valid")
else:
    print("Password is not valid")
