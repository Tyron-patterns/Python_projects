print('Welcome to the blind auction!')
name_amount = {}

game_on = True
while game_on:
    name = input('Please insert the bidder name? ').upper()
    amount = int(input(f'{name}, what is your bet? '))
    name_amount[name]=amount
    more_bid = True

    while more_bid:
        other_bidders = input('Are there other bidders? (Y or N)').upper()
        print("\n" * 100)
        if other_bidders == 'Y':
            more_bid = False
            break
        elif other_bidders == 'N':
            game_on = False
            break
        else:
            print('Please type Y or N')
            continue

def winning_bid(name_amount):
    max_bet=0
    winner = ''

    for key in name_amount:
        if max_bet < name_amount[key]:
            max_bet = name_amount[key]
            winner = key
print(f'The winner is {winner} with a bid of ${name_amount[winner]}')



print('Welcome to the blind auction!')
name_amount = {}

game_on = True

# Collect all bidders
while game_on:
    name = input('Please insert the bidder name? ')
    amount = int(input(f'{name}, what is your bet? '))
    name_amount[name] = amount

    while True:
        other_bidders = input('Are there other bidders? (Y or N): ').upper()
        print("\n"*100)
        if other_bidders == 'Y':
            break  # continue outer loop
        elif other_bidders == 'N':
            game_on = False
            break
        else:
            print('Please type Y or N')

# Now determine the winner (outside the input loop!)
winner = max(name_amount,key = name_amount.get)

print(f'The winner is {winner} with a bid of ${name_amount[winner]}')
