# This is my lab 1
principal_amount = float(input("Enter the principal amount: "))
rate_interest = float(input("Enter the rate of interest: "))
period_years = int(input("Enter your time period in years: "))
simple_interest = ((principal_amount*rate_interest*period_years)/100)
print(f"Your simple interest is: {simple_interest}.")