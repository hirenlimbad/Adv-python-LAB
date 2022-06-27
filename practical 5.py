# Write a program to carryout following task on a python set


a = {'apple','pine-apple','guava','kiwi'}

# access item of set
for new in a:
	print(new)

# adding item in set.
c = input('Enter your item to add into set: ')
a.add(c)
print(c)

# add another set items in set
b = {}
a = a.union(b)
print(a)

# remove item from set
a.remove('apple')
print(a)

# clear set
a.clear()
print(a)

# delete set
del a
print(a)

# error are normal