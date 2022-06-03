# practical 15
# Write a program to input names of n employees and store them in a tuple Also
# input a name from the user and find if this employee is present in the tuple or not.

n = int(input("Enter a number of employee: "))
t = ()
for j in range(n):
    name = input("Enter a employee name: ")
    
    t = list(t)
    t.append(name)
    t = tuple(t)
    
print("Employee names in python tuple: ",t)

name = input("Enter name of employee to check name available or not! : ")

if name in t:
    print("Yes its available...")
    
else:
    print("No its not available...")
