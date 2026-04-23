#input from the user 

expresion = input("Expresion: ")

#split the input into 3 variables 

x,y,z = expresion.split(' ')

#calculate the result according to the expresion 

if y == "+" :
   result = int(x) + int(z)
   print(float(result))
elif y == "-":
   result = int(x) - int(z)
   print(float(result))
elif y == "*":
   result = int(x) * int(z)
   print(float(result))
elif y == "/":
   result = int(x) / int(z)
   print(float(result))
else:
   print("Invalid")
