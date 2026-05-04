#output that same date in YYYY-MM-DD format

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

 
while True:
    try:
        date = input("Date:")
     #format : MM/DD/YYY
        if '/' in date:
         month , day , year = date.split('/')
         month = int(month)
         day = int(day)
     #format : Month DD YYY
        else :
         month_str , day , year = date.split(' ')
         month = months.index(month_str) + 1 
         day = int(day.replace(",",""))
          

    #print the output YYYY-MM-DD
        if 1 <= month <= 12 and 1 <= day <= 31:
           print(f"{year}-{month:02}-{day:02}")
           break
         
    except (ValueError, IndexError):
       pass
