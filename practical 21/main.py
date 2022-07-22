# Python Practical-21 - Write a program to read the content of file line by line and write it to another 
# file except for the lines containing "a" letter in it.

fp = open("about python.txt","r")

counter = 0

while True:
    w = fp.readline().split()

    if not w:
        break
    
    for i in w:
        for j in i:
            if "a" == j:
                counter = counter + 1
    
print("a in given text file: ",counter)
fp.close()