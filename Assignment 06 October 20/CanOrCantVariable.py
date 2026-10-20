import keyword

name = input("Write down your variable: ")

if (name.isidentifier() and name.lower() and "__" not in name and name not in keyword.kwlist):
    print(True)
else:
    print(False)