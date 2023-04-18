import tkinter as tk
from turtle import RawTurtle, Screen

# Fonction pour quitter l'application
def quitter():
    fenetre.destroy()

# Création de la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Exemple de fenêtre Turtle")
fenetre.geometry("400x400")

# Création d'un canevas pour accueillir le graphique Turtle
canevas = tk.Canvas(fenetre, width=300, height=300)
canevas.pack()

# Création d'un objet Turtle et configuration
tortue = RawTurtle(canvas=canevas)
tortue.shape("turtle")

# Fonction pour dessiner un carré avec la tortue
def dessiner_carre():
    for _ in range(4):
        tortue.forward(100)
        tortue.left(90)

# Bouton pour dessiner un carré
bouton_carre = tk.Button(fenetre, text="Dessiner un carré", command=dessiner_carre)
bouton_carre.pack()

# Bouton pour quitter l'application
bouton_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
bouton_quitter.pack()

# Lancement de la boucle d'événements Tkinter
fenetre.mainloop()