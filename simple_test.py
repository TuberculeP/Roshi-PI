from jarjar import Jarjar

instance_test = Jarjar()

@instance_test.map("dis bonjour")
def say_hello():
    print("Bonjour !")


instance_test.run()