#to generate a library that can be reused in other programs 

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello,{name}")

def goodbye(name):
    print(f"Goodbye, {name}")

#shouldnot call main without condition as it will be laoded in the library it has been called
# __name__ automatically sets to name of the file 

if __name__ == "__main__":
    main()


#the name of the file this library is called is mylibrarytest

    