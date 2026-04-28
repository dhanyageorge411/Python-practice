#users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit

#dict to store fruits and calories 

fruits = {
    "apple" : "130" ,
    "avocado" :  "50" ,
    "sweet cherries" : "100" ,
    "banana" : "110",
}

#input from user 

name = input("Item :")

if name.lower() in fruits :
        print("Calories:", fruits[name.lower()])