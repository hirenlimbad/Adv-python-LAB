# practical 14
def cube(n):
    b = 1
    t = []
    for j in range(1,n+1):
        b = j*j*j
        t.append(b)
        
    t = tuple(t)
    return t

n = int(input("Enter a number for find cube of 1 to your number: "))
ans = cube(n)
print("one to",n,"cube tuple is:",ans)
