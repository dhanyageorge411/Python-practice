#To square the input 

#user input 

def main():
    x = int(input("Enter the number to be squared: "))
    print("The squared number is :", square(x))

# square the input 

def square(x):
    return pow(x,2)  #return x*x

#calling the function 

main()
