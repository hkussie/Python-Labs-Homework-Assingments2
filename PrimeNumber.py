number = int(input("Enter a number here: "))
possible_numbers = [n for n in range(2, number) if number%n == 0]
if number == 1:
    print("One isn't a prime number.")
elif not possible_numbers:
    print("This number is a prime number.")
else:
    print("This isn't a prime number.") 
