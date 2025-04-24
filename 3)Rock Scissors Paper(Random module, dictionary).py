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

        # Ask for player's input and validate it
        while True:
            
            try: ## Handle invalid (non-integer) input using try/except to prevent crashes
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


# *===========================================================================================
# PROGRAM 2: CLEANER, INDEX-BASED VERSION USING DICTIONARIES FOR LABELING
# This version improves clarity and structure by mapping player and computer moves to names 
# using dictionaries. It avoids string comparison logic and relies on indexed control flow 
# for clean, efficient gameplay logic. ASCII art is still used for output.
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

options = [paper, scissors, rock]
options1 = {0: 'paper', 1: 'scissors', 2: 'rock'}
game_on = True

while game_on:
    
    while True:
        # Ask for player's input and validate it
        while True:
            
            try: # Handle invalid (non-integer) input using try/except to prevent crashes
                choice = int(input("Please choose 1=paper, 2=scissors or 3=rock! \n"))
                if choice not in [1, 2, 3]:
                    print('Please choose a number from 1 to 3: \n')
                    continue
                player = choice - 1
                print(f"Player chose {options1[player]}")
                print(options[player])
                break
            except ValueError:
                print('Please enter the correct integer!')

        # Generate computer's choice
        computer = random.randint(0, 2)
        print(f"Computer chose {options1[computer]}")
        print(options[computer])

        # Determine result using player vs computer index values
        if player == computer:
            print("It's a tie! Please choose again! \n")
            continue
        elif (player == 0 and computer == 2) or \
             (player == 1 and computer == 0) or \
             (player == 2 and computer == 1):
            print("Player wins!")
            break
        else:
            print("Computer wins!")
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


# *===========================================================================================
# PROGRAM 3: USER-FRIENDLY, STRING-BASED VERSION FOR BETTER READABILITY
# This version allows the player to type the full name of their choice (e.g., "rock"), 
# making the game more intuitive. It uses a single dictionary to store both names and 
# ASCII visuals, and all game logic is handled through string comparison.
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

# Single dictionary: name → ASCII art
choices = {
    'paper': paper,
    'scissors': scissors,
    'rock': rock
}

game_on = True

while game_on:
    
    while True:
        # Player input
        player_choice = input("Please choose paper, scissors or rock! \n").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose: paper, scissors, or rock.\n")
            continue

        print(f"\nPlayer chose {player_choice}:")
        print(choices[player_choice])

        # Computer random choice
        computer_choice = random.choice(list(choices.keys()))
        print(f"\nComputer chose {computer_choice}:")
        print(choices[computer_choice])

        # Determine result using string comparison
        if player_choice == computer_choice:
            print("\nIt's a tie! Please choose again!\n")
            continue
        elif (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'rock' and computer_choice == 'scissors'):
            print("\nPlayer wins!\n")
            break
        else:
            print("\nComputer wins!\n")
            break

    # Replay prompt
    while True:
        
        play_again = input("Do you want to play again? Y or N: ").upper()
        if play_again == 'Y':
            print("\nLet's play again!\n")
            break
        elif play_again == 'N':
            print("\nSee you next time!\n")
            game_on = False
            break
        else:
            print("Please enter Y or N.\n")

