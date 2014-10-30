# The below information was coded with Caesar Cipher to prevent it from being searchable in Google.
# It can be deciphered using http://www.braingle.com/brainteasers/codes/caesar.php with a letter shift 3.

# lpsohphqwdwlrq ri fdug jdph - Phprub

# Plql-surmhfw 4 iurp 'Dq Lqwurgxfwlrq wr Lqwhudfwlyh Surjudpplqj lq Sbwkrq'
# frxuvh eb Ulfh Xqlyhuvlwb rq Frxuvhud: kwwsv://zzz.frxuvhud.ruj/frxuvh/lqwhudfwlyhsbwkrq
# Wkh frgh vkrxog eh hahfxwhg lq kwws://zzz.frghvnxoswru.ruj

import simplegui
import random

# constants and globals
AV_CARDS = list(range(9)) + list(range(9))
CARD_WIDTH = 50
FRAME_WIDTH = len(AV_CARDS) * CARD_WIDTH
deck = AV_CARDS
game_state = 0
turns = 0
matches = 0
last_two = [None] * 4
exposed = []

# helper function to reset the exposed cards and reshuffle deck
def reshuffle():
    global deck, exposed
    for index, card in enumerate(deck):
        if len(exposed) < len(AV_CARDS):  
            exposed.append(False)
        else:
            exposed[index] = False
    random.shuffle(deck)
        
# helper function to initialize globals
def new_game():
    global game_state, turns, matches
    game_state = 0
    turns = 0
    reshuffle()
    matches = 0

# define event handlers
def mouseclick(pos):
    global game_state, turns, matches
    # determinate which card was clicked by deducting x coordinate of the click from the sum 
    # of the frame with and card width and then reversing by deducting it from the number of cards.
    index = int(len(AV_CARDS) - (FRAME_WIDTH + CARD_WIDTH - pos[0]) / CARD_WIDTH)
    clicked_card = deck[index]
    
    if matches < 9:
        # if stat is 0 expose 1st card and store it in last_two
        if game_state == 0:
            exposed[index] = True
            last_two[0] = clicked_card
            last_two[2] = index
            game_state = 1
        # if state is 1 expose 2nd card and store it in last_two
        elif game_state == 1:
            exposed[index] = True
            last_two[1] = clicked_card
            last_two[3] = index
            game_state = 2
            turns += 1
        elif game_state == 2:     
            # if state is 2 and cards don't match expose the new card and hide the two previous ones
            if last_two[0] != last_two[1]:
                exposed[index] = True
                exposed[last_two[2]] = False
                exposed[last_two[3]] = False
                last_two[0] = clicked_card
                last_two[2] = index
            # elif clicked on the same card twice, continue
            elif last_two[2] == last_two[3]:
                exposed[index] = True
            # else the last two cards match so keep them exposed and store the newly clicked card in last_two
            else:
                exposed[index] = True
                last_two[0] = clicked_card
                last_two[2] = index
                matches +=1
            game_state = 1
            
                     
# cards are logically 50x100 pixels in size    
def draw(canvas):
    # update the labels 
    label.set_text("Turns: " + str(turns))
    label_matches.set_text("Matches: " + str(matches))
    
    # iterate over deck and if the card is to be exposed draw its value on a different background.
    for index, card in enumerate(deck):
        if exposed[index] == True:     
            canvas.draw_polygon([[(index * CARD_WIDTH), 0], [(index * CARD_WIDTH), 100], [(index * CARD_WIDTH) + CARD_WIDTH, 100], [(index * CARD_WIDTH) + CARD_WIDTH, 0]], 1, 'Black', 'Silver') #[(top-left),(bottom-left),(bottom-right),(top-right)]
            canvas.draw_text(str(card), ((index * CARD_WIDTH) + 10, 70), 52, "White", "sans-serif")
        else:
            canvas.draw_line(((index * CARD_WIDTH) + CARD_WIDTH, 0), ((index * 50) + 50, 100), 2, "Black")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", FRAME_WIDTH, 100)
frame.set_canvas_background('Green')
frame.add_button("Reset", new_game)
label = frame.add_label("Turns: 0")
label_matches = frame.add_label("Matches: 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric