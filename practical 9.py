# practical 9
# Write a user-defined exception that could be raised when the text entered by user consists of less than 10 characters.

try:
    a = input("Enter your characters: ")

    if len(a) <= 10:
        raise Exception("Please Enter more than 10 characters.")

        
except Exception as d:
    print(d)

finally:
    print("Finished")
