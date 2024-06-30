#importation
import random

# Title 
mode = input("Guess The Number Game (either say yes or ok): ")

if mode == "yes":
    num1 = random.randint(0,10)
    g1 = 0
    while g1 != num1:
        g1 = int(input("Guess a Number between 0-10: "))
        
        if g1 < num1:
            print("Guess higher!")
        elif g1 > num1:
            print("Guess lower!")
        else:
            print("yep! you got it! \n Thanks For Playing!")

elif mode == "ok":
    num2 = random.randint(0,50)
    g2 = 0
    while g2 != num2:
        g2 = int(input("Guess a Number between 0-50: "))
            
        if g2 < num2:
            print("Guess higher!")
        elif g2 > num2:
            print("Guess lower!")
        else:
            print("yep! you got it! \n Thanks For Playing!")

# end of code :)
    