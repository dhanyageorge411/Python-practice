# implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
#the requirements are:All vanity plates must start with at least two letters.vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.No periods, spaces, or punctuation marks are allowed.”

import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#function to check if all the requirenments are met

def is_valid(s):
    if start_letter(s) and lenght_string(s) and is_number(s) and  special_char(s):
        return True 

# funtion to check if starts with at least 2 letters 

def start_letter(s):
    if len(s) < 2 :
        return False
    elif not s[0].isalpha() or not s[1].isalpha() :
        return False
    else :
        return True

# to check if the input contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def lenght_string(s):
    if len(s) < 2 or len(s) > 6 :
        return False
    else :
        return True

# to check if the number at the end and not in the middle of the input.     
#  The first number used cannot be a ‘0’

def is_number(s):
    number_part = ""
    letter_part = ""
    for i in s :
        if i.isdigit():
            number_part += i
        else :
            if number_part:
                return False
                break
            letter_part += i
    else :
        if number_part.startswith("0") and number_part != "" :
            return False
        else :
            return True


    return True

# to check if the input has any periods, spaces, or punctuation marks.

def special_char(s):
    for i in s: 
        if i in string.punctuation or i.isspace():
            return False
    else :
        return True


main()