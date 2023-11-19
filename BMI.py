weight = float(input("Enter weight in kg:"))
height = float(input("Enter height in m:"))

height_in_metres = height / 100
bmi = weight / (height_in_metres ** 2)

print("Your BMI is:",bmi)

if bmi < 18.5:
    print("You're underweight")
elif 18.5 <= bmi < 25:
    print("You're a normal weight")
elif 25 <= bmi < 30:
    print("You're overweight")
