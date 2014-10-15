# The below information was coded with Caesar Cipher to avoid it being searchable in Google.
# It can be deciphered using http://www.braingle.com/brainteasers/codes/caesar.php with a letter shift 3.

# "Vwrszdwfk: Wkh Jdph"

# Plql-surmhfw 3 iurp 'Dq Lqwurgxfwlrq wr Lqwhudfwlyh Surjudpplqj lq Sbwkrq'
# frxuvh eb Ulfh Xqlyhuvlwb rq Frxuvhud: kwwsv://zzz.frxuvhud.ruj/frxuvh/lqwhudfwlyhsbwkrq
# Wkh frgh vkrxog eh hahfwxhg lq kwws://zzz.frghvnxoswru.ruj

# import libraries
import simplegui

# define global variables
time_in_milliseconds = 0
time_is_running = False
number_of_tries = 0
number_of_points = 0

# define constant values
milliseconds_in_minute = 600
milliseconds_in_10_seconds = 100
millicesonds_in_second = 10

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t / milliseconds_in_minute
    seconds_10 = t % milliseconds_in_minute / milliseconds_in_10_seconds
    seconds = t % milliseconds_in_minute % milliseconds_in_10_seconds / millicesonds_in_second
    milliseconds = t % milliseconds_in_minute % milliseconds_in_10_seconds % millicesonds_in_second
    return str(minutes) + ":" + str(seconds_10) + str(seconds) + "." + str(milliseconds)
        
# define event handlers for buttons; "Start", "Stop", "Reset"
# start the stopwatch
def start():
    timer.start()
    purr.play()
    global time_is_running
    time_is_running = True

# pause the stopwatch
def stop():
    timer.stop()
    purr.rewind()
    global number_of_tries
    global time_is_running
    global number_of_points
    global time_purring
    
    # if the stopwatch was running check if it was stopped on a full second 
    if time_is_running:
        if time_in_milliseconds % millicesonds_in_second == 0:
            number_of_points += 1
            number_of_tries += 1
            win.play()
        else:
            meuw.play()
            number_of_tries += 1
   
    time_is_running = False
    time_purring = 0

# reset the time and points
def reset():
    timer.stop()
    
    global time_in_milliseconds
    global number_of_tries
    global time_is_running
    global number_of_points
    
    time_in_milliseconds = 0
    purr.rewind()
    number_of_tries = 0
    number_of_points = 0
    time_is_running = False

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_in_milliseconds
    time_in_milliseconds += 1
        
# define draw handler
def draw_handler(canvas):
    canvas.draw_image(image, (600 / 2, 455 / 2), (600, 455), (300, 227), (600, 455))
    canvas.draw_text(str(format(time_in_milliseconds)), (275, 400), 64, 'White', 'monospace')
    canvas.draw_text((str(number_of_points) + "/" + str(number_of_tries)), (470, 325), 36, 'Yellow', 'sans-serif')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 598, 453)

# set timer and background image and sounds
# sound source https://www.freesound.org/
timer = simplegui.create_timer(100, timer_handler)
image = simplegui.load_image('http://stylistics.ie/misc/stopwatcher.jpg')
purr = simplegui.load_sound('http://stylistics.ie/misc/130968__cubilon__purring-cat.wav')
meuw = simplegui.load_sound('http://stylistics.ie/misc/4913__noisecollector__cat1.wav')
win = simplegui.load_sound('http://stylistics.ie/misc/215773__otisjames__win.wav')
purr.set_volume(0.7)
meuw.set_volume(0.4)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 175)
frame.add_button("Stop", stop, 175)
frame.add_button("Reset", reset, 175)

# start frame
frame.start()