# Write a program to carry out following tasks on a Python Dictionary.
# Access items of Dictionary
# Adding item in Dictionary
# Changing Values in Dictionary
# Removing item from Dictionary
# Check If item exists in Dictionary
# Loop through a Dictionary/

dict1 = {}
n = int(input("Enter a total number of key for dictionary: "))
for j in range(n):
    a = input("Enter key and value with space for dictionary: ").split()
    dict1[a[0]] = a[1] 
    
print("Dictionary added success fully...")

# Access items of Dictionary
j = input("Search word in dictionary...")
b = dict1[j]
print("your word is",b)

# Adding item in dictionary
j = input("Enter key and value with space for add in dictionary: ").split()
dict1[j[0]] = j[1]
print(dict1)

# Changing Values in Dictionary
j = input("Enter key and value for change that value with space: ").split()
dict1[j[0]] = j[1] 
print(dict1)


# Check If item exists in Dictionary
a = input("Enter your item for check in dictionary: ")

if a in dict1:
    print("Yess, possible.")
    
else:
    print("Not exists in dictionary.")
    
# Loop through a Dictionary
print("OK we are printing dictionary keys...")
for j in dict1:
    print(dict1[j])
    
# Removing item from Dictionary
dict1.clear()
print("This is cleared dictionary: ",dict1)
