#!/usr/bin/python3


def sorted_names(names_list):
    def get_last_name(name):
        return name.split()[-1]

    sorted_list = sorted(names_list, key=get_last_name)
    formatted_list = [f"{name.split()[-1]} {name.split()[0]}" for name in sorted_list]

    return formatted_list


names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
sorted_names_list = sorted_names(names)
print(sorted_names_list)
