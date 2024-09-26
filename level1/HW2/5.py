"""
Name: Ali Shirazi Zamani
Level: 1
Homework: 2
Exercise: 5
Write a function that does binary search algorithm recursively
for a sequence of ordered numbers.
"""
def binary_search(target: int, *numbers, start: int = 0, end: int = None) -> int:
    """
    Finds index of target in numbers and returns it.
    """
    if end != None and end < start:
        return -1
    
    if end == None:
        end = len(numbers) - 1

    middle = (end - start + 1) // 2 + start
    if numbers[middle] == target:
        return middle
    elif numbers[middle] > target:
        return binary_search(target, *numbers, start = start, end = middle - 1)
    elif numbers[middle] < target:
        return binary_search(target, *numbers, start = middle + 1, end = end)

  
usr_inp = input("Enter numbers separated by space with first number being the search target: ")
numbers = [int(number) for number in usr_inp.split(' ')]
target = numbers[0]
numbers.remove(target)
index_of_target = binary_search(target, *numbers)
if index_of_target < 0:
    print(f"{target} not found!")
else:
    print(f"Index of {target} is {index_of_target}")    