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
    rulesFile = open("Rules.txt", "r")
    print(rulesFile.read())
    rulesFile.close()
    input('\nPress Enter to continue... ')
    print('\n' + ('*' * 60) + '\n')


# function tests input type
def getChoice(v, message):
    while True:
        try:
            choice = v(input(message))                       
            return choice

        except ValueError:
            pass
        
        print('Invalid entry!\n')


# function builds the game table display
def buildTable(cups):
    cupList = [0] * cups

    for i in range(0, len(cupList)):
        cupList[i] = ('[ ' + str(i + 1) + ' ]')

    # Table surface: Nine symbols per cup
    table = '\n' + ('\t'.join(cupList)) + '\n' + ('=' * (8 * cups)) + '\n'
    return table


# function displays the current amount in the bank and asks for bet
def betOrQuit(bank):
    print('\nYou have $' + str(bank))
    message = 'How much would you like to bet? '
    bet = getChoice(float, message)

    while bank - bet < 0:
        print('\nYou can''t bet more than you have!')
        bet = getChoice(float, message)

    return bet


# function displays stone location, user's choice, and empty cups
def revealCups(cups, stone, choice):
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

    result = '\n' + ('\t'.join(cupList)) + '\n' + ('=' * (8 * cups)) + '\n'
    return result


# function determines if user chose the correct cup
def isWinner(stone, choice):
    if stone == choice - 1:
        return True
    else:
        return False


# function calculates bank after win
def bankWin(bank, bet, cups):
    bank += (bet * cups)
    return bank


# function calculates bank after incorrect guess
def bankLose(bank, bet):
    bank -= bet
    return bank


# main
def main():
    bank = 100.00

    # Program displays rules of the game.
    welcomeBanner()
    rules()

    keepPlaying = 'y'

    while keepPlaying.lower() == 'y':

        # User chooses number of cups.
        message = 'How many cups would you like? '
        cups = getChoice(int, message)

        # Choose a random cup to hold the stone
        stone = random.randint(0, cups - 1)

        # Display the table with cups hidden and labeled
        table = buildTable(cups)
        print(table)

        # Get user bet amount
        bet = betOrQuit(bank)

        # Get user cup choice
        message = 'Choose a cup number: '
        choice = getChoice(int, message)

        # Verify cup choice is in established range.
        while choice not in range(1, cups + 1):
            message = 'Cup doesn''t exist! Choose a cup number: '
            choice = getChoice(int, message)

        # Reveal location of stone
        result = revealCups(cups, stone, choice)
        print(result)

        # Apply results
        winner = isWinner(stone, choice)

        if winner:
            print('\nWINNER!!!\nYou win $' + str(bet * cups))
            bank = bankWin(bank, bet, cups)

        else:
            print('\nToo bad. Stone was under cup #' + str(stone + 1))
            bank = bankLose(bank, bet)

        if bank <= 0:
            print('\n' + ('x-x' * 20) + '\n')
            input('Out of money! Press Enter to exit. ')
            exit()

        print('\nYou have $' + str(bank))

        # Continue or quit
        message = '-' * 30 + '\n\n[Y] Play again\n[R] View Rules\n[Other] Quit\nYour choice: '
        keepPlaying = getChoice(str, message)

        while keepPlaying.lower() == 'r':
            rules()
            message = 'Keep playing? Y/N '
            keepPlaying = getChoice(str, message)

    input('Thanks for playing! Press Enter to exit.')
    exit()


if __name__ == '__main__':
    main()
