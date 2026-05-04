#program that prompts the user for items, one per line, until the user inputs control-d . Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item

#for the dictionary

grocery_list = {}


while True:
    try:

        key = input("").upper()
        
        if key.upper() in grocery_list :
           grocery_list[key] +=1
        else:
            grocery_list[key] = 1 

    except EOFError:
        break

#to print sorted output
for i in sorted(grocery_list):
    print (grocery_list[i],i)