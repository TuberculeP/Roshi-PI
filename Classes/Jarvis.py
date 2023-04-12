import inspect

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
        self.__active = True
        self.__status_behavior = default_behavior
        self.__recognizer = Recognizer()
        self.__mapped_tree = {}  # key -> func
        self.__mapped = {}  # func.__name__ -> key
        self.__categories = {}  # class.__name__ -> key
        print("> Recognizer online")
        self.__microphone = Microphone()
        print("> Microphone online")

    def __listen(self):
        """Listen to the microphone and return the result.
        :return: str or None
        """
        with self.__microphone as source:
            self.__recognizer.adjust_for_ambient_noise(source)
            self.__recognizer.pause_threshold = 0.7
            self.__status_behavior(True)
            audio = self.__recognizer.listen(source)
            self.__status_behavior(False)
            try:
                print("> Recieved audio")
                result = self.__recognizer.recognize_google(audio, language="fr-FR")
                return result
            except Exception as e:
                print("> Please try again. Error: " + str(e))
                return None

    def map(self, key, sub=False):
        """Map a function or a class to a key.
        Mapped funcs in Mapped Classes will be executed if the class key is in the entry.
        :param key: str
        :param category: str (optional)
        :return: function
        """
        def decorator(func):
            if inspect.isclass(func):
                self.__mapped_tree[key] = {}
                self.__categories[key] = func
                # for methods in class
                for name, method in inspect.getmembers(func, predicate=inspect.isfunction):
                    print(name)
                    if hasattr(method, "jarvis_map"):
                        # remove key -> func from mapped_commands and add it to sub dict
                        self.__mapped_tree[key][self.__mapped[name]] = self.__mapped_tree[self.__mapped[name]]
                        del self.__mapped_tree[self.__mapped[name]]

            else:
                self.__mapped_tree[key] = func
                self.__mapped[func.__name__] = key
                func.jarvis_map = True

            return func

        return decorator

    def assign_status_behavior(self):
        """Assign a custom behavior to the status of the Jarvis instance."""

        def decorator(func):
            self.__status_behavior = func
            return func

        return decorator

    def run(self):
        print("> All functions found :")
        print(self.__mapped_tree)
        print("> All categories found :")
        print(self.__categories)
        print("Jarvis is running...")
        try:
            while self.__active:
                if (entry := self.__listen()) is not None:
                    print('Entry : "' + entry + '"')
                    if "stop" in entry.lower():
                        print("> Stopping...")
                        break
                    for key, associated in self.__mapped_tree.items():
                        if key in entry.lower():
                            # if key -> sub dict
                            if isinstance(associated, dict):
                                for sub_key, sub_associated in associated.items():
                                    print("> sub_key : " + sub_key)
                                    if sub_key in entry.lower():
                                        print("> method " + sub_key + " in category " + key)
                                        #  then it's a method, we need to construct the class
                                        #  get class name
                                        instance = self.__categories[key]()
                                        method = getattr(instance, sub_associated.__name__)
                                        method()

                            else:
                                associated()
        except KeyboardInterrupt:
            print("Bye")
