string = input("Enter string: ")
counter = {}
for char in string:
    if char in counter.keys():
        counter[char] += 1
    else:
        counter[char] = 1

print(counter)            