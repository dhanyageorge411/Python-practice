#to generate random codes

#flip a coin

#imports all the function from random so need to use random.choice 
import random

#flip a coin

coin = random.choice(["head" , "tail"])
print(coin)

#from random import choice 
#coin = choice(["head" , "tail"])
#print(coin)

#to generate a random integer 

random_integer = random.randint(1,10)
print(random_integer)

#to shuffle 

cards = ["king","queen","jack"]
random.shuffle(cards)
#to print the output one item/line
for i in cards:
    print(i)