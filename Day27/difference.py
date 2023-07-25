#!/usr/bin/python3


def difference(list_one, list_two):
    """
    # Elements in list1 but not in list2
    unique_to_list1 = [x for x in list1 if x not in list2]

    # Elements in list2 but not in list1
    unique_to_list2 = [x for x in list2 if x not in list1]

    # Combine both lists and return the result
    return unique_to_list1 + unique_to_list2
    """
    return list(set(list_one) ^ set(list_two))





list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1, list2))
