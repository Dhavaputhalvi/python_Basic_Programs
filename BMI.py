weight=float(input("enter your weight(kg) :"))
height=float(input("enter your height (m) :"))
bmi=(weight*(height**2))

print(f"Your BMI is : {bmi}")
if bmi<=18.5:
    print("you are underweighht")
elif bmi<=24.9:
    print("you are normal")
else:
    print("You are obese")
