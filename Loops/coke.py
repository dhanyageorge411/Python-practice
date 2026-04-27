#a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents

#Assiging the cost of coke 

amount_due = 50

while True: 
    print("Amount Due:" , amount_due)
    coin = int(input("Insert coin:"))

#to check if the inserted coin in 25,10 or 5    
    if coin == 25 or coin == 10 or coin ==5:     
        amount_due = amount_due - coin
        if amount_due <= 0:
        # abs = absolute value to convert to +ve number 
            change = abs(amount_due)
            print("Change Owned:",change)
            break;

    