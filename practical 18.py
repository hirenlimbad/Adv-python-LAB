# practical 18
# write a program to join two given dictionary to creat new one.

dict1 = {}
dict2 = {}
dict3 = {}

n = int(input("Enter a total number of key for dictionary: "))
for j in range(n):
    a = input("Enter key and value with space for dictionary: ").split()
    dict1[a[0]] = a[1] 
    

n = int(input("Enter a total number of key for dictionary: "))
for j in range(n):
    a = input("Enter key and value with space for dictionary: ").split()
    dict2[a[0]] = a[1] 


for tt in dict1:
    for t in dict1.values():
        dict3[tt] = t
        
for tt in dict2:
    for t in dict2.values():
        dict3[tt] = t
        
dict3
