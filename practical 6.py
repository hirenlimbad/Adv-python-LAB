a = {"java-script","python","c++"}
b = {"HTML","css","php","java-script"}
 
o = a.union(b)
p = a.intersection(b)
q = a.symmetric_difference(b)
r = a.isdisjoint(b)
s = a.issubset(b)


print(o)
print(p)
print(q)
print(r)
print(s)