#the value typed by the user  in the command prompt is passed to the program as list 

import sys

if len(sys.argv) < 2:
    print("too few arguments")

#to print more value from input and slice the file name from the output 
for avg in sys.argv[1:]:
    print("Hello, my name is " ,avg)

#the value typed is passed as a list 
#try:
#    print("Hello, my name is " , sys.argv[1])
#except IndexError:
#    print("too few arguments")

