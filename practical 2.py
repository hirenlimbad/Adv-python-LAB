# Write a program that creates a dynamic list of numbers,calculate sum of all the list element of list.

a = int(input('Enter a number of list element: '))


b = []
for c in range(a):
	f = int(input('Enter number for list: '))
	b.append(f)

t = 0 
for new in b:
	t = t + new

print('a sum of list element is ',t)