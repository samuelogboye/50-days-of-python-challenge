#!/usr/bin/python3

def register_check(a_dict):
    count = 0
    for i in a_dict:
        if a_dict.get(i) == 'yes':
            count += 1
    return count


register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(register))
