#to call the library created 


import sys 
#calling the library from mylibrary file 
from mylibrary import hello 

if len(sys.argv) == 2:
    hello(sys.argv[1])