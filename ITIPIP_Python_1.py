# The below information was coded with Caesar Cipher to avoid it being searchable in Google.
# It can be deciphered using http://www.braingle.com/brainteasers/codes/caesar.php with a letter shift 3.

# Urfn-sdshu-vflvvruv-olcdug-Vsrfn jdph

# Plql-surmhfw 1 iurp 'Dq Lqwurgxfwlrq wr Lqwhudfwlyh Surjudpplqj lq Sbwkrq'
# frxuvh eb Ulfh Xqlyhuvlwb rq Frxuvhud: kwwsv://zzz.frxuvhud.ruj/frxuvh/lqwhudfwlyhsbwkrq
# Wkh frgh vkrxog eh hahfwxhg lq kwws://zzz.frghvnxoswru.ruj

# Wkh nhb lghd ri wklv surjudp lv wr htxdwh wkh vwulqjv
# "urfn", "sdshu", "vflvvruv", "olcdug", "Vsrfn" wr qxpehuv
# dv iroorzv:
#
# 0 - urfn
# 1 - Vsrfn
# 2 - sdshu
# 3 - olcdug
# 4 - vflvvruv


# imports random library
import random

def name_to_number(name):
    """
    Convert name to a correspondent number value
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Incorrect name input"
    
def number_to_name(number):
    """
    Convert number value to a correspondent choice name
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Incorrect number (out of range 0-4)"

def rpsls(player_choice):
    """
    Implements the game of Rock-paper-scissors-lizard-Spock
    """
    # print a blank line to separate consecutive games
    print " "

    # print out the message for the player's choice
    print "Player chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice

    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if result == 0:
        print "It's a tie!"
    elif result <= 2:
        print "Computer wins!"
    elif result > 2:
        print "Player wins!"
    else:
        print "Error while trying to evaluate winner"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

