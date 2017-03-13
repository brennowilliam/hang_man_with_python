import random
import os
import sys


#Get the words from the /usr/share/dict/words from a UNIX file system.
#Note: It will not work in a Windows env, neither I have the desire to make it work there ;).
file = open('/usr/share/dict/words')
words = [line[:-1] for line in file]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#--------------------------------
def draw(bad_guesses, good_guesses, secret_word):
    clear() 

    print('Strikes: {}/7 '.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter),
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print('\033[4m{}\033[0m'.format(letter)),
        else:
            print('_ '),
    	    
#--------------------------------
def get_guess(bad_guesses, good_guesses):
    while True:
        guess = str(raw_input('Guess a letter: ').lower())

        if len(guess) != 1:
            print('You can only enter a letter each time')
        elif guess in bad_guesses or guess in good_guesses:
            print('You have already guessed that letter!')
        elif not guess.isalpha():
            print('You can only enter letters!')
        else:
            return guess
#---------------------------------
def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
   
    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print('You win!')
                print('The secret words was {}'.format(secret_word))
 		done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
  		print('You lost!')
		print("The secret word was {}".format(secret_word))
                done = True
        
        if done:
            play_again = raw_input('PLay again? Y/n	').lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()

#-----------------------------------
def welcome():
    start = str(raw_input('Press enter/return to start or Q to quit: ').lower())


if __name__ == '__main__':
    done = False

    while True:
        clear()
        welcome()
        play(done)	    

