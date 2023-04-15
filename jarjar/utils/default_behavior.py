"""
Utils : Default Behavior
Description : Default Jarjar status behavior
Author : @TuberculeP
"""


def default_behavior(status):
    """Default behavior for the status of the Jarvis instance.
    :param status: bool
    """
    if status:
        print("> Listening...")
    else:
        print("> Not listening...")
