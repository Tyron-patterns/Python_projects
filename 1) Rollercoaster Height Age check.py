

# *======================================================================================================================================================
# This script checks whether a person meets the height and age requirements for a rollercoaster ride. It uses two while loops to validate user input,
# and nested if/else statements to determine eligibility and pricing.
# NOTE: range(0,100) and .isdigit() (this one having clear limitations in the cope of the desired results) are redundant used in combination
# but intentionally used together to demonstrate multiple validation techniques.
# NOTE: creating a function in this case could have probably been the best option for multiple reasons (e.g. it would have allowed the use of "return"),
# but, again, the purpose was to experiment with the code (e.g. using exit())
#======================================================================================================================================================*

#import numpy as np
print("")
print("WELCOME TO MY ROLLERCOASTER HEIGHT AND AGE VALIDATION!")
print("")
#acceptable_height = np.arange(0,250,0.1)
#height = int(input("What is your height in cm? "))
#acceptable_height = range(0,251)  #only for integers

height = -1
# Prompt user to enter a valid height between 0 and 250 cm

while not (0 <= height <= 250): #restarts the procedure of asking for the height. Loop until height is valid
    try: #prompts the user to input the correct value. Try converting to float
        height = float(input("What is your height in cm? \n"))
        print("")

        if 0 <= height <= 250: #checks if the height from the input is in the correct range -> exit
            break
        else: #number out of bount -> continue
            print("Please, select a value between 0 and 250")
            print("")
            continue

    except ValueError: #not a number -> restart the whil -> try again
        print("Please, insert a valid number between 0 and 250!")

# If the height is acceptable, ask for age
if height >= 120:

    acceptable_age = range(0,100)
    print("Please, declare your age!")

    while True: #restarts the procedure of asking for the age

        age_input = input("Insert a number between 0 and 99! \n")
        print("")
        if age_input.isdigit(): #checks if the user inserted an integer value
            age = int(age_input)

            if age not in acceptable_age:
                print("Please,")
                continue
            else:
                break
    price = 0
     if age in range(18,76) and 45 <= age <= 55: #condition for different ages
        price = 0
        print(f"The ticket for people between the age of 45 and 55 is free! Enjoy the ride!")
        print("")
    elif age in range(18,76):
        price +=12
        print(f"The price of the ticket is {price}$! Enjoy the ride!")
    elif 12 <= age < 18:
        price = 7
        print(f"The price of the ticket is {price}$! Enjoy the ride!")
    elif age >= 76:
        print("Unfortunately you are too old to ride!")
        exit()
    else:
        print("Unfortunately you are too young to ride!")
        exit()

    print("")
    print("Do you want a photo?")
    wants_photo = ""
    #prompts the user for a photo and updates the price
    while not (wants_photo == 'Y' or wants_photo == 'N'): #forces the user to input the right value
   #while wants_photo != 'Y' and wants_photo != 'N': alternative version
        wants_photo = input("Please, type Y or N ").upper()

    if wants_photo == 'Y':
        price_photo = 3
        price += 3
      # total_price = price
        print("")
        print(f"The cost of the photo is {price_photo}$, and the total price will be \n{price}$") #{total_price}
    else:
        print("")
        print(f"No problem! The total price remains \n{price}$")

else:
    print("Unfortunately you must be at least 120 cm to ride!")


# *===========================================================================================
# FUNCTION 2: ROLLERCOASTER ENTRY VALIDATION — LINEAR VERSION (NO EARLY EXITS)
# This version refactors the ride eligibility logic into a linear, nested structure.
# It avoids using `exit()` and keeps the flow within condition blocks until the end.
# *===========================================================================================

print("")
print("WELCOME TO MY ROLLERCOASTER HEIGHT AND AGE VALIDATION!")
print("")

height = -1
# Prompt user to enter a valid height between 0 and 250 cm
while not (0 <= height <= 250): #restarts the procedure of asking for the height
    try: #prompts the user to input the correct value
        height = float(input("What is your height in cm? \n"))
        print("")

        if 0 <= height <= 250: #checks if the height from the input is in the correct range
            break
        else:
            print("Please, select a value between 0 and 250")
            print("")
            continue

    except ValueError:
        print("Please, insert a valid number between 0 and 250!")

# If the height is acceptable, ask for age
if height >= 120:

    acceptable_age = range(0,100)
    print("Please, declare your age!")

    while True: #restarts the procedure of asking for the age

        age_input = input("Insert a number between 0 and 99! \n")
        print("")
        if age_input.isdigit(): #checks if the user inserted an integer value
            age = int(age_input)

            if age not in acceptable_age:
                print("Please,")
                continue
            else:
                break
    price = 0
    if age in range(12,76): #checks if the height from the input is in the correct range
        if age < 18:
            price = 7
            print(f"The price of the ticket is {price}$! Enjoy the ride!")
            print("")
        elif age in range(45,56):
            price = 0
            print(f"The ticket for people between the age of 45 and 55 is free! Enjoy the ride!")
        else:
            price = 12
            print(f"The price of the ticket is {price}$! Enjoy the ride!")

        print("")
        print("Do you want a photo?")
        wants_photo = ""
        # prompts the user for a photo and updates the price
        while not (wants_photo == 'Y' or wants_photo == 'N'):  # forces the user to input the right value
            # while wants_photo != 'Y' and wants_photo != 'N': alternative version
            print("")
            wants_photo = input("Please, type Y or N ").upper()

        if wants_photo == 'Y':
            price_photo = 3
            total_price = price + price_photo
            print("")
            print(f"The cost of the photo is {price_photo}$, and the total price will be \n{total_price}$")
        else:
            print("")
            print(f"No problem! The total price remains \n{price}$")
    elif age >= 76:
        print("Unfortunately you are too old to ride!Don't break an ankle, you old fart!")
    else:
        print("Unfortunately you are too young to ride! Come back in a few years, Bitch")

else:
    print("Unfortunately you must be at least 120 cm to ride! You fucking midget")
