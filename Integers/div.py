#input from users 
# Decimal and interger values 

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

#Division and rounding the result to 2 digits

z= round (x/y ,2)

#To format the output with commas 

print(f"Adding both:{z:,}") 