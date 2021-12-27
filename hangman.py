import random
import os

hangman_art = ['''
 +---+
     |
     |
     |
     |
    ===''',
 '''
 +---+
 o   |
     |
     |
     |
    ===''',
 '''
 +---+
 o   |
 |   |
     |
     |
    ===''',
'''
 +---+
 o   |
 |   |
 |   |
     |
    ===''',
'''
 +---+
 o   |
/|   |
 |   |
     |
    ===''',
'''
 +---+
 o   |
/|\  |
 |   |
     |
    ===''',
'''
 +---+
 o   |
/|\  |
 |   |
/    |
    ===''',
'''
 +---+
 o   |
/|\  |
 |   |
/ \  |
    ===''']

       
def get_rand_word():
    words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
    game_word = random.randint(0, len(words) - 1)
    game(words[game_word])

def input_word():
    os.system('cls')
    game_word = input('Player 2, what is the word you want to provide? \n > ')
    game(game_word.lower())

def game(game_word):
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    guesses = []
    count = 0
    blank_word = '_'* len(game_word)
    
    
    
    #(len(hangman_art))  --- this is 8. So they get 8 wrong guesses. 
    while count < (len(hangman_art)):
        os.system('cls')
        guess = input(hangman_art[count] +'\n\n'+ blank_word +'\n\nYou have guessed: {} \nWhat is your current guess?\n> '.format(guesses))
        if guess not in letters:
            notlower = guess.lower()
            guess = notlower
        if guess in guesses:
            print("you have already guessed {}".format(guess))
            count += 1
        elif guess not in guesses:
            if guess in game_word:
                print('\nThat was a good guess!')
                guesses.append(guess)
                for i in range(len(game_word)):
                    if game_word[i] in guesses:
                        blank_word = blank_word[:i] + game_word[i] + blank_word[i+1:]
                if '_' not in blank_word:
                    print('Congrats on winning!')
                    play_again()
            elif guess not in game_word:
                print('\nI am sorry, that is not in secret word.')
                guesses.append(guess)
                count += 1
            else:
                print('What the fuck did you do?!')
                end()
    if count >= (len(hangman_art)):
        print('I am sorry. You have lost. Maybe you should suck less')
        play_again()
 
     
    play_again()

    
    
def end():
    os.system('cls')
    print('This is an error screen loser')

    
    
    
def play_again():
    again = input('Would you like to play again?(y/n) \n>')
    os.system('cls')
    yes = ['y', 'yes', 'ye', 'es']
    no = ['n', 'no']
    if again.lower() in yes:
        print('Awesome! Lets get your game set up!')
        number_of_players()
    if again.lower() in no:
        print('Thanks for playing! Have a good day!')
    
    
def main():
    print('Hello! Welcome to Hangman!\n')
    number_of_players()

def number_of_players():
    player_num = input('Is this a one or two player game?\n> ')
    os.system('cls')
    def confirm_game(player_num):
        yes = ['y', 'yes', 'ye', 'es']
        no = ['n', 'no']
        conf = input('Are your sure you want to play a {} player game? (y/n)\n> '.format(player_num))
        os.system('cls')
        if conf.lower() in list(yes):
            print(player_num)
            if player_num == '1' or player_num.lower() == 'one':
                get_rand_word()
            elif player_num == '2' or player_num.lower() == 'two':
                input_word()
        elif conf.lower()in no:
            print('Ok, let\'s start over.\n')
            os.system('cls')
            number_of_players()
        else:
            print('Pleae make a valid selection.\n')
            number_of_players()

    
    if player_num == '1' or player_num.lower() == 'one':
        confirm_game(player_num)
    elif player_num == '2' or player_num.lower() == 'two':
        confirm_game(player_num)
    else:
        player_num = input('Please make a valid selection. \n>')
        number_of_players()
        


    
    
    
 
main() 



#Ideas for Hangman
#1. Ask for how many players, 1 or 2.
#2. If two, accept input for word
#3. If one, provide a random word I need to provide a list 