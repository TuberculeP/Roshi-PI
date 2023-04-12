from Classes import Jarvis

app = Jarvis()

app.register_category("say")


@app.map(key="hello", category="say")
def hi():
    print("Hello World")


app.run()
