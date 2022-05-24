# practical 10

try:
    n = int(input("Enter a number of number: "))
    s = []

    for j in  range(n):
        a = int(input("Enter a number for sum: "))
        s.append(a)

    print(sum(s))
except ValueError:
    print("Please enter valid number.")
