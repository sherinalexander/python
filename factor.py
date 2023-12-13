number = int(input("Enter a number to find out factors: "))

if number > 0:
    print("Factors of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
else:
    print("Error: Please enter a positive number.")
