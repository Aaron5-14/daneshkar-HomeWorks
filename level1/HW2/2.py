"""
Name: Ali Shirazi Zamani
Level: 1
Homework: 2
Exercise: 2
Write a function that converts celsius to farenheit,
then without using loops apply it on a sequence of temperatures.
"""

def to_farenheit(celsius: int | float | str) -> float:
    """
    Converts input celsius temperature into farenheit and returns it.
    """

    farenheit = 9 * float(celsius) / 5 + 32
    return farenheit

temps = input("Enter temperatures in celsius separated by space: ")
temps = temps.split(' ')
temps = map(float, temps)
temps = map(to_farenheit, temps)
temps = map(str, temps)
temps = ' '.join(temps)
print(f"Temperatures in farenheit: {temps}")