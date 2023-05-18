'''
Created on 3/5/2023

@author:
Roshan Lau Jee Van A189629
Neoh e-Kin
'''

import turtle
window = turtle.Screen()
pen = turtle.Turtle() #my turtle name is pen for easy understanding... :)
window.bgcolor("cyan")
pen.speed(0)

# reset the pen direction
def reset():
    pen.seth(0)

# move pen
def move_pen(xpos, ypos):
    '''move the pen to the respective location'''
    pen.penup()
    pen.goto(xpos, ypos)
    pen.down()

# set pen color
def setColor_pen(color):
    '''set the pen to the respective color'''
    pen.color(color)

# draw grass 
def grass(xpos, ypos, width, height, color="green"):
    '''draw green color grass with 4 parameters which are starting x position, starting y position, width and height respectively'''
    reset()
    move_pen(xpos, ypos)
    setColor_pen(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# draw mountain
def mountain(xpos, ypos, size, color="brown"):
    '''draw mountain with 4 parameters which are starting x position, starting y position, size and color respectively'''
    reset()
    move_pen(xpos, ypos)
    setColor_pen(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

# draw sun
def sun(xpos, ypos, size, color="yellow1"):
    '''draw sun with 4 parameters which are starting x position, starting y position, size and color respectively'''
    reset()
    move_pen(xpos, ypos)
    pen.color("yellow")
    for i in range(120):
        pen.forward(80)
        pen.right(80)
        pen.forward(30)
        pen.left(30)
        pen.forward(30)
        pen.right(60)
        
        pen.penup()
        pen.setposition(xpos, ypos)
        pen.pendown()
        
        pen.right(4)
    

def tree(xpos, ypos):
    '''draw a tree with 2 parameters which are starting x position and starting y position respectively'''
    reset()
    move_pen(xpos, ypos)
    # Tree trunk
    pen.color("brown4")
    pen.begin_fill()
    for i in range(2):
        pen.forward(10)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    # Turn the turtle around
    pen.penup()
    pen.forward(30)
    pen.left(90)
    pen.forward(50)
    pen.down()
    # Leaves on tree
    pen.color("limegreen")
    pen.begin_fill()
    pen.circle(25)
    pen.end_fill()

# draw mountain cap
def mountain_cap():
    '''draw moutain cap'''
    reset()
    # Middle Mountain Ice Cap
    pen.penup()
    pen.goto(-35, 120)
    pen.pendown()
    pen.color("snow3")
    pen.begin_fill()
    pen.left(35)
    pen.forward(60)
    pen.right(90)
    pen.forward(30)
    pen.left(100)
    pen.forward(45)
    pen.right(85)
    pen.forward(65)
    pen.left(160)
    pen.forward(150)
    pen.end_fill()

    # Left Mountain Ice Cap
    pen.penup()
    pen.goto(-215, 100)
    pen.pendown()
    pen.color("snow2")
    pen.begin_fill()
    pen.forward(70)
    pen.left(120)
    pen.forward(75)
    pen.left(150)
    pen.forward(45)
    pen.right(90)
    pen.forward(45)
    pen.left(120)
    pen.end_fill()

    # Right Mountain Ice Cap
    pen.penup()
    pen.goto(203, 80)
    pen.pendown()
    pen.color("snow1")
    pen.begin_fill()
    pen.forward(95)
    pen.right(120)
    pen.forward(80)
    pen.right(150)
    pen.forward(50)
    pen.left(70)
    pen.end_fill()
    pen.left(50)
    
def mainDraw():
    # draw grass
    grass(-500, -100, 1000, 400)
    # draw left moutain
    mountain(-400, -100, 300)
    # draw right mountain
    mountain(100, -100, 300, "brown1")
    # draw middle moutain
    mountain(-160, -100, 400, "brown3")
    # draw sun
    sun(420, 280, 125)
    # draw tree 1
    tree(-125,-100)
    # draw tree 2
    tree(-100,-250)
    # draw tree 3
    tree(-300,-250)
    # draw tree 4  
    tree(300,-250)
    # draw tree 5
    tree(200,-100)
    # draw tree 6 
    tree(432,-123)
    # draw tree 7
    tree(89,-143)
    # draw mountain cap
    mountain_cap()
    
if __name__ == '__main__':
    mainDraw() 

window.exitonclick()
