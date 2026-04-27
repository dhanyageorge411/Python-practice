#prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time

def main():
  time = input("What time is it ")
  value = convert(time)
  meal(value)

#To convert the 24 format time into float value

def convert(time):
   hours, minutes = map(int, time.split(':'))
   time_converted = hours + minutes/60
   return(time_converted)

#to check and return the output 

def meal(value):
   if 7.0 <= value <= 8.0:
      print("Breakfast time")
   elif 12.0 <= value <= 13.0:
      print("Lunch time")
   elif 18.0 <= value <= 19.0:
       print("Dinner time")
   

if __name__ == "__main__":
    main()