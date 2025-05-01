# *===========================================================================================
# PROGRAM 1: LOVE SCORE CALCULATOR — HARDCODED VERSION
# This initial version uses a fixed logic where the words "true" and "love" are hardcoded.
# It loops through each character in both names and counts matches for both keywords separately.
# The score is formed by concatenating the counts of letters from "true" and "love".
# *===========================================================================================

def calculate_love_score(name1, name2):
    count_true = 0
    count_love = 0

    for x in name1.lower():
        if x in 'true':
            count_true += 1
        if x in 'love':
            count_love += 1

    for x in name2.lower():
        if x in 'true':
            count_true += 1
        if x in 'love':
            count_love += 1

    print(count_true)
    print(count_love)
    print(f'Your love score is {count_true}{count_love}')

calculate_love_score('Tyron', 'Eline')




# *===========================================================================================
# PROGRAM 2: LOVE SCORE CALCULATOR — PARAMETERIZED VERSION FOR FLEXIBILITY
# This version introduces flexibility by making "true" and "love" configurable via parameters.
# It also includes a 'type_of_score' label to customize the output message.
# Characters from both input names are merged and evaluated dynamically against the two words.
# *===========================================================================================

def calculate_love_score(name1, name2, type_of_score, word1, word2):
    count_true = 0
    count_love = 0
    combined_names = name1 + name2

    for x in combined_names.lower():
        if x in word1:
            count_true += 1
        if x in word2:
            count_love += 1

    print(count_true)
    print(count_love)
    print(f'Your {type_of_score} is {count_true}{count_love}')

calculate_love_score('Tyron', 'Eline', 'type_of_score', 'true', 'love')



# *===========================================================================================
# PROGRAM 3: LOVE SCORE CALCULATOR — OPTIMIZED VERSION WITH COUNT AND COMPREHENSION
# This version simplifies the logic by using Python's built-in count() method.
# It merges both names and converts them to lowercase once, then calculates the total matches
# using generator expressions for each keyword.
# Cleaner, more efficient, and still dynamic for other scoring words.
# *===========================================================================================

def calculate_love_score(name1, name2, word1, word2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    first_digit = sum(lower_names.count(x) for x in word1)
    second_digit = sum(lower_names.count(x) for x in word2)

    print(f"Your love score is {first_digit}{second_digit}")

calculate_love_score('Tyron', 'Eline', 'true', 'love')
