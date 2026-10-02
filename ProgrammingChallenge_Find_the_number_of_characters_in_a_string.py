# In a .py file, write a program which calculates the number of characters in a string.
# 1. The string should be entered using input() and assigned to a variable.
string_phrase = str(input("Enter a string of text: "))
total = 0
for letter in string_phrase:
    total += 1
print("The string of text entered: " + string_phrase)
print("The total number of characters in the string: " + str(total))