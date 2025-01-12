# Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80]. 
# (i) WAP to add 200 and 300 to L.  
# (ii) WAP to remove 10 and 30 from L. 
# (iii) WAP to sort L in ascending order. 
# (iv) WAP to sort L in descending order.



List = [10, -2, 30, 40, 95, -6, 7, 8]

#(i) Add 200 and 300 to L
List.extend([200, 300])
print("List after adding 200 and 300:", List)

#(ii) Remove 10 and 30 from L
List.remove(10)
List.remove(30)
print("List after removing 10 and 30:", List)

#(iii) Sort L in ascending order
List.sort()
print("List sorted in ascending order:", List)

#(iv) Sort L in descending order
List.sort(reverse=True)
print("List sorted in descending order:", List)
