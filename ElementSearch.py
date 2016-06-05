#this program evaluates the content in the list a
#if the user entered number is bigger then 5, it is added to the list 

a = [1,2,3,4,5]

def element_search(n):
    if n > 5:
         print("This number is large enough to go in the list, the list is now: ", a)
    elif n < 5:
         print("The number is to small to go into the list")
     else:
         print("Enter a number")

         
