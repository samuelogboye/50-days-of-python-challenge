# Day 15: Same in Reverse
Write a function called same_in_reverse that takes a string
and checks if the string reads the same in reverse. If it is the
same, the code should return True if not, it should return False.
For example, ‘dad’ should return True, because it reads the
same in reverse.

## Extra Challenge: What’s My Age?
Write a function called your_age. This function asks a student
to enter their name and then it returns their age. For example, if
a user enters Peter as their name, your function should return,
‘Hi, Peter, you are 27 years old. This function reads data
from the database (dictionary below). If the name is not in the
dictionary, your code should tell the user that their name is not
in the dictionary, and ask them for their age. Your code should
then add the name and age to the dictionary of names_age
below. Once added your code should return to the user ‘Hi,
(added name), you are (added age) years old’. Remember
to convert the input from user to lowercase letters
names_age = {"jane": 23, "kerry": 45, "tim": 34, “peter": 27}