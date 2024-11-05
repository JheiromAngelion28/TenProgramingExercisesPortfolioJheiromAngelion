#We ask for the first name by declaring the variable aong with the input as well is the age and the hometown.

#Because there may be a chance of the user to enter a second name or their full name, a string is used to handle multiple words.
firstname = str(input('enter your first name'))
# Fo the age we use value error in the case that they place the format in words 
try:
    age = str(input('enter your age'))
except ValueError:
    print("an error occured")
# Declaring the variable and asking the user to input teir home town.
hometown = str(input('enter your home town'))

#Declaring a dictionary 

dict = {
  "Firstname": firstname,
  "age": age,
  "hometown": hometown
}
print(f"Your First name is: {dict["Firstname"]}\n Your Age is:{dict["age"]}\n Your hometown is:{dict["hometown"]}")
#Updated with a dictionary 
