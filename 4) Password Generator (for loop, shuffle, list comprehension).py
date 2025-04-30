# *===========================================================================================
# PROGRAM 1: PY PASSWORD GENERATOR — HARDCODED STRUCTURE WITH FOR LOOP, SHUFFLE, AND STRING
# This version uses a hardcoded approach to build the password.
# It starts with an empty string, appends random choices using for-loops,
# then converts the string into a list to shuffle and randomize character positions.
# *===========================================================================================

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password = ''

for i in range(nr_letters):
    password += random.choice(letters)

for i in range(nr_symbols):
    password += random.choice(symbols)

for i in range(nr_numbers):
    password += random.choice(numbers)

password_list = list(password)
random.shuffle(password_list)
print('Your password is ' + ''.join(password_list))



# *===========================================================================================
# PROGRAM 2: PY PASSWORD GENERATOR — USING EMPTY LIST AND FOR LOOPS
# This version uses an empty list to collect characters.
# It replaces the string concatenation from version 1 and directly builds the list for shuffling.
# A bit cleaner and avoids unnecessary type conversion.
# *===========================================================================================

password = []

for i in range(nr_letters):
    password.append(random.choice(letters))

for i in range(nr_symbols):
    password.append(random.choice(symbols))

for i in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print('Your password is ' + ''.join(password))


# *===========================================================================================
# PROGRAM 3: PY PASSWORD GENERATOR — SHORTENED WITH LIST COMPREHENSIONS
# This version introduces list comprehensions to reduce the amount of lines.
# Separate lists are created for each character type, then combined and shuffled.
# *===========================================================================================

password = [random.choice(letters) for i in range(nr_letters)]
password2 = [random.choice(numbers) for i in range(nr_numbers)]
password3 = [random.choice(symbols) for i in range(nr_symbols)]

final_password = password + password2 + password3
random.shuffle(final_password)
print('Your password is: ' + ''.join(final_password))



# *===========================================================================================
# PROGRAM 4: PY PASSWORD GENERATOR — COMPACT ONE-LINERS WITH NESTED COMPREHENSIONS
# This is the most concise version, combining all character selections into a single expression.
# It demonstrates maximum compactness while still achieving the same result.
# *===========================================================================================

password = (
    [random.choice(letters) for i in range(nr_letters)] +
    [random.choice(numbers) for i in range(nr_numbers)] +
    [random.choice(symbols) for i in range(nr_symbols)]
)
random.shuffle(password)
print('Your password is: ' + ''.join(password))
