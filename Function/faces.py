# To convert the emoticons to emoji 

#main function for user input and to print the result 
def main():
    name = input("")
    print(convert(name))

#function to convert the emoticons

def convert(value): 
    x =value.replace(':)','🙂').replace(':(' , '🙁')
    return(x)  

#Calling the main()

main()