#!/usr/bin/python3


def remove_char_at(str, n):
    first = str[:n] 
    last = str[n + 1:]

    return first + last
