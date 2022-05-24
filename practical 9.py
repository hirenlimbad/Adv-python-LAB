try:
    a = input("Enter your characters: ")
    l = len(a)

    if l <= 10:
        raise Exception("Please Enter more than 10 digit.") 



except Exception as d:
    print(d)
