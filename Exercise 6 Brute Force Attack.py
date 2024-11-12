# Exercise 6 

#Ceclaring a Variable for the password attemps
Password = 12282006

attempts = 0
max= 5

# Using while function to only allow 5 attempts
while attempts < max:
    #Using If else Statements along with inputs, we are able to make the password attempt only 5 times
    if Password == input('Enter your password. The limit of attempts is 5. '):
        print('correct password! Accese granted')
    else: 
        attempts += 1
        if attempts == max:
            print("You have reach the limit of 5 attempts")
        else:
            print(f'The ammount of attempts is {attempts}')
       