# write a program that finds maximum and minimum numbers from a given list.

a = int(input('Enter a number of list element: '))


b = []
for c in range(a):
	f = int(input('Enter number for list: '))
	b.append(f)

mini,high = min(b),max(b)
print('minimum value in list is: ',mini)
print('maximum value in list is: ',high)