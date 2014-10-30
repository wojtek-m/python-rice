# The below information was coded with Caesar Cipher to prevent it from being searchable in Google.
# It can be deciphered using http://www.braingle.com/brainteasers/codes/caesar.php with a letter shift 3.

# Lpsohphqwdwlrq ri Eodfnmdfn

# Plql-surmhfw 6 iurp 'Dq Lqwurgxfwlrq wr Lqwhudfwlyh Surjudpplqj lq Sbwkrq'
# frxuvh eb Ulfh Xqlyhuvlwb rq Frxuvhud: kwwsv://zzz.frxuvhud.ruj/frxuvh/lqwhudfwlyhsbwkrq
# Wkh frgh vkrxog eh hahfwxhg lq kwws://zzz.frghvnxoswru.ruj


import simplegui
import random

# load 1664x1024 card deck and card back source: http://www.nexusmods.com/newvegas/mods/35896/?
card_images = simplegui.load_image("https://dl.dropbox.com/s/k1tal7hey1l0af2/fallout_deck-f.jpg")
CARD_SIZE = (72, 143)
CARD_CENTER = (36, 71.5)
card_back = simplegui.load_image("https://dl.dropbox.com/s/w25vy38cfdesdc6/fallout_deck-b.jpg")
CARD_BACK_SIZE = (72, 143)
CARD_BACK_CENTER = (36, 71.5)

# load background image, source: "Fallout: New Vegas" http://fallout.bethsoft.com
background = simplegui.load_image("https://dl.dropbox.com/s/zb4d07nec23berp/fallout_bg_1.jpg")

# load sounds, source: https://www.freesound.org/
lost_hand = simplegui.load_sound("https://dl.dropbox.com/s/tm3mbl30aau3ctz/113988__kastenfrosch__verloren.mp3")
won_hand = simplegui.load_sound("https://dl.dropbox.com/s/oofxih8swdxzmb1/162192__monotraum__coins.mp3")
casino_ambiance = simplegui.load_sound("https://dl.dropbox.com/s/6sd6lpkfe1uz0ds/118855__joedeshon__casino-ambiance-03.mp3")
casino_ambiance.set_volume(0.4)

# initialize some useful global variables
in_play = False
rules_needed = False
outcome = ""
prompt = ""
score = 2000
playing_deck = None
player_hand = None
dealer_hand = None
CANVAS_SIZE = 600

# define globals for cards
SUITS = ('C', 'D', 'H', 'S')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

RULES = ["1. Aces may be counted as 1 or 11 points. J, Q and K count as 10 points", 
         "2. The value of a hand is the sum of the point values of the individual cards." ,    
         "3. The player whos hand value go over 21 points busts and looses.",
         "4. If no one busts, the higher value hand wins.",
         "5. Dealer wins all the draws.",
         "6. Result of any hand can be overturn by the member of the Omerta family.",
         "7. You can take one more card by Hitting or go to showdown by Standing.",
         "8. You start with 2000 chips. Each round you win 85 or loose 100 chips.",
         "9. If your chip count is negative it means you are in debt to the Omertas...",
         "10. Never get in debt to the Omertas!"]


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def draw_back(self, canvas, pos):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_BACK_SIZE)
    
# define hand class
class Hand:
    def __init__(self):
        self.hand = []  # create Hand object

    def __str__(self):
        # return a string representation of a hand
        hand_str = "hand contains "
        for hand in self.hand:
            hand_str = hand_str + str(hand) + " "
        return hand_str

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)  
   
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        hand_with_A = False
        
        # sum the cards and set the A flag to true
        for card in self.hand:
            hand_value = hand_value + VALUES[card.rank]
            if card.rank == 'A':
                hand_with_A = True
        
        # if hand withouth an A, return its value, else add 10 or keep the 1, depending on the hand value        
        if not hand_with_A:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else: 
                return hand_value
   
    def draw(self, canvas, pos, player):
        # draw a hand on the canvas, use the draw method for cards
        x_offset = 0
        index = 0
        # if drawing dealer's hand while in play hide one card
        if player == 'dealer' and in_play:
            for card in self.hand:
                if index == 0:
                    card.draw_back(canvas, (pos[0] + x_offset, pos[1]))
                    x_offset += (CARD_SIZE[0] * 1.05)
                    index += 1
                else:
                    card.draw(canvas, (pos[0] + x_offset, pos[1]))
                    x_offset += (CARD_SIZE[0] * 1.05)
                    index += 1
        # else draw all cards face up            
        else:
            for card in self.hand:   
                card.draw(canvas, (pos[0] + x_offset, pos[1]))
                x_offset += (CARD_SIZE[0] * 1.05)
         
# define deck class 
class Deck:
    def __init__(self):
    # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
    # shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
    # deal a card from the deck
        card_to_deal = self.deck.pop(len(self.deck) - 1)
        return card_to_deal
    
    def __str__(self):
    # return a string representing the deck
        deck_str = "Deck contains "
        for card in self.deck:
            deck_str += str(card) + " "
        return deck_str

