from jarjar import Jarjar
import turtle
import tkinter as tk

# Turtle setup
root = tk.Tk()
root.geometry("500x500")
root.title("Roshi : Master of Turtles")
root.resizable(False, False)
roshi = Jarjar()
button = tk.Button(root, text="Quit", command=root.destroy)
button.pack()








canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

var = tk.StringVar()
var.set("Online")
label = tk.Label(root, textvariable=var)
label.pack()

t = turtle.RawTurtle(canvas)


def lancement():
    if not roshi.get_status():
        var.set("Online")
        roshi.run()


Relance = tk.Button(root, text='relancer', command=lancement)
Relance.configure( font=('Helvetica', 12), bd=4, relief='flat', highlightthickness=0, padx=10, pady=5, )

t.shape("turtle")

t.pencolor("black")
t.speed(0)
t.showturtle()
t.penup()



default_color = "black"

@roshi.override_status_behavior()
def status_behavior(status):
    if status:
        t.fillcolor("green")
    else:
        t.fillcolor(default_color)

@roshi.override_quit_behavior()
def onQuit():
    var.set('Offline')
    Relance.pack()


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
root.mainloop()
