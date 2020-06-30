from WordGenerator import word_gen

# Prompts the user for the amount of incorrect attempts they want


def select_incorrect_attempts():
    while True:

        num_attempts = input('How many incorrect attempts would you like? [1-25] ')

        # Sees if user input is an integer, prompts again if not
        try:
            num_attempts = int(num_attempts)

            # Sees if user input is within the range, prompts again if not
            if num_attempts in range(1, 26):
                return num_attempts

            else:
                print(f'{num_attempts} is not an integer within the range.')

        except:
            print(f'{num_attempts} is not a valid integer.')

# Prompts the user for the word length they want


def select_min_word_length():
    while True:
        word_length = input('What minimum word length would you like? [4-16] ')

        # Checks if user input is integer
        try:
            word_length = int(word_length)

            # Checks if integer is within range
            if word_length in range(4, 17):
                return word_length

            else:
                print(f'{word_length} is not an integer within the range.')

        except:
            print(f'{word_length} is not a valid integer.')


def letter_check(letter, word):
    if letter.lower() in word:
        print(f'{letter} is in the word!')
        return True
    else:
        print(f'{letter} is NOT in the word!')
        return False

# Returns the censored word


def word_censor(letter, word, censored_word):
    indicies = []
    cen_word = censored_word
    if cen_word is None:
        cen_word = ""
        for char in word:
            cen_word += "*"

    # Finds where the instance of the letter occurs
    for idx, char in enumerate(word):
        if letter == char:
            indicies.append(idx)

    # Converts censored word to list and replaces asterisk with letter
    cen_list = list(cen_word)
    for index in indicies:
        cen_list[index] = letter

    # Joins the list back into a string
    cen_word = "".join(cen_list)

    return cen_word


def play_hangman():
    print('Starting a game of Hangman...')
    num_attempts = select_incorrect_attempts()
    word_length = select_min_word_length()
    word = word_gen(word_length)
    cen_word = word_censor('', word, None)
    letters_used = []

    while True:
        print('')
        print(f'Word: {cen_word}')
        print(f'Attempts Remaining: {num_attempts}')
        print(f'Letters you have used: {letters_used}')
        guessed_letter = input('Guess the next letter: ')

        #Checks to see if letter was already used
        if guessed_letter in letters_used:
            print('You have already guessed that letter.')
            letter_outcome = True
        else:
            letters_used.append(guessed_letter)
            letter_outcome = letter_check(guessed_letter, word)

        #Changes the censored word if letter was in the word
        if letter_outcome:
            cen_word = word_censor(guessed_letter, word, cen_word)
        else:
            num_attempts -= 1

        #Breaks out of loop if you run out of attempts or you guessed the word
        if num_attempts == 0 or word == cen_word:
            break

    if(word != cen_word):
        print('You lose!')
    else:
        print('Congratulations, you won!')

    print(f'The word was {word}')

    while True:
        try_again = input('Would you like to play again? [Y/N] ')
        if try_again.lower() == 'y':
            play_hangman()
            print('')
        elif try_again.lower()=='n':
            break
        else:
            continue

if __name__ == '__main__':
    play_hangman()
