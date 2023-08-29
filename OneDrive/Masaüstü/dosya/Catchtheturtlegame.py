import turtle
from random import randint

SMALL_FONT = ('Arial', 15, 'normal')
MEDIUM_FONT = ('Arial', 30, 'normal')
LARGE_FONT = ('Arial', 50, 'normal')

screen=turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the turtle")

target=turtle.Turtle()
target.penup()
target.color("green")
target.setposition(randint(-300,300),(randint(-300,300)))
target.shape("turtle")

score_keeper=turtle.Turtle()
score_keeper.hideturtle()
score_keeper.penup()

seconds=int(screen.numinput("Timer","Enter the seconds",minval=0,maxval=300))

time_keeper=score_keeper.clone()

time_keeper.sety(370)
time_keeper.write("Time Left:", align='center', font=SMALL_FONT)
time_keeper.sety(300)
time_keeper.write(seconds, align='center', font=LARGE_FONT)

def change_positions():
    target.hideturtle()
    x =randint(-300,300)
    y =randint(-300,300)
    target.goto(x,y)
    target.showturtle()
    
    
    

score= 0

def uptade_score():
    global score

    score += 1
    score_keeper.clear()
    score_keeper.write(score,align="center",font=SMALL_FONT)

def update_time():
    time_keeper.undo() 
    time_keeper.write(seconds,align="center",font=LARGE_FONT) 

def target_clicked(x,y):
    if seconds >= 0:
        uptade_score()
        change_positions()      

def action():
    global seconds

    seconds -= 1
    if seconds <= 0:
        target.hideturtle()

        time_keeper.clear()
        time_keeper.sety(320)
        time_keeper.write("Time Over", align='center', font=MEDIUM_FONT)
    else:
        update_time()
        screen.ontimer(action, 1000)

def change_position_timer():
    
    screen.ontimer(change_positions,5000)

target.onclick(target_clicked)

change_positions()

action()

screen.mainloop()


    



    











