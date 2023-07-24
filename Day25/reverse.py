#!/usr/bin/python3


def read_backwards(string):
    words = string[::-1].split(" ")
    a = ""
    for i in words:
        a += i[::-1] + " "
    return a.strip()


print(read_backwards("the love is real"))
