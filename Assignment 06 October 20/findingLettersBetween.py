import string

letters = string.ascii_letters

user_input = input("Write your first and last letter Example(a-g): ") # User write his letters
start, end = user_input.split("-") # It splits user's letters and assign them to "start" and "end"

start_index = letters.index(start) # finding index of the first letter
end_index = letters.index(end) # finding index of the last letter

print(letters[start_index:end_index + 1]) #finding letters that are between those to letters