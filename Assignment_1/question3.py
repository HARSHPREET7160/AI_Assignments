# Write a Python program to check the validity of password input by users.  
# Validation:  
#  At least 1 letter between [a-z] and 1 letter between [A-Z].  
#  At least 1 number between [0-9].  
#  At least 1 character from [$#@].  
#  Minimum length 6 characters.  
#  Maximum length 16 characters.

import re
PASSWORD = input("Enter the password: ")

if (6 <= len(PASSWORD) <= 16 and
    re.search("[a-z]", PASSWORD) and
    re.search("[A-Z]", PASSWORD) and
    re.search("[0-9]", PASSWORD) and
    re.search("[$#@]", PASSWORD)):
    print("Password is valid.")
else:
    print("Password is invalid.")
