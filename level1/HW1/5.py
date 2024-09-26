print("Enter Data below, or type 'quit' to stop.\n")
pairs = []
while True:
    
    price =  input("Price: ")
    if price == 'quit':
        break

    quality = input("Quality: ")
    if quality == 'quit':
        break
    
    price = int(price)
    quality = int(quality)    
    pairs.append((price, quality))
    print(f"({price}, {quality}) added.")

flag = 0
for pair1 in pairs:
    for pair2 in pairs:
        if pair1[0] < pair2[0] and pair1[1] >= pair2[1]:
            flag = 1
            break
    
    if(flag):
        break

if(flag):
    print("\n**Founded**")
else:
    print("\n**Not Found**")
