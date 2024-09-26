"""
Name: Ali Shirazi Zamani
Level: 1
Homework: 2
Exercise: 4
Write a function that calculates neper number to the power
of (x) with (n) term approximation and presicion of 3.
"""
def factorial(number: int) -> int:
    """
    Calculates and returns factorial of input number.
    """

    total = 1
    for i in range(1, number + 1):
        total = total * i

    return total    

def round_to_3(number: float) -> float:
    """
    Rounds input number to 3 decimal numbers and returns it.
    """
    if '.' in str(number):
        tmp = str(number).split('.')
    else:
        return number

    if len(tmp[1]) <= 3:
        return number

    if int(tmp[1][3]) < 5:
        tmp[1] = tmp[1][:3]    
        number = float('.'.join(tmp))
    else:
        tmp[1] = str(int(tmp[1][:3]) + 1)
        number = float('.'.join(tmp))

    return number        

def e_power(x: int | float, n: int) -> float:
    """
    Calculates neper number to the power of (x) with 
    (n) approximation terms rounded to 3 decimal numbers.
    """

    total = 0
    for i in range(n):
        term = x**i/factorial(i)
        total = total + term

    return round_to_3(total)    

x = int(input("Enter power: "))
n = int(input("Enter number of approximation terms: "))

print(f"e to the power of {x} with {n} approximation terms = {e_power(x, n)}")