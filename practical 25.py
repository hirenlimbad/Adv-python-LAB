# practical 25.py
# write a program to create binary file to store Roll no and name, search any Roll no and display name if roll no no found
# otherwise display a message 'rollno nor found. '

import pickle
n = int(input('how many students you have...'))
dict1 = {}
for j in range(1,n+1):

	l1 = input('Enter student name: ')

	dict1[j] = l1

fp = open('student.txt','wb')
pickle.dump(dict1,fp)
fp.close()

fp = open('student.txt','rb')
dict2 = pickle.load(fp)
fp.close()
try:
	search = int(input('Search roll number: '))
	print(search,dict2[search])
except KeyError:
	print('No roll number found...')