# define event handlers for buttons
def deal():
    global outcome, in_play, score, rules_needed, playing_deck, player_hand, dealer_hand, lost_hand, won_hand
    
    # play the baground sound file
    casino_ambiance.rewind()
    casino_ambiance.play()
    
    # if the deal button is clicked during the hand player loosed the hand
    if in_play and not rules_needed:
        outcome = "You have forfeited your hand."
        lost_hand.rewind()
        lost_hand.play()
        score -= 100
        in_play = False
    else:
        outcome = " "
    
    rules_needed = False
    in_play = True
    
    playing_deck = Deck() # create a deck
    player_hand = Hand() # create a hand
    dealer_hand = Hand() # create a hand
    playing_deck.shuffle() # shuffle the deck
    
    # deal the first 4 cards
    rounds_dealt = 0
    while rounds_dealt < 2:
        player_hand.add_card(playing_deck.deal_card())
        dealer_hand.add_card(playing_deck.deal_card())
        rounds_dealt += 1

def hit():
    global in_play, outcome, score, playing_deck, player_hand, lost_hand, won_hand
    
    if in_play:
        new_card = playing_deck.deal_card()
        # if players hand value is over 21, player busts
        if player_hand.get_value() + VALUES[new_card.rank] > 21:
            player_hand.add_card(new_card)
            lost_hand.rewind()
            lost_hand.play()
            outcome = "You have busted, dealer wins."
            in_play = False
            score -= 100
        # else add the new card to the hand
        else:
            player_hand.add_card(new_card)
            outcome = "New card dealt"
            
def stand():
    global in_play, outcome, score, playing_deck, player_hand, lost_hand, won_hand
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(playing_deck.deal_card())
    
        # if dealers hand value is over 21, dealer busts
        if dealer_hand.get_value() > 21:
            won_hand.rewind()
            won_hand.play()
            score += 85
            outcome = "Dealer have busted, you win!"
            
        else:
            # if dealers hand is equal or higher in value than players hand, dealer wins
            if dealer_hand.get_value() >= player_hand.get_value():
                lost_hand.rewind()
                lost_hand.play()
                score -= 100
                outcome = "Dealer wins."
            # else player wins    
            else:
                won_hand.rewind()
                won_hand.play()
                score += 85
                outcome = "You win!"
        in_play = False
            
def rules():
    # handler for the game rules button
    global rules_needed
    rules_needed = True

# draw handler    
def draw(canvas):
    
    # rules screen
    if rules_needed:
        # top label for rules
        canvas.draw_text("Gomorrah Blackjack Rules", (CANVAS_SIZE / 8, CANVAS_SIZE / 8), 36, 'Silver')
        
        # iterate over the rules and draw them in a list form
        y_offset = 125
        for rule in RULES:
            canvas.draw_text(rule, (25, y_offset ), 18, 'Silver')
            y_offset += 28  
    # game screen
    else:
        # draw background
        canvas.draw_image(background, (800 / 2, 716 / 2), (800, 716), (CANVAS_SIZE / 2, CANVAS_SIZE / 2), (CANVAS_SIZE, CANVAS_SIZE))
        
        # top label
        canvas.draw_text("Gomorrah Blackjack", (CANVAS_SIZE / 8, CANVAS_SIZE / 8), 56, 'Silver')
    
        # scoring
        canvas.draw_text("Chips: " + str(score), (CANVAS_SIZE / 1.55, CANVAS_SIZE / 4.2), 36, 'Silver')
        
        # dealer's hand
        canvas.draw_text("Dealer's hand: ", (CANVAS_SIZE / 8, CANVAS_SIZE / 4.2), 28, 'Silver')
        dealer_hand.draw(canvas, [CANVAS_SIZE / 8, CANVAS_SIZE / 3.75], 'dealer')
    
        # player's hand
        canvas.draw_text("Player's hand: ", (CANVAS_SIZE / 8, CANVAS_SIZE / 1.75), 28, 'Silver')
        player_hand.draw(canvas, [CANVAS_SIZE / 8, CANVAS_SIZE / 1.67], 'player')
    
        # outcome text
        canvas.draw_text(outcome, (CANVAS_SIZE / 8, CANVAS_SIZE / 1.12), 36, 'Silver')
    
        # user action prompts text
        if not in_play:
            canvas.draw_text("Another round?", (CANVAS_SIZE / 8, CANVAS_SIZE / 1.05), 24, 'Silver')
        else:
            canvas.draw_text("Hit or Stand?", (CANVAS_SIZE / 8, CANVAS_SIZE / 1.05), 24, 'Silver')
        

# initialization frame
frame = simplegui.create_frame("Blackjack", CANVAS_SIZE, CANVAS_SIZE)

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Rules", rules, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric