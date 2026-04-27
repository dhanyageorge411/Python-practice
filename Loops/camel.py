#To replace the input from user with captial letter to underscore 
# Input from user 

name = input("Enter the camel case: ")
result = ""

for i in name :
    if i.isupper():
        result = result + "_"
        result = result+i.lower()
    else:
        result = result + i
print("Snake case : " , result)