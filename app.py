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
        t.fillcolor("blue")
    else:
        t.fillcolor("black")


@roshi.map("dessine")
class Draw:

    @roshi.map("carré")
    def square(self):
        t.pendown()
        for _ in range(4):
            t.forward(100)
            t.left(90)
        t.penup()

    @roshi.map("triangle")
    def triangle(self):
        t.pendown()
        for _ in range(3):
            t.forward(100)
            t.left(120)
        t.penup()


@roshi.map("test")
def test():
    print("test")


roshi.run()
