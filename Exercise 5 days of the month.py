#Exercise 5 
#Making the Dictionary For the Months ff theyear
dyear = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

# Asking the user to input the numbers of the month. Using nested If else statements to tell if the Feb has 28 or 29 days
dmonth = int(input("Please enter the number of the month: "))
if 1 <= dmonth <= 12:
    if dmonth == 2:
        leap_year = (input("Is the year considered a leap year? yes/no: ")).lower()
        if leap_year == "yes":
            print("The Month of February has 29 days")
        else:
            print("The month Of February has 28 days")
    else:
        print(f"This month has {dyear[dmonth]} days~!")

else:
    print(f"invalid number")