def utf16_value(string):
    total = 0
    # None of this was necessary
    # # lst = []
    # # for char in string:
    # #     lst.append(char)
    # second try
    # lst = []
    # [lst.append(char) for char in string]
    for char in string:
        total += ord(char)
    return total
        


# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)