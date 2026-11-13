import string

def is_palindrome(text):
    text = text.lower()
    text = "".join(char for char in text if char not in string.punctuation and char != " ")

    return text == text[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("0P"))
print(is_palindrome("a."))
print(is_palindrome("aurora"))
print("ОК")