# Input numbers from users 

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

#Compare using if 

if x<y :
    print("First number is less than second")
elif x>y:
    print("First is greater than second")  
else:
    print("First is equal to second")    

# compare using or

if x<y or x>y:
    print("Not equal")
else:
    print("Equal")

# To check even or odd 
# Using % operator 

if x % 2 ==0:
     print("The first number is even")
else:
    print("The first number is odd")

