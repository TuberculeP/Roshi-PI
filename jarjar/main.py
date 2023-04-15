from jarjar.utils import m2c, default_behavior
import inspect
from speech_recognition import Recognizer, Microphone


class Jarjar:
    """Jarvis is a class that allows you to create a voice assistant."""

    # Langs shortcuts
    LANG_FR = "fr-FR"
    LANG_US = "en-US"

    def __init__(self, lang=LANG_FR, phrase_time_limit=5, pause_threshold=0.7):
        self.__active = True
        self.__lang = lang
        self.__status_behavior = default_behavior
        self.__recognizer = Recognizer()
        self.__recognizer.pause_threshold = pause_threshold
        self.__phrase_time_limit = phrase_time_limit
        self.__mapped_tree = {}  # key -> func
        self.__mapped = {}  # func.__name__ -> key
        self.__categories = {}  # class.__name__ -> key
        self.__valued = {}  # func.__name__ -> key
        print("> Recognizer online")
        self.__microphone = Microphone()
        print("> Microphone online")

    def __listen(self):
        """Listen to the microphone and return the result.
        :return: str or None
        """
        with self.__microphone as source:
            self.__recognizer.adjust_for_ambient_noise(source)
            self.__status_behavior(True)
            audio = self.__recognizer.listen(source, phrase_time_limit=self.__phrase_time_limit)
            self.__status_behavior(False)
            try:
                print("> Recieved audio")
                result = self.__recognizer.recognize_google(audio, language=self.__lang)
                return result
            except Exception as e:
                print("> Please try again. Error: " + str(e))
                return None

    def map(self, key, param_trigger=None):
        """Map a function or a class to a key.
        Mapped main.py in Mapped jarjar will be executed if the class key is in the entry.
        :param key: str
        :param param_trigger: list (optional)
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
                if param_trigger is not None:
                    self.__valued[func.__name__] = param_trigger

            return func

        return decorator

    def override_status_behavior(self):
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
        print("> All valued functions found :")
        print(self.__valued)
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
                                        self.exec(getattr(instance, sub_associated.__name__), entry)

                            else:
                                print("> function " + key)
                                self.exec(associated, entry)
        except KeyboardInterrupt:
            print("Bye")

    def exec(self, func, entry):
        """Execute a function.
        :param func: function
        :param entry: str
        """
        if func.__name__ in self.__valued:
            # get key
            params = self.__valued[func.__name__]

            values = []

            # foreach params, we seek for param in entry, then get the number before
            for param in params:
                if param in entry:
                    # get the index of the param
                    index = entry.index(param)
                    # get the number at index -1 (skip spaces)
                    number = ""
                    while entry[index - 1] == " ":
                        index -= 1
                    while entry[index - 1].isdigit():
                        number = entry[index - 1] + number
                        index -= 1
                    # convert to int
                    number = int(number)
                    # add to values
                    values.append(number)

            # if we have values
            if len(values) > 0:
                # execute function with values as params
                func(*values)
            else:
                # try to see if the word before the param is a number written in letters
                # to do so, we pass the word before the param to mot2chiffre
                for param in params:
                    if param in entry:
                        # get the index of the param
                        index = entry.index(param)
                        # get the word before the param
                        word = ""
                        while entry[index - 1] == " ":
                            index -= 1
                        while entry[index - 1].isalpha():
                            word = entry[index - 1] + word
                            index -= 1
                        # convert to int
                        number = m2c(word)
                        # add to values
                        values.append(number)

                # if we have values
                if len(values) > 0:
                    # execute function with values as params
                    func(*values)
                else:
                    func()

        else:
            func()
