
#Prompts the user for the amount of incorrect attempts they want
def incorrect_attempts():
    while True:
        num_attempts =
        input('How many incorrect attempts would you like? [1-25]')

        try:
            num_attempts = int(num_attempts)

            if num_attempts in range (1,26):
                return num_attempts

            else:
                print(f'{num_attempts} is not a valid integer')
                num_attempts=
                input('How many incorrect attempts would you like? [1-25]')

        except:
                print(f'{num_attempts} is not a valid integer')


if __name__ == '__main__':
    print('Starting a game of Hangman...')
    incorrect_attempts()
