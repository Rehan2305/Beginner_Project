print("Welcome to the BMI Calculator!")

weight = float(input("What's your weight in kg? "))
height = float(input("And your height in meters? "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {round(bmi, 2)}")

if bmi < 18.5:
    print("You're underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You're overweight.")
else:
    print("You're obese.")
