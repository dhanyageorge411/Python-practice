#input from the user 

file = input("Name of the file: ")

#To extract the file extension from input

extension = file.split('.')[-1].strip().casefold()

#condition to check the output 

if extension == 'gif':
    print("image/gif")
elif extension == 'jpg' or extension == 'jpeg':
    print ("image/jpeg")
elif extension == 'png':
    print("image/png")
elif extension == 'pdf':
    print("application/pdf")
elif extension == 'txt':
    print("text/plain")
elif extension == 'zip':
    print("application/zip")
else:
    print("application/octet-stream")