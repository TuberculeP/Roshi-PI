from jarjar import Jarjar
import turtle as t

# Turtle setup

t.setup(500, 500)
t.bgcolor("white")
t.pencolor("black")
t.speed(0)
t.showturtle()
t.penup()

roshi = Jarjar()

default_color = "black"

@roshi.override_status_behavior()
def status_behavior(status):
    if status:
        t.fillcolor("green")
    else:
        t.fillcolor(default_color)


@roshi.map("recule")
def back():
    t.backward(100)


@roshi.map("avance")
def fw():
    t.forward(100)


@roshi.map("tourne")
class Rotate:

    @roshi.map("gauche", param_trigger=["degrés"])
    def left(self, deg=90):
        t.left(deg)

    @roshi.map("droite", param_trigger=["degrés"])
    def right(self, deg=90):
        t.right(deg)


@roshi.map("dessine")
class Draw:

    @roshi.map("carré", param_trigger=["pixels"])
    def square(self, p=100):
        t.pendown()
        for _ in range(4):
            t.forward(p)
            t.left(90)
        t.penup()

    @roshi.map("triangle", param_trigger=["pixels"])
    def triangle(self, p=100):
        t.pendown()
        for _ in range(3):
            t.forward(p)
            t.left(120)
        t.penup()

    @roshi.map("figure", param_trigger=["côtés", "pixels"])
    def polygon(self, c, l=100):
        t.pendown()
        for _ in range(c):
            t.forward(l)
            t.left(360/c)
        t.penup()

@roshi.map("couleur")
class Color:
    @roshi.map("noir")
    def switchBlack(self):
        t.pencolor("black")
        global default_color
        default_color = "black"

    @roshi.map("rouge")
    def switchRed(self):
        t.pencolor("red")
        global default_color
        default_color = "red"

    @roshi.map("bleu")
    def switchBlue(self):
        t.pencolor("blue")
        global default_color
        default_color = "blue"

roshi.run()
