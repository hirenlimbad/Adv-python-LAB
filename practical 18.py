dict1 = {}
dict2 = {}
dict3 = {}

def inputs(dictionary):
    n = int(input("Enter a total number of key for dictionary: "))
    for j in range(n):
        a = input("Enter key and value with space for dictionary: ").split()
        dictionary[a[0]] = a[1] 

inputs(dict1)
inputs(dict2)    


def loops(maindict,finaldict):
    for tt in maindict:
        for t in maindict.values():
            finaldict[tt] = t
            
loops(dict1,dict3)
loops(dict2,dict3)
        
print(dict3)
