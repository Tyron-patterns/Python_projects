
print('Welcome to the blind auction!')
name_amount = {}


def winning_bid(bidding_dict):
    max_bet=0
    winner = ""

    for key in name_amount:
        if max_bet < bidding_dict[key]:
            max_bet = bidding_dict[key]
            winner = key
    print(f'The winner is {winner} with a bid of ${name_amount[winner]}')

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
            winning_bid(name_amount)
            game_on = False
            break
        else:
            print('Please type Y or N')
            continue


print('Welcome to the blind auction!')
name_amount = {}
def winning_bid(bidding_dict):
    winner = max(bidding_dict,key = bidding_dict.get)

print(f'The winner is {winner} with a bid of ${name_amount[winner]}')


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
            winning_bid(name_amount)
            game_on = False
            break
        else:
            print('Please type Y or N')

# Now determine the winner (outside the input loop!)

