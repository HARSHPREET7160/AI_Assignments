# Write a Python Program to input basic salary of an employee and calculate its Gross salary 
# according to following: Basic Salary <= 10000 : HRA = 20%, DA = 80% Basic Salary <= 20000 
# : HRA = 25%, DA = 90% Basic Salary > 20000 : HRA = 30%, DA = 95%.


Basic_Salary = float(input("Enter the basic salary: "))

if Basic_Salary <= 10000:
    Hra = 0.20 * Basic_Salary
    Da = 0.80 * Basic_Salary
elif Basic_Salary <= 20000:
    Hra = 0.25 * Basic_Salary
    Da = 0.90 * Basic_Salary
else:
    Hra = 0.30 * Basic_Salary
    Da = 0.95 * Basic_Salary

gross_salary = Basic_Salary + Hra + Da
print(f"Gross Salary: {gross_salary:.2f}")
