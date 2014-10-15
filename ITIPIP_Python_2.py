# The below information was coded with Caesar Cipher to avoid it being searchable in Google.
# It can be deciphered using http://www.braingle.com/brainteasers/codes/caesar.php with letter shift 3.

# "Jxhvv wkh qxpehu"

# Plql-surmhfw 2 iurp 'Dq Lqwurgxfwlrq wr Lqwhudfwlyh Surjudpplqj lq Sbwkrq'
# frxuvh eb Ulfh Xqlyhuvlwb rq Frxuvhud: kwwsv://zzz.frxuvhud.ruj/frxuvh/lqwhudfwlyhsbwkrq
# Wkh frgh vkrxog eh hahfwxhg lq kwws://zzz.frghvnxoswru.ruj

# import libraries
import simplegui
import random
import math

# declare global variables
secret_number = None
tries_left = None
game_won = False
playing_range_1000 = False

def new_game():
    """ helper function to start and restart the game"""
    
    # starts a new game depending on the variation of the last game played
    if playing_range_1000:
        range1000()
    else:
        range100()

def range100():
    """ initialize a new game in the range 0-100"""
    
    # initialize secret_number
    global secret_number
    secret_number = random.randrange(0,101)
    
    print "Starting a game in the range 0 to 100, please enter your guess."
    
    # initialize tries_left
    global tries_left
    tries_left = 7

def range1000():
    """ initialize a new game in the range 0-1000"""
    
    # initialize secret_number
    global secret_number
    secret_number = random.randrange(0,1001)
    
    print "Starting a game in the range 0 to 1000, please enter your guess."
    
    # initialize tries_left
    global tries_left
    tries_left = 10
    
    global playing_range_1000
    playing_range_1000 = True
    
def input_guess(guess):
    """ implements the game """
    
    # prints the guess
    print "Guess was", guess
    
    # converts the guess to an int
    guess_int = int(guess)
    
    # checks if any guesses left
    global tries_left
    
    # conditional determining computer feedback
    if guess_int == secret_number:
        print "Correct"
        print "You have won!\n"
        global game_won
        game_won = True
        new_game()
    elif guess_int > secret_number:
        print "Lower\n"
    elif guess_int < secret_number:
        print "Higher\n"
    else:
        print "There was a problem with your guess, please try again"
            
    # decrements number of guesses left
    tries_left = tries_left - 1
    
    # checks for loosing condition and prints number of guesses left
    if tries_left <= 0:
        print "You have run out of guesses... The number was", secret_number, "\n"
        new_game()
        
    elif not game_won:
        print "You have", tries_left, "guesses left.\n"
   
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200)
frame.set_canvas_background('White')

# add input field and buttons to the frame
frame.add_input("Your guess", input_guess, 45)
frame.add_button("Range: 0-100", range100, 175)
frame.add_button("Range: 0-1000", range1000, 175)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
