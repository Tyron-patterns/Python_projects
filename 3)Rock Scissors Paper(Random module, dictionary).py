# *===========================================================================================
# PROGRAM 1: FIRST ATTEMPT WITH HARDCODED LOGIC AND THE RANDOM MODULE
# This version focuses on building the core gameplay logic using basic integer comparisons 
# and hardcoded rules to determine the winner. The `random` module is used to generate the 
# computer's move, and ASCII art enhances user interaction.
# *===========================================================================================


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [None, paper, scissors, rock]
game_on = True

while game_on:
    while True:
        player_pick = [1, 2, 3]
        player = ...

        # Ask for player's input and validate it
        while True:
            try:
                player = int(input("Please choose 1=paper, 2=scissors or 3=rock! "))
                if player not in player_pick:
                    print('Please choose a number from 1 to 3: ')
                    continue
                else:
                    print(f"Player chose {player}")
                    print(options[player])
                    break
            except ValueError:
                print('Please enter the correct integer!')

        # Generate computer's random choice
        computer = random.randint(1, 3)

        if computer == 1:
            print('Computer chose paper!')
            print(paper)
        elif computer == 2:
            print("Computer chose scissor")
            print(scissors)
        elif computer == 3:
            print('Computer chose rock')
            print(rock)

        # Determine result
        if computer == player:
            print("It's a tie!")
            print("Choose again!")
            continue
        elif computer == 1:
            if player == 2:
                print('Player won')
            else:
                print('Computer won!')
            break
        elif computer == 2:
            if player == 3:
                print('Player won!')
            else:
                print('Computer won!')
            break
        elif computer == 3:
            if player == 1:
                print('Player won!')
            else:
                print('Computer won!')
            break

    # Prompt to play again
    while True:
        play_again = input('Do you want to play again: Y or N?').upper()
        if play_again == 'Y':
            print("\nLet's play again!\n")
            break
        elif play_again == 'N':
            print('\nSee you next time!')
            game_on = False
            break
        else:
            print('\nPlease choose either Y or N\n')
            continue
