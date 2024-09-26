"""
Name: Ali Shirazi Zamani
Level: 1
Homework: 2
Exercise: 1 
Write a function that validates input postal code,
then use it to validate a sequence of user inputs.
"""

def is_valid(str: str) -> bool:
    """
    Function that takes string as input and checks if 
    it is a valid postal code, returns True if valid
    otherwise returns false.
    """
    if '-' not in str:
        return False
    
    str_splt = str.split('-')
    if len(str_splt) != 2:
        return False
    
    for splt in str_splt:
        if not splt.isnumeric() and len(splt) != 5:
            return False

    return True

# main 
while True:
    usr_inp = input("Enter text or type 'quit' to stop: ")
    if usr_inp == 'quit':
        break

    text = usr_inp.split(' ')
    filtered_text = [splt for splt in text if is_valid(splt)]
    output = ' '.join(filtered_text)
    print("Filtered Text: ", output)