def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
        
    return 1    

interval_lower = int(input("Enter interval lower: "))
interval_upper = int(input("Enter interval upper: "))
if interval_lower <= interval_upper:
    for number in range(interval_lower, interval_upper + 1):
        if is_prime(number):
            print(number, end=' ')

else:
    print("Invalid input")