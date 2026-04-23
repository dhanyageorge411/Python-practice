#input from user 

check = input("Greeetings: ")

#check the input case in case-insensitively

if check.casefold().startswith("hello"):
    print("$0")
elif check.casefold().startswith("h"):
    print("$20")
else:
    print("$100")