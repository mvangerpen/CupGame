# Program gives user a choice of three cups. User bets to find the stone under one cup.

import random


# function displays welcome banner
def welcomeBanner():
    print('*' * 60 + '\n')
    print('*' * 60)
    print('\n\tWELCOME TO CUPS\n\tA fantastic game by Mark VanGerpen\n')
    print('*' * 60 + '\n')


# function displays rules and clears the screen
def rules():
    print('*' * 60 + '\n')
    rulesFile = open("Rules.txt","r")
    print(rulesFile.read())
    rulesFile.close()
    input('\nPress Enter to continue... ')
    print('\n' + ('*' * 60) + '\n')


# function builds and displays the game table
def buildTable(cups):

    cupList = [0] * cups

    for i in range(0,len(cupList)):
        cupList[i] = ('[ ' + str(i+1) + ' ]')

    # Table surface: Nine symbols per cup
    print('\t'.join(cupList))
    print('=' * (8 * cups))

# function displays the current amount in the bank and asks for bet
def betOrQuit(bank):
    print('\nYou have $' + str(bank))
    bet = float(input('How much would you like to bet? '))

    while bank - bet < 0:
        print('\nYou can''t bet more than you have!')
        bet = float(input('How much would you like to bet? '))

    return bet


def revealCups(cups,stone,choice):
    cupEmpty = '[   ]'
    cupStone = '[ o ]'
    cupChoice = '[ X ]'
    cupWin = '[WIN!!]'

    # Build list of cups
    cupList = ['[   ]'] * cups

    # insert WIN cup
    if stone == choice - 1:
        cupList[stone] = cupWin
    else:
        # insert stone and choice cups
        cupList[stone] = cupStone
        cupList[choice - 1] = cupChoice

    print('\n')
    print('\t'.join(cupList))
    print('=' * (8 * cups))


def main():

    multiplier = int
    bank = 100.00

    # Program displays rules of the game.
    welcomeBanner()
    rules()

    keepPlaying = 'y'

    while keepPlaying.lower() == 'y':

        # User chooses number of cups.
        cups = int(input('How many cups would you like? '))
        print()

        # Choose a random cup to hold the stone
        stone = random.randint(0,cups-1)

        # Display the table with cups hidden and labeled
        buildTable(cups)

        # Get user bet amount
        bet = betOrQuit(bank)

        # Get user cup choice
        choice = int(input('Choose a cup number: '))
        while choice not in range(1,cups+1):
            choice = int(input('Cup doesn''t exist! Choose a cup number: '))


        # Reveal location of stone
        revealCups(cups,stone,choice)

        # Apply results
        if stone == choice - 1:
            print('WINNER!!!\nYou win $' + str(bet * cups))
            bank += (bet * cups)
        else:
            print('Too bad. Stone was under cup #' + str(stone + 1))
            bank -= bet

        if bank <= 0:
            print('\n' + ('x-x' * 20) + '\n')
            input('Out of money! Press Enter to exit. ')
            exit()

        print('\nYou have $' + str(bank))


        keepPlaying = input('-' * 30 + '\n\n[Y] Play again\n[R] View Rules\n[Other] Quit\nYour choice: ')

        while keepPlaying.lower() == 'r':
            rules()
            keepPlaying = input('Keep playing? Y/N ')

    input('Thanks for playing! Press Enter to exit.')
    exit()


main()