import string

# User write a word or words
text = input("Write down your word: ")
words = text.split() # Split the words
result = ""

for word in words:
    for char in string.punctuation: # Char contains a string.punctuation
        word = word.replace(char, "") # Remove every punctuation from char
    result += word.capitalize() # Change result to a word with a capitalized letter

hashtag = "#" + result # Add a "#" in front
hashtag = hashtag[:140] # So it's limited a word to 140 words

print(hashtag)
