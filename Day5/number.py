
def number_enrolled(a_list):
    new = []
    for i in a_list:
        new.append(i.lower())
    output = [('Male'), new.count('male'), ('female'), new.count('female')]
    return output

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
