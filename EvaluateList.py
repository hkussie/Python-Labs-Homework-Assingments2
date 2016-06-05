#this program asses the variables in the list a
#any variable in the list that is less then 5 is taken and appended to a new
#list x, all other variables are printed to the user

a = [1,2,4,4,7,9,18,21]
x = []

for n in a:
    if n < 5:
        x.append(n)
        print(x)
    elif n > 5:
        print("The number is", n)
    else:
        print("The number is 5")

        
