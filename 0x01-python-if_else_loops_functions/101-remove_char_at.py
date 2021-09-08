#!/usr/bin/python3


def remove_char_at(str, n):
    if n >= 0:
        first = str[:n]
        last = str[n + 1:]
        return first + last
    else:
        return str
