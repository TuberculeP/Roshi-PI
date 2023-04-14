from Classes import Jarjar
import turtle as t

# Turtle setup

t.setup(500, 500)
t.bgcolor("white")
t.pencolor("black")
t.speed(0)
t.showturtle()
t.penup()

roshi = Jarjar(Jarjar.LANG_FR)  # Let's introduce our new friend, roshi, master of Turtles


@roshi.override_status_behavior()
def status_behavior(status):
    if status:
        t.fillcolor("green")
    else:
        t.fillcolor("black")


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


roshi.run()
