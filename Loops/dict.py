#to print the name corresponding to houses 

students = { 
    "david" : "red" ,
    "ram" : "blue",
    "sara" :"green" ,
    "tina" :"red"}

print(students["david"]) #prints the color corresponding to david
print("\nFor loop statment")

for student in students :
   # print(student) #prints the key
    print( students[student]) #prints the color correspoding to the names

#when more details are provided . Include grade as well.

print("\n Adding Grade")

#create a list and then create a dictionary inside it 

students = [
    {"name": "david" , "house" : "red" , "grade" : "A"},
    {"name": "ram" , "house" : "blue" , "grade" : "B"},
    {"name": "sara" , "house" : "green" , "grade" : "A"},
    {"name": "tina" , "house" : "red" , "grade" : "c"},

]

for student in students:
    print(student["name"], student["house"] , student["grade"], sep=',')
