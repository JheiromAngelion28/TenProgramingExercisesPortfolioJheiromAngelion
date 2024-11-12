# Exercise 6 Brute forse attack
# Declaring a variable of the password.
# Declaring the attempts and the maximum number of attempts.
Password = 12282006

attempts = 0
max= 5

# Using the while loop fuction as long as the number of attempts is less than 5.
#Using if else statements.
while attempts < max:
    if Password == input('Enter your password. The limit of attempts is 5. '):
        print('correct password! Accese granted')
    else: 
        attempts += 1
        if attempts == max:
            print("You have reach the limit of 5 attempts")
        else:
            print(f'The ammount of attempts is {attempts}')
       