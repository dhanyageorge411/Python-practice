# main function for users input and to display the output 

def main():
    x = int(input("Enter the number: "))
    if is_even(x):
        print("The number is even ")
    else:
        print("The numer is odd ")

#function to check if its even and return the value

def is_even(n):
    if n % 2 == 0:
        return True #Boolian expression 
    else:
        return False  
    # return True if n % 2 ==0 else False
    # return n % 2 == 0

#calling the main fucntion

main()

