#input from user 


value = input("What is the anwer to Great Question of Life, the Universe and Everything: ").strip()
if value == '42' or value.casefold() == 'forty-two' or value.casefold() == 'forty two':
    print("Yes")
else:
    print("no")

    