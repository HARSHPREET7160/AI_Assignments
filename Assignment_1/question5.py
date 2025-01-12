# D is a dictionary defined as D= {1:”One”, 2:”Two”, 3:”Three”, 4: “Four”, 5:”Five”}. 
# (i) WAP to add new entry in D; key=6 and value is “Six” 
# (ii) WAP to remove key=2. 
# (iii) WAP to check if 6 key is present in D. 
# (iv) WAP to count the number of elements present in D. 
# (v) WAP to add all the values present D.



D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

#(i) Add new entry
D[6] = "Six"
print("Dictionary after adding new entry:", D)

#(ii) Remove key=2
D.pop(2, None)
print("Dictionary after removing key 2:", D)

#(iii) Check if key=6 is present
print("Is key 6 present?", 6 in D)

#(iv) Count the number of elements
print("Number of elements in dictionary:", len(D))

#(v) Add all values in dictionary
print("All values in dictionary:", ", ".join(D.values()))
