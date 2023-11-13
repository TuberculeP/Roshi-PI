import webbrowser
from jarjar import Jarjar

app = Jarjar()


@app.map("ouvre")
class Websites:

    @app.map("google")
    def google(self):
        webbrowser.open("https://www.google.com")

    @app.map("youtube")
    def youtube(self):
        webbrowser.open("https://www.youtube.com")

    @app.map("netflix")
    def netflix(self):
        webbrowser.open("https://www.netflix.com")


app.run()
