# practical 8

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))

    devide = a/b
    print(a,"devide by",b,"=",devide)


except ZeroDivisionError:
    print("A numbe cannot devide by Zero")

finally:
    print("finished")
