string = input("Enter string: ")
modified_string = ""
for char in string:
    if not char.isspace():
        if char.lower() in ['a', 'o', 'e', 'i', 'e']:
            char = '.'
            modified_string += char
        else:
            if char.islower():
                modified_string += char.upper()
            else:
                modified_string += char.lower()

print(modified_string)