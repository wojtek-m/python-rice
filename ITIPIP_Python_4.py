# The below information was coded with Caesar Cipher to prevent it from being searchable in Google.
# It can be deciphered using http://www.braingle.com/brainteasers/codes/caesar.php with a letter shift 3.

# Lpsohphqwdwlrq ri fodvvlf dufdgh jdph Srqj
# Plql-surmhfw 4 iurp 'Dq Lqwurgxfwlrq wr Lqwhudfwlyh Surjudpplqj lq Sbwkrq'
# frxuvh eb Ulfh Xqlyhuvlwb rq Frxuvhud: kwwsv://zzz.frxuvhud.ruj/frxuvh/lqwhudfwlyhsbwkrq
# Wkh frgh vkrxog eh hahfwxhg lq kwws://zzz.frghvnxoswru.ruj

import simplegui
import random

# CONSTANTS
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
PAD_VEL = 10
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
BALL_RESET_POS = [WIDTH / 2, HEIGHT / 2]
START_DIRECTION = ['LEFT', 'RIGHT']

# global variables
ball_pos = BALL_RESET_POS 
ball_vel = [0,0]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

def spawn_ball(direction):
    # initialize ball
    global ball_pos, ball_vel 
    
    ball_pos[0] = WIDTH / 2
    ball_pos[1] = HEIGHT / 2
    
    if direction == 'RIGHT':
        ball_vel = [random.randrange(2, 4), -random.randrange(1, 3)]
    elif direction == 'LEFT':
        ball_vel = [-random.randrange(2, 4), random.randrange(1, 3)]
        
def update_ball_pos(ball_pos, ball_vel): 
    # updating the position of the ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
           
def move_ball(ball_pos, ball_vel): 
    # handling the ball move and bouncing
    global score1, score2
    # bounce of the top and bottom 
    if ball_pos[1] < 0 + BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        update_ball_pos(ball_pos, ball_vel)   
    # check if reached left side
    elif ball_pos[0] + ball_vel[0] < 0 + PAD_WIDTH + BALL_RADIUS:  
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] and paddle1_pos + HALF_PAD_HEIGHT >= ball_pos[1]:
            # handle cases when the ball is hit from sides or behind
            if ball_pos[0] < PAD_WIDTH + BALL_RADIUS - 10:
                score2 += 1
                spawn_ball("RIGHT")
            else:
                # bounce of the left paddle and increase the speed
                ball_vel[0] = 1.1 * -ball_vel[0]
                update_ball_pos(ball_pos, ball_vel)
        else:
            # resetting the ball with some delay by letting the ball go off canvas
            if ball_pos[0] + ball_vel[0] < PAD_WIDTH - 5 * BALL_RADIUS:
                score2 += 1
                spawn_ball("RIGHT")
            else:
                update_ball_pos(ball_pos, ball_vel) 
    # check if reached right side
    elif ball_pos[0] + ball_vel[0] > WIDTH - PAD_WIDTH - BALL_RADIUS: 
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] and paddle2_pos + HALF_PAD_HEIGHT >= ball_pos[1]:
            # handle cases when the ball is hit from sides or behind
            if ball_pos[0]  > WIDTH - PAD_WIDTH - BALL_RADIUS + 10:
                score1 += 1
                spawn_ball("LEFT")
            else:
                # bounce of the right paddle and increase the speed
                ball_vel[0] = 1.1 * -ball_vel[0]
                update_ball_pos(ball_pos, ball_vel)
        else:
            # resetting the ball with some delay by letting the ball go off canvas
            if ball_pos[0] + ball_vel[0] > WIDTH - PAD_WIDTH + 5 * BALL_RADIUS:
                score1 += 1
                spawn_ball("LEFT")
            else:
                update_ball_pos(ball_pos, ball_vel)   
    else:
        update_ball_pos(ball_pos, ball_vel)


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2 
    
    # reset all parameters
    ball_pos = BALL_RESET_POS 
    ball_vel = [0,0]
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
    # start with a random ball direction
    spawn_ball(START_DIRECTION[random.randrange(0,2)])

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
  
    # update ball
    move_ball(ball_pos, ball_vel)
    
    # draw ball
    ball = canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'White', 'White')
  
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel > HALF_PAD_HEIGHT - PAD_VEL and paddle1_pos + paddle1_vel < HEIGHT + PAD_VEL - HALF_PAD_HEIGHT:
        paddle1_pos = paddle1_pos + paddle1_vel # left paddle
    
    if paddle2_pos + paddle2_vel > HALF_PAD_HEIGHT - PAD_VEL and paddle2_pos + paddle2_vel < HEIGHT + PAD_VEL - HALF_PAD_HEIGHT:
        paddle2_pos = paddle2_pos + paddle2_vel # right paddle

    # draw paddles   #[(top-left),(bottom-left),(bottom-right),(top-right)] 
    paddle1 = canvas.draw_polygon([[0, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos - HALF_PAD_HEIGHT],
               [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT]], 1, "White", "White") #### left paddle     
    paddle2 = canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],
               [WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 1, "White", "White") #### right paddle

    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2 - WIDTH / 5 - 32, HEIGHT / 4), 64, 'White', 'sans-serif') #### left score
    canvas.draw_text(str(score2), (WIDTH / 2 + WIDTH / 5, HEIGHT / 4), 64, 'White', 'sans-serif')   #### right score
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = PAD_VEL   
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = PAD_VEL
      
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -PAD_VEL  
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -PAD_VEL

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 145)


# start frame
new_game()
frame.start()
