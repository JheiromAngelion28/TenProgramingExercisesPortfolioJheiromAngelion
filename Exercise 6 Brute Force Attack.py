Password = 12282006

attempts = 0
max= 5
while attempts < max:
    if Password == input('Enter your password'):
        print('correct password! Accese granted')
    else: 
        attempts += 1
        if attempts == max:
            print("You have reach the limit of 5 attepmts")
       
       
       