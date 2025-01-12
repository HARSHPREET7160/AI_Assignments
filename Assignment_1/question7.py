# (i) Write a function which takes principal amount, interest rate and time. This function returns 
# compound interest. Call this function to print the output. 
# (ii) Save this function (as a module) in a python file and call it in another python file.
  
def calculate_compound_interest(principal, rate, time):
    return principal*((1+rate/100)**time)-principal

if __name__ == "__main__":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time (in years): "))

    ci = calculate_compound_interest(principal, rate, time)
    print(f"Compound Interest: {ci:.2f}")
    