def correct_sentence(text):
    text = text.capitalize()

    if not text.endswith("."):
        text += "."

    return text

massage = input("Write down your massage: ")
print(correct_sentence(massage))