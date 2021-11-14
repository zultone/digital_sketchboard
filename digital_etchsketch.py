import turtle as bob

message = "Arrow keys to move. Q and A keys for thicker/thinner line\n 1. Red, 2. Green, 3. Blue, 4. Black, 5. Yellow, 6. Pink, 7. Brown, 8. Grey, 9. Eraser\n Change eraser size with Q and A keys"
bob.color('black')
bob.up()
bob.goto(-250,275)
style = ('Courier', 10, 'italic')
bob.write(message, font=style, align='left')
bob.goto(0,0)
bob.down()


bob.speed(0)
width = 1


def red():
    bob.color("red")
    
def green():
    bob.color("green")
    
def blue():
    bob.color("blue")
    
def black():
    bob.color("black")

def yellow():
    bob.color("yellow")

def pink():
    bob.color("pink")

def brown():
    bob.color("brown")

def grey():
    bob.color("grey")

def white():
    bob.color("white")
    
def up():
    bob.setheading(90)
    bob.forward(10)
def down():
    bob.setheading(270)
    bob.forward(10)
def right():
    bob.setheading(0)
    bob.forward(10)
def left():
    bob.setheading(180)
    bob.forward(10)
def bigger_line():
    global width
    width += 1
    bob.width(width)
def smaller_line():
    global width
    if width >= 1:
        width -= 1
        bob.width(width)

    
bob.onkey(up,"Up")
bob.onkey(down,"Down")
bob.onkey(left,"Left")
bob.onkey(right,"Right")
bob.onkey(bigger_line,"q")
bob.onkey(smaller_line,"a")
bob.onkey(red,"1")
bob.onkey(green,"2")
bob.onkey(blue,"3")
bob.onkey(black,"4")
bob.onkey(yellow,"5")
bob.onkey(pink,"6")
bob.onkey(brown,"7")
bob.onkey(grey,"8")
bob.onkey(white,"9")
bob.listen()



bob.done()
