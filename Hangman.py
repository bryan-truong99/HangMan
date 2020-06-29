from WordGenerator import word_gen

# Prompts the user for the amount of incorrect attempts they want
def select_incorrect_attempts():
    while True:

        num_attempts=input('How many incorrect \
        attempts would you like? [1-25] ')

        # Sees if user input is an integer, prompts again if not
        try:
            num_attempts = int(num_attempts)

            # Sees if user input is within the range, prompts again if not
            if num_attempts in range(1, 26):
                return num_attempts

            else:
                print(f'{num_attempts} is not an integer within the range')

        except:
            print(f'{num_attempts} is not a valid integer')

# Prompts the user for the word length they want


def select_min_word_length():
    while True:
        word_length = input('What minimum word length would you like? [1-16] ')

        # Checks if user input is integer
        try:
            word_length = int(word_length)

            # Checks if integer is within range
            if word_length in range(1, 17):
                return word_length

            else:
                print(f'{word_length} is not an integer within the range')

        except:
            print(f'{word_length} is not a valid integer')

def letter_check(letter,word):
    if letter.lower() in word:
        print(f'{letter} is in the word!')
        return True
    else:
        print(f'{letter} is NOT in the word!')
        return False


def play_hangman():
    print('Starting a game of Hangman...')
    num_attempts = select_incorrect_attempts()
    word_length = select_min_word_length()
    word = word_gen(word_length)

    while True:
        print(f'Word: {PUT_WORD_ASTERISKS_HERE}')
        print(f'Attempts Remaining: {num_attempts}')
        guessed_letter=input('Guess the next letter: ')
        letter_outcome=letter_check(guessed_letter,word)

        if letter_outcome:
            x = 1
        else:
            continue

        num_attempts -= 1



if __name__ == '__main__':
    print('Starting a game of Hangman...')
