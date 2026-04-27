#input from user

def main():
    number = get_number()
    out(number)

#to check if the entered number is positive 

def get_number():
    while True:
        n = int(input("enter the value: "))
        if n > 0 :
              break
    return n

#to print the output 
def out(o):
     for i in range(o):
          print("Welcome")

main()

