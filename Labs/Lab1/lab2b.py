'''
Name: John Niagwan
Student ID: 121092225
Tax calculator
'''
income = int(input("Enter your gross income:")) #Prompt the user to enter their gross income as an integer

dependants = int(input("Enter number of dependents:")) #Prompt the user to enter the number of dependents as an integer

if income <= 32000:
    taxrate = 0.1 #10% tax rate if income is 32,000 or less
elif 32000 < income <= 64000:
    taxrate = 0.15 #15% tax rate if income is over 32,000 and less 64,000
else:
    taxrate = 0.25 #25% tax rate if income is above 64,000

taxable_income = income - (10000 + (dependants * 2000)) #Calculate taxable income after accounting for a fixed deduction of 10,000 and additional deductions for each dependent (2,000 per dependent)

income_tax = int(taxable_income * taxrate) #Calculate income tax by multiplying taxable income with the determined tax rate

if income_tax < 0:
    income_tax = 0 #Ensure income tax is not negative (set it to 0 if it's negative)

output_message = f"The income tax is ${income_tax}" #Create an output message to display the calculated income tax
print(output_message) #Print the output message
