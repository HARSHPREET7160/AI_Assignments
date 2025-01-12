import ci_module
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time (in years): "))
ci=ci_module.calculate_compound_interest(principal,rate,time)
print(f"Compound Interest: {ci:.2f}")