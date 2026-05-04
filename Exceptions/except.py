#To try and create exception 

try:
    name = int(input("Enter the value: "))
    print("Output: " ,name)

#To catch if the value of the variable is incorrect 
except ValueError:
    print("Value not an integer")

#including min lines under try

try: 
     name = int(input("Enter the integer:"))
except ValueError:
    print("Value not an integer")
else:
    print("Output: " ,name)

#loop and pass 

while True:
    try: 
     name = int(input("Enter the integer:"))
    except ValueError:
        pass
else:
    print("Output: " ,name)