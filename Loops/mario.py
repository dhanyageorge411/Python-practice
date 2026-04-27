#To ceate the game textually using hashes for bricks 
#create the bricks using #

def main():
    print_col(3)
    print_row(4)
    print_square(3)

#to print vertically

def print_col(height):
    for i in range(height):
        print("#")

#to print horizontally

def print_row(width):
    print("?" * width)

#to print square H * W

def print_square(size):
# for each row in square  
    for i in range(size):
# for each line in row 
        for j in range(size):
            print("#", end = "")
        print()

main()
