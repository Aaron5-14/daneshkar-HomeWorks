"""
Name: Ali Shirazi Zamani
Level: 2
Homework: 3
Exercise: 2
To do: First research about LBYL and EAFP, then create a function that 
divides two numbers and works for all possbile input that may give error.
For example it should return math.inf for division by zero.
"""
import math
def divide(a: int | float, b: int | float) -> float:
    """
    Divides a by b and returns result
    """
    if b == 0:
        return math.inf
    
    return a / b

print(f"5 / 0 = {divide(5, 0)}")
print(f"11 / 6 = {divide(11, 6)}")
    



