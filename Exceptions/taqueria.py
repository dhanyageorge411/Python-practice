#implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0

while True:
    try :
        item = input("Item: ")
        if item.title() in menu:
            cost = float(menu[item.title()])
            total_cost=total_cost + cost                                                                                
            print (f"Total: ${ total_cost:.2f}")
        else:
            raise KeyError
     #to catch input not in the dictionary    
    except KeyError:
        pass

    #to catch the ctrl D or Ctrl Z
    except EOFError:
        break;
                     

