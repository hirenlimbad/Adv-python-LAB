# practical 8
# write a program to catch divide by zero exeception also use finally block.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))

    devide = a/b
    print(a,"devide by",b,"=",devide)


except ZeroDivisionError:
    print("A numbe cannot devide by Zero")

finally:
    print("finished")
