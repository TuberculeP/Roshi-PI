from speech_recognition import Recognizer, Microphone


def default_behavior(status):
    """Default behavior for the status of the Jarvis instance.
    :param status: bool
    """
    if status:
        print("> Listening...")
    else:
        print("> Not listening...")


class Jarvis:
    """Jarvis is a class that allows you to create a voice assistant."""

    def __init__(self):
        self.active = True
        self.status_behavior = default_behavior
        self.recognizer = Recognizer()
        self.mapped_commands = {}
        print("> Recognizer online")
        self.microphone = Microphone()
        print("> Microphone online")
        print("> " + self.str_config())

    def str_config(self) -> str:
        """Return a string with the current configuration of the Jarvis instance.
        :return: str
        """
        return """Running with active: {}""".format(self.active)

    def listen(self):
        """Listen to the microphone and return the result.
        :return: str or None
        """
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.pause_threshold = 0.7
            self.status_behavior(True)
            audio = self.recognizer.listen(source)
            self.status_behavior(False)
            try:
                print("> Recieved audio")
                result = self.recognizer.recognize_google(audio, language="fr-FR")
                return result
            except Exception as e:
                print("> Please try again. Error: " + str(e))
                return None

    def map(self, key, category=None):
        """Map a function to a key.
        :param key: str
        :param category: str (optional)
        :return: function
        """

        def decorator(func):
            if category is None:
                self.mapped_commands[key] = func
            else:
                self.mapped_commands[category][key] = func
            return func

        return decorator

    def register_category(self, name):
        """Register a function category to the Jarvis instance.
        :param name: Category
        """
        self.mapped_commands[name] = {}

    def assign_status_behavior(self):
        """Assign a custom behavior to the status of the Jarvis instance."""
        def decorator(func):
            self.status_behavior = func
            return func

        return decorator

    def run(self):
        print("Jarvis is running...")
        try:
            while self.active:
                if (entry := self.listen()) is not None:
                    print('Entry : "' + entry + '"')
                    if "stop" in entry.lower():
                        print("> Stopping...")
                        break
                    for key, associated in self.mapped_commands.items():
                        if key in entry.lower():
                            # if category
                            if isinstance(associated, dict):
                                print("> Category : " + key)
                                for word, func in associated.items():
                                    if word in entry.lower():
                                        print("> Executing function : " + word)
                                        func()
                            else:
                                associated()
        except KeyboardInterrupt:
            print("Bye")
