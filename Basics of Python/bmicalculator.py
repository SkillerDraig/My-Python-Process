# This is a project that calculates teenager bmi detailed
# It will ask you for your weight, height, age and gender
# Then it will calculate your bmi and give you a detailed report about it

age = float(input("Please enter your age: "))
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in cm: "))
gender = input("Please enter your gender (male/female): ").lower()

bmi = weight / ((height/100) ** 2)

if age < 18:
    if gender == "male":
        if bmi < 18.5:
            print("Your BMI is", round(bmi, 2), "which is considered underweight for your age and gender.")
        elif 18.5 <= bmi < 24.9:
            print("Your BMI is", round(bmi, 2), "which is considered normal weight for your age and gender.")
        elif 25 <= bmi < 29.9:
            print("Your BMI is", round(bmi, 2), "which is considered overweight for your age and gender.")
        else:
            print("Your BMI is", round(bmi, 2), "which is considered obese for your age and gender.")
    elif gender == "female":
        if bmi < 18.5:
            print("Your BMI is", round(bmi, 2), "which is considered underweight for your age and gender.")
        elif 18.5 <= bmi < 24.9:
            print("Your BMI is", round(bmi, 2), "which is considered normal weight for your age and gender.")
        elif 25 <= bmi < 29.9:
            print("Your BMI is", round(bmi, 2), "which is considered overweight for your age and gender.")
        else:
            print("Your BMI is", round(bmi, 2), "which is considered obese for your age and gender.")
else:
    print("Your BMI is", round(bmi, 2), "which is considered adult BMI. Please consult a doctor for more information.")

