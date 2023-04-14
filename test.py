from Classes import Jarjar


test = Jarjar(Jarjar.LANG_FR)  # Let's introduce our new friend, roshi, master of Turtles


@test.map("boucle", param_trigger=["fois", "pixels"])
def loop(f, p):
    for i in range(f):
        print("Coucou ! {}".format(i))
    print("Pixels : {}".format(p))


test.run()
