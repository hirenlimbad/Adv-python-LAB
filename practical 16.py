# practical 16

# Python Practical-16 Create a dictionary with the roll number, name, and marks of n students in a class and 
# display the names of students who have scored marks above 75.

dict1 = {}
n = int(input("Enter total number of students: "))
b = []
for j in range(1,n+1):
    tt = []
    name = input("Enter name of student: ")
    mark = float(input("Enter marks of student: "))
    tt.append(name)
    tt.append(mark)
    dict1[j] = tt
    
for i in dict1:
    
    if dict1[i][1] >= 75:
        print(dict1[i][0])
