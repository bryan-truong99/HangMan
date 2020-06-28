#Prompts the user for the amount of incorrect attempts they want
def incorrect_attempts():
    num_attempts = input('How many incorrect attempts would you like? [1-25]')

    if num_attempts in range (1,25):
        continue

    else:
        print(f'{num_attempts} is not a valid integer')


if __name__ == '__main__':
    print('Starting a game of Hangman...')
    incorrect_attempts()
