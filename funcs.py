import turtle
import random

def set_window():
    wn = turtle.Screen()
    wn.reset
    wn.title("Snake")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)    # turns off screen updates
    
    return wn

def create_snake_head():
    head = turtle.Turtle()
    head.speed(0)   # zero slow down
    head.shape("square")
    head.color("green")
    head.penup()    # dont draw anything as turtle moves
    head.goto(0,0)  #starting position
    head.direction = "stop"
    
    return head

def create_new_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()    
    
    return new_segment

def create_food():
    
    food = turtle.Turtle()
    food.speed(0)   # zero slow down
    food.shape("circle")
    food.color("red")
    food.penup()    # dont draw anything as turtle moves
    food.goto(0,100)  #starting position
    
    return food

def create_pen():
    pen = turtle.Turtle()
    pen.speed(0)   # zero slow down
    pen.shape("square")
    pen.color("white")
    pen.penup()    # dont draw anything as turtle moves
    pen.hideturtle()
    pen.goto(0,260)  #starting position
    pen.write("Score: 0   Highscore: 0", align = "center", font = ("Courier", 24, "normal"))

    return pen

def move(head, vel):
    
    if head.direction == "up":    
        y = head.ycor()
        head.sety(y + vel)
        
    elif head.direction == "down":    
        y = head.ycor()
        head.sety(y - vel)
        
    if head.direction == "right":    
        x = head.xcor()
        head.setx(x + vel)
        
    elif head.direction == "left":    
        x = head.xcor()
        head.setx(x - vel)
        
def move_body(head, segments):
    
    al = True
    
    if len(segments) > 1:
        
        for i in range(len(segments)-1,0,-1):
            
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            
            segments[i].goto(x,y)
            
            if head.distance(segments[i]) < 5:
                al = False
                
        
    if len(segments) > 0:    
        
        segments[0].goto(head.xcor(),head.ycor())
        
    return al

def move_food(food):
    x = 20 * random.randint(-14,14)
    y = 20 * random.randint(-14,14)
    
    food.goto(x,y)