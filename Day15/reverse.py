#!/usr/bin/python3


def same_in_reverse(a_string):
    return a_string == a_string[:: -1]


print(same_in_reverse('dad'))
