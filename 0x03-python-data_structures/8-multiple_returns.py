#!/usr/bin/python3
# Return lenght and first char of a sentence


def multiple_returns(sentence):
    """
    Will return the len and first chr of a sentence
    sentence: is the string to get the lenght and first chr
    """
    lenStr = len(sentence)

    return (lenStr, sentence[0] if lenStr > 0 else None)
