# Day 31: Longest Word
Write a function that has one parameter and takes a list of words
as an argument. The function returns the longest word from the
list. Name the function longest_word. The function should
return the longest word and the number of letters in that word.
For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your
function should return
[10, JavaScript] as the longest word.

## Extra Challenge: Create User
Write a function called create_user. This function asks the
user to enter their name, age, and password. The function
saves this information in a dictionary. For example, if the use
enters name as Peter, age - 18 and password - love. The
function should save the information as: {'name': 'Peter',
'age': 18, 'password': 'love'}
Once the information is saved. The function should print to the
user that - "User saved. Please login"
The function should then ask the user to re-enter their name
and password. If the name and password match with what is
saved in the dictionary, the function should return "Logged in
successfully". If the name and password do not match with
what is saved in the dictionary, the function should print
('Wrong password or user name. Please try again'. The
function should keep running until the user enters correct
logging details.