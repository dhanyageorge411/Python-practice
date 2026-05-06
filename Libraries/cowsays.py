#to install packages : pip install cowsay 

import cowsay 
import sys 

if len(sys.argv) == 2:
    #can only pass one string
    cowsay.cow("Hello ," + sys.argv[1])
    #to print t-rex 
    cowsay.trex("Hello ," + sys.argv[1])


