# practical 11
# Write a program to carry out following tasks on a Python Tuple.

# Access items of Tuple
# Adding item in Tuple
# Changing Values in Tuple
# Removing item from Tuple
# Check If item exists in Tuple 
# Loop through a Tuple


# starts


t = input("Enter your tuple elements with space: ").split()
t = tuple(t)

# access item from tuple
j = int(input("for access item serial number of item: "))
j = j-1
print(t[j])

# add item in tuple
new = input("Enter a item for add into tuple: ")
t = list(t)
t.append(new)
t = tuple(t)
print(t)

# change value in tuple
t = list(t)
rep = input("Enter old elment with space Enter a new element").split()
for j in range(len(t)):
    if rep[0] == t[j]:
        t[j] = rep[1]   
t = tuple(t)
print(t)

# remove item from tuple
t = list(t)
rem = input("Enter item for remove from tuple: ")
t.remove(rem)
t = tuple(t)
print(t)

# check if item exist in tuple
a = input("Enter item for check available or not! : ")
if a in t:
    print("tes item is available.")
else:
    print("sorry item is not available.")
    
# loop through a tuple
print("We are printing loop through a tuple...")
for j in t:
    print(j)
