# WAP to create a list of 100 random numbers between 100 and 900. Count and print the:  
# (i) All odd numbers 
# (ii) All even numbers 
# (iii) All prime numbers 


import random
numbers = [random.randint(100, 900) for _ in range(100)]
print("Generated numbers between 100 and 900:", numbers)
print('\n')

# (i) All odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers between 100 and 900:", odd_numbers)
print('\n')

# (ii) All even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers between 100 and 900:", even_numbers)
print('\n')

# (iii) All prime numbers
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]
print("Prime numbers between 100 and 900:", prime_numbers)
