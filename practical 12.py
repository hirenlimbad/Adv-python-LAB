# practical 12
# Write a program to input 'n' number from the user and store this numbers in tuple print maximum and minimum number from this tuple. 


n = int(input("Enter number of element of tuple: "))
t = []   
for j in range(n):
    g = input("Enter your element: ")
    t.append(g)
      
tuple(t)
print("maximum number of tuple is",max(t))
print("maximum number of tuple is",min(t))
