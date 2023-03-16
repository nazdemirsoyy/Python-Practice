c0 = int(input("Enter a non-negative, non-zero integer number: "))

while c0 <= 0:
    print("Invalid input. Please enter a non-negative, non-zero integer number.")
    c0 = int(input("Enter a non-negative, non-zero integer number: "))

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)



 

