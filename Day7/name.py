#!/usr/bin/python3


def check_name(names):
    name_dict = {}
    for name in names:
        if name[0] == "S":
            if name not in name_dict:
                name_dict[name] = 1
            else:
                name_dict[name] += 1
    return name_dict


names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

print(check_name(names))
