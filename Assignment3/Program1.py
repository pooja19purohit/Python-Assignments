__author__ = 'pooja'

def bunnyEars(n):
    if(n == 0 or n < 0):
        return 0
    elif(n % 2 == 0):
        return 3 + bunnyEars(n-1)
    elif(n % 2 != 0):
        return 2 + bunnyEars(n-1)

bunnies = int(input("enter the number of bunnies"))
ears = bunnyEars(bunnies)

print("number of ears is " + str(ears))