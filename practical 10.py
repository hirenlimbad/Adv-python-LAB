# practical 10
# Write a program to calculate the sum of elements within a list.Catch all necessarry exceptions.

try:
    n = int(input("Enter a number of element of list: "))
    s = []

    for j in  range(n):
        a = int(input("Enter a number for sum : "))
        s.append(a)

    print(sum(s))
except ValueError:
    print("Please enter valid number.")
