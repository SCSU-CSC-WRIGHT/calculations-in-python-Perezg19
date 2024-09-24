# This is my lab 2
weight_kilo = float(input("Enter your weight in kilograms: "))
meter_height = float(input("Enter your height in meters: "))
bmi_calc = (weight_kilo/(meter_height**2))
print(f"Your BMI is: {bmi_calc}.")
if bmi_calc < (18.5): print("You are not within the healthy BMI range.")
elif bmi_calc > (24.9): print("You are not within the healthy BMI range.")
else: print("You are within the healthy BMI range.")