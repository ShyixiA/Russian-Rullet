import random
import random
from traceback import print_tb

print("----RUSSIAN RULLET----")

bullet = random.randrange(1, 7)

select = int()
Counter = 0
try:
    while select != bullet:
        
        Counter=Counter +1
        select = int(input("Try not to find the bullet : "))

        if select == bullet:
            if Counter==1:
                print("Unlucky Try AgaiN..")
            elif Counter==2: 
                print("Next Time My Friend..")
            elif Counter==3:
                print("Try Again...")
            elif Counter==4:
                print("You Are Close Continue..")     
            elif Counter==5:
                print("Very Good:D ")      
            elif Counter==6:
                print("PERFECT You Win")   
                   
                
        elif select > 6:
            print("The number you entered is incorrect, please try again.")
        elif select < 1:
            print("The number you entered is incorrect, please try again.")
            
        else:
            if Counter==1:
                print("İt was easy")
            elif Counter==2: 
                print("Luck")
            elif Counter==3:
                print("Pretentious")
            elif Counter==4:
                print("That's it")     
            elif Counter==5:
                print("You are great")      
            elif Counter==6:
                print("Best Score")     
            elif Counter==7:
                print("There is a penalty for always entering the same numbers. YOU LOST")
                break

                
except:
    print("The number you entered is incorrect, please try again.")
