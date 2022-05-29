a = []
b = []


n = int(input("How many set element in first set?: "))
for i in range(n):
    g = input("Enter a element for set: ")
    a.append(g)


n = int(input("How many set element in second set?: "))
for i in range(n):
    g = input("Enter a element for set: ")
    b.append(g)

a = set(a)
b = set(b)

o = a.union(b)
p = a.intersection(b)
q = a.symmetric_difference(b)
r = a.isdisjoint(b)
s = a.issubset(b)3j

print("Union of sets is: ",o)
print("intersection of sets is: ",p)
print("symetric difference is: ",q)
print("disjoint is:",r)
print("subset is: ",s)
