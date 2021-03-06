#These are the defined functions used in Assn 10

import turtle, random

def setup():
    import turtle
    turtle.penup()
    turtle.speed(150)
    turtle.screensize (1000,800)
    import random
    global colors
    colors = ("red", "green", "purple", "blue", "yellow", "pink", "black", "orange","deep sky blue", "medium spring green",
        "coral", "indian red", "gold", "lemon chiffon", "dark cyan", "olive drab", "dark turquoise", "dodger blue", "alice blue",
        "pale goldenrod", "royal blue", "light gray", "cadet blue", "light salmon", "rosy brown", "deep pink", "antique white",
        "plum", "seashell")



def drawRectangle (height, width):
    for i in range (2):
        turtle.forward (width)
        turtle.left (90)
        turtle.forward (height)
        turtle.left (90)

def drawRectanglePattern (centerX, centerY, offset, width, height, count, rotation):
    for j in range (count):
        color = random.choice(colors)
        turtle.color (color)
        turtle.goto (centerX, centerY)
        turtle.forward (offset)
        turtle.left (rotation)
        turtle.pendown()
        drawRectangle (height, width)
        turtle.penup ()
        turtle.right(rotation)
        turtle.goto (centerX, centerY)
        turtle.left (360 / count)

def drawCirclePattern (centerX, centerY, offset, radius, count):
    for i in range (count):
        color = random.choice(colors)
        turtle.color (color)
        turtle.goto (centerX, centerY)
        turtle.forward (offset)
        turtle.pendown()
        turtle.circle (radius)
        turtle.penup ()
        turtle.goto (centerX, centerY)
        turtle.left (360 / count)

def drawSuperPattern (patternNumber):

    for i in range (patternNumber):
        centerX = random.randint(-500, 500)
        centerY = random.randint(-400, 400)
        offset = random.randint(-100, 100)
        radius = random.randint(-100, 100)
        rotation = random.randint(-90, 90)
        width = random.randint(-100, 100)
        height = random.randint(-100, 100)
        count = random.randint(-100, 100)
        super = random.randint (0,1)
        if super == 0:
            turtle.penup ()
            drawRectanglePattern(centerX, centerY,offset, width, height, count, rotation)
        elif super == 1:
            turtle.penup()
            drawCirclePattern(centerX, centerY, offset, radius, count)



def reset ():
    turtle.reset ()

def done ():
    turtle.done()