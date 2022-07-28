# Write a program to concatenate the following dictionaries to create a new one.
# Sample Dictionary: dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict1 = {}
dict2 = {}
dict3 = {}


def inputs(dictionary):
    n = int(input("Enter a total number of key for dictionary: "))
    for j in range(n):
        a = input("Enter key and value with space for dictionary: ").split()
        dictionary[a[0]] = a[1] 

def its(maindict,finaldict):
    for t in maindict:
        finaldict[t] = maindict[t]


inputs(dict1)
inputs(dict2)  

its(dict1,dict3)
its(dict2,dict3)
       
print("Your final dictionary is: ",dict3)
