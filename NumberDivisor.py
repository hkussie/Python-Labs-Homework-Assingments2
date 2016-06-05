#this program asks the user to enter a number
#the program then returns all of the divisors of that number 

number = int(input("Enter a number here: "))

number_range = range(1, number)
divisor_list = []
for n in number_range:
    if number % n == 0:
        divisor_list.append(n)
    print(divisor_list)
