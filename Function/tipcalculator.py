#To calculate the tip to be left .
#Input from user the meal cost and precentage to tip

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percentage = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percentage
    print (f"Please leave ${tip:.2f}")

#function to convert dollar to float 

def dollars_to_float(d):
    y = float(d.lstrip('$'))
    return(y)

#function to convert the percent to float 

def percent_to_float(p):
    x =float(p.rstrip('%'))
    percent = x/100
    return(percent)

main()