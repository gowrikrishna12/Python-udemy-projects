height = int(input("Enter your height")
weight = int("Enter your weight")

bmi =weight/height**2
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("Overweight")

