# *===========================================================================================
# PROGRAM 1: TYRON PIZZA ORDER FLOW — CLASSIC INPUT VALIDATION STYLE
# This version walks through the pizza order step by step, using standard input validation,
# conditional blocks, and user-friendly messages to compute the final price of the pizza.
# *===========================================================================================

print("Welcome to Tyron Pizza Deliveries! \n")

# Prompt the user for pizza size and validate input
size = input("What size pizza do you want? S, M or L: \n").upper()
bill = 0
while size not in ['S','M','L']:
    size = input("Please, choose among the available options S,M or L").upper()

# Set base price depending on pizza size
if size == "L":
    bill += 25
    print(f"The price for a Large pizza is ${bill}\n")
elif size == "M":
    bill += 20
    print(f"The price for a Medium pizza is ${bill}\n")
else:
    bill += 15
    print(f"The price for a Small pizza is ${bill}\n")

# Ask if user wants pepperoni and validate input
pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n").upper()
while pepperoni not in ["Y","N"]:
    pepperoni = input("Please choose a valid answer: Y or N? \n").upper()

# Add price for pepperoni based on pizza size
if pepperoni == "Y" and size=="S":
    bill += 2
    print(f"The total bill is now {bill}\n")
elif pepperoni == "Y" and size in ["M", "L"]:
    bill += 3
    print(f"The total bill is now {bill}\n")
else:
    bill += 0
    print(f"The total bill remains the same: ${bill}\n")

# Ask if user wants extra cheese and validate input
extra_cheese = input("Do you want extra cheese? Y or N: \n").upper()
while extra_cheese not in ["Y","N"]:
    extra_cheese = input("Please choose a valid answer: Y or N? \n").upper()

# Add price for extra cheese if selected
if extra_cheese == "Y":
    bill += 1
    print(f"The total bill is now ${bill}\n")
else:
    bill += 0
    print(f"The total bill remains the same: ${bill}\n")



# *===========================================================================================
# PROGRAM 2: TYRON PIZZA ORDER FLOW — EXPLORING THE WALRUS OPERATOR (:=)
# This version replicates the same logic as Program 1, but uses the walrus operator 
# to streamline variable assignment and loop conditions. It's an experiment in writing 
# more concise and expressive validation code using Python 3.8+ features.
# *===========================================================================================

print("Welcome to Tyron Pizza Deliveries!")

# Define valid options for pizza size
valid_size = ['S', 'M', 'L']

# Ask for pizza size using the walrus operator to assign and validate in one line
while (size := input("What size pizza do you want? S, M or L: \n").upper()) not in valid_size:
    print('The size you entered is not valid, please try again!')

# Set base price depending on pizza size
bill = 0
if size == "L":
    bill += 25
    print(f"The price for a Large pizza is ${bill}\n")
elif size == "M":
    bill += 20
    print(f"The price for a Medium pizza is ${bill}\n")
else:
    bill += 15
    print(f"The price for a Small pizza is ${bill}\n")

# Ask for pepperoni using walrus operator for input validation
valid_pepperoni = ["Y","N"]
while (pepperoni := input("Do you want to add pepperoni? Y or N?: \n").upper()) not in valid_pepperoni:
    print("Please choose a valid answer: Y or N? \n")

# Add pepperoni price based on pizza size
if pepperoni == "Y" and size=="S":
    bill += 2
    print(f"The total bill is now {bill}\n")
elif pepperoni == "Y" and size in ["M", "L"]:
    bill += 3
    print(f"The total bill is now {bill}\n")
else:
    bill += 0
    print(f"The total bill remains the same: ${bill}\n")

# Ask for extra cheese using walrus operator
valid_extra_cheese = ["Y","N"]
while (extra_cheese := input("Do you want to add cheese? Y or N\n").upper()) not in valid_extra_cheese:
    print("Please choose a valid answer: Y or N? \n")

# Add cheese price if selected
if extra_cheese == "Y":
    bill += 1
    print(f"The total bill is now ${bill}\n")
else:
    bill += 0
    print(f"The total bill remains the same: ${bill}\n")

