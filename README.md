# Roshi (x Jarjar)

**Roshi** est une application développée en Python3 permettant le contrôle vocal de [Turtle Graphics](https://docs.python.org/fr/3/library/turtle.html) à la voix. 

Elle tourne grâce à **Jarjar 1**, un framework Speech-To-Function fait maison.

## Prérequis & Dépendances

- Python 3
- PiP
- SpeechRegognition : `pip install SpeechRecognition`
- PyAudio : `pip install PyAudio`
- Turtle Graphics (inclus avec Python3)
- Un microphone

## À propos de Jarjar 1

Jarjar est un framework cuisiné par [Félix Laviéville](https://github.com/TuberculeP) en partant d’un projet original de [Pierrick Chevron](https://www.linkedin.com/in/pierrick-chevron-42b05810b/).

Sa structure et son utilisation sont similaires au système de routage Flask ou Symfony (PHP 8.1). Elle repose sur les décorateurs. Grâce à cela, il suffit d’associer un mot ou un groupe de mots à une fonction à exécuter :

```python
from Jarjar import Jarjar # Récupérer la classe principale

app = Jarjar() # Changer la langue par défaut : lang=Jarjar.LANG_US

@app.map("bonjour")
def sayHello():
	print("Hello World")

@app.run()

# Maintenant à chaque fois que le mot "bonjour" est détecté, "Hello World" est affiché
```

Jarjar 1 propose également un système de catégorisation à travers les classes :

```python
from Jarjar import Jarjar
app = Jarjar()

@app.map("affiche")
class StuffToPrint:
	
	@app.map("bonjour")
	def sayHello():
		print("Hello World")

	@app.map("au revoir")
	def sayBye():
		print("Goodbye !")

# sayHello et sayBye ne seront désormais exécutés que si "affiche" + clé est prononcé

@app.run()
```

Enfin, parlons de la détection de la voix. La voix est enregistrée via Microphone de SpeechRecognition et transformée en texte via Google. Par défaut, Jarjar prévient que l’enregistrement est en cours en affichant dans la console “> Listening”, “> Not Listening”.

Il est possible de changer ce comportement par défaut avec la méthode :

```python
from Jarjar import Jarjar
import turtle as t

app = Jarjar()


# Voici un exemple d'override avec turtle

@app.override_status_behavior()
def status_behavior(status):
    if status:
        t.fillcolor("green")
    else:
        t.fillcolor("black")

# "Listening" correspondra à une tortue verte et "Not Listening" à une tortue noire
```