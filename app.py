from Classes import Jarvis as TextToAction
import turtle as t

# Turtle setup

t.setup(500, 500)
t.bgcolor("white")
t.pencolor("black")
t.speed(0)
t.showturtle()
t.penup()

roshi = TextToAction()  # Let's introduce our new friend, roshi, master of Turtles


@roshi.assign_status_behavior()
def status_behavior(status):
    if status:
        t.pencolor("red")
    else:
        t.pencolor("black")


roshi.register_category("dis")  # To print stuff on the console
roshi.register_category("dessine")  # To draw stuff on the screen
roshi.register_category("tourne")  # To draw stuff on the screen


@roshi.map(key="bonjour", category="dis")
def hi():
    print("Hello World")


@roshi.map(key="avance")
def forward():
    t.forward(100)


@roshi.map(key="recule")
def backward():
    t.backward(100)


@roshi.map(key="droite", category="tourne")
def right():
    t.right(90)


@roshi.map(key="gauche", category="tourne")
def left():
    t.left(90)


@roshi.map(key="carré", category="dessine")
def draw_square():
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.penup()


roshi.run()
