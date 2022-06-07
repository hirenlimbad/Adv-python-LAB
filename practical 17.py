# Write a program to count the number of a character appears in a given string using dictionary.
''' for example 
dict1 = {1:"one" ,
            2:"two" ,
            3:three}
            
# sample input "e"
# sample output : 1
                  0
                  2

'''



# starts
dict1 = {}
for j in range(0,11):
    b = input("Enter a string: ")
    dict1[j] = b
print(dict1)

t = input("Enter your one character: ")
for j in dict1.values():
    s = 0
    
    for q in j:
        if t in q:
            s = s+1
    
    print(s,"time ",t,"in",j)
