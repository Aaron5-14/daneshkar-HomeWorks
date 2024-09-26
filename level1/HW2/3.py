"""
Name: Ali Shirazi Zamani
Level: 1
Homework: 2
Exercise: 3
Write a function that calculates sum of digits of an input number
and keeps doing it as long as the resulst is greater than 10.
"""

def sum_digits(number: int) -> int:
    """
    Calculates sum of digits of input number and returns it.
    """

    digits = [int(digit) for digit in str(number)]
    number = sum(digits)

    return number    

usr_inp = int(input("Enter number: "))
sum_of_digits = sum_digits(usr_inp)
while sum_of_digits > 10:
    sum_of_digits = sum_digits(sum_of_digits)

print(f"Result is: {sum_of_digits}")