# Create a package named DemoPackage which contains two modules named mathematics and greets. The mathematics module contains sum, average, power functions, and the greets module contains the sayHello function.
# a) import the module from a package to another program.
# b) import a specific function from a module.
# from  Demopackage import greets as d

d.sayhello()
d.sayhelloto("Hiren")


from  Demopackage import mathematics as b
print('\nfor find two sum...')
a = int(input('Enter your first number: '))
t = int(input('Enter your second number: '))
sum3 = b.sum1(a,t)
print('Your answer is: ',sum3)

print('\nfor find average...')
n = int(input('how many number you have to find average: '))
l1 = []
for j in range(n):
	element = int(input('enter a number: '))
	l1.append(element)

avv = b.avg1(l1)
print('average is: ',avv)

print('\nfor find power of any number...')
n = int(input("Enter your number: "))
power = int(input('Enter power of your number: '))
power3 = b.power(n,power)
print(n,'power',power,'answer is: ',power3)
