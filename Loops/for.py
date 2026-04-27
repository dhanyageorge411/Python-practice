for i in range(3):  #for _ in range(3): can use _ instead of i 
    print ("hi")

print("hello\n" *3 , end = "")

#input from user to how many times output should be printed 

#to check if the input is a positive value 

while True:
    n = int(input("The number of times: "))
    if n > 0:
        break

# to print the output 

for i in range(n):
    print("Welcome")