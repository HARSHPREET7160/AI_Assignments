# A class with 10 students wants to produce some information from the results of the four standard 
# tests in Maths, Science, English and IT. Each test is out of 100 marks. The information output 
# should be the highest, lowest and average mark for each test and the highest, lowest and average 
# mark overall. Write a program in Python to complete this task. 


students = {
    "Maths": [81, 6, 78, 100, 45, 88, 66, 98, 99, 54],
    "Science": [80, 50, 90, 55, 55, 88, 86, 87, 85, 90],
    "English": [55, 85, 85, 65, 95, 15, 85, 90, 60, 80],
    "IT": [70, 80, 50, 60, 30, 40, 100, 70, 50, 80],
}

for subject, marks in students.items():
    print(f"{subject} - Highest: {max(marks)}, Lowest: {min(marks)}, Average: {sum(marks) / len(marks)}")

all_marks = [mark for marks in students.values() for mark in marks]
print(f"Overall - Highest: {max(all_marks)}, Lowest: {min(all_marks)}, Average: {sum(all_marks) / len(all_marks)}")