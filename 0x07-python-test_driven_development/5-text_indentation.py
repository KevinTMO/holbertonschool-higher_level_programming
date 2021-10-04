#!/usr/bin/python3


def text_indentation(text):
    """
    This method should print a text
    Text: is a string
    - if text is not a string:
         - raise TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delim = ".?:"

    text = text.strip()

    for newText in text:
        if newText not in delim:
            print(newText, end="")
        else:
            print(newText)
            print('\n')
