from funcs import *
import time

delay = 0.1
vel = 20

# set up screen
wn = set_window()

# snake head
head = create_snake_head()

# snake body
segments = []

# snake food
food = create_food()

# pen
pen = create_pen()

# keyboard bindings
def go_up():
    if head.direction != "down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_right():
    if head.direction != "left":
        head.direction = "right"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"        

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

# main loop
alive = True

score = 0
highscore = 0

while True:   # play again

    while alive:
        
        #cont += 1
        wn.update()
        
        #### Collision with food #############
        
        if head.distance(food) < 20:
        
            move_food(food)
            
            new_segment = create_new_segment()    
            segments.append(new_segment)
            
            score += 10
            
            if score > highscore:
                
                highscore = score
            
            pen.clear()
            pen.write("Score: {}   Highscore: {}".format(score, highscore), align = "center", font = ("Courier", 24, "normal"))
        
        al = move_body(head,segments)
        
        if not al:
            alive = False
            
        move(head, vel)
        
        time.sleep(delay)
        
        if abs(head.xcor()) > 300 or abs(head.ycor()) > 300: #out of bounds
            alive = False
     
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    
    for segment in segments:
        segment.goto(1000,1000)
    
    # reset game after snake dies
    segments = []
    score = 0
    
    pen.clear()
    pen.write("Score: {}   Highscore: {}".format(score, highscore), align = "center", font = ("Courier", 24, "normal"))
    
    alive = True

wn.mainloop()   # keep window open

