#practical 23
#Write a program that takes input from a text file. The program should print all of the unique words in the file in alphabetical order.
fp = open('data.txt','w')
a = input('Enter your data for text file: ')
fp.write(a)
fp.close()


fp1 = open('data.txt','r')
n = 1
l1 = []
while True:
	line = fp1.readline().split()

	if not line:
		break

	for j in line:
		l1.append(j)
fp1.close()

l1 = set(l1)
l1 = list(l1)
l1.sort()

	
print('Below printed every word in alphabetical order...')
for b in l1:
	print(b)
