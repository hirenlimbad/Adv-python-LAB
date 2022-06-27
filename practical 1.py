# Write a program which excepts a string from user count number of vowel and consonants from given string.

a = input('Enter any line to find number of vowel and consonents: ')
b = a.lower()
db = ["a","e","i","o","u"]

vowel = 0
conso = 0

for new in b:
	if new in db:
		vowel = vowel + 1
	else:
		conso = conso+1

print('vowel in line ',a,'is','is',vowel)
print('consonents in line ',a,'is','is',conso)