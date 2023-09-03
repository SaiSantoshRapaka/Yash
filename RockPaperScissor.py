import time
from random import *
dicti = {1 : "Rock", 2 : "Paper", 3 : "Scissor"}
choice = True
while choice == True:
    x = randint(1,3)
    UserChoice = input("Please enter you input: \n1:Rock\n2:Paper\n3:Scissor\n")
    try:
        UserChoice = int(UserChoice)
        if UserChoice in [1,2,3]:
            print('Your Choice is {}'.format(dicti[UserChoice]))
            time.sleep(3)   
            if x ==1:
                if UserChoice ==1:
                    print("Computer choice is {}. It is a Tie".format(dicti[x]))
                elif UserChoice ==2:
                    print("Computer choice is {}. You Won".format(dicti[x]))
                else:
                    print("Computer choice is {}. Computer Won".format(dicti[x]))
            elif x ==2:
                if UserChoice ==1:
                    print("Computer choice is {}. Computer Won".format(dicti[x]))
                elif UserChoice ==2:
                    print("Computer choice is {}. It is a Tie".format(dicti[x]))
                else:
                    print("Computer choice is {}. You Won".format(dicti[x]))
            elif x ==3:
                
                if UserChoice ==1:
                    print("Computer choice is {}. You Won".format(dicti[x]))
                elif UserChoice ==2:
                    print("Computer choice is {}. Computer Won".format(dicti[x]))
                else:
                    print("Computer choice is {}. It is a Tie".format(dicti[x]))
                
        else:
            time.sleep(3)
            print("Please enter valid input")
    except Exception as e:
        time.sleep(3)
        print("Please enter valid Integer Only")
        
            
            
    time.sleep(3)
    choice = input("Do you want to try again ? \nEnter Y for Yes (or) N for No\n")
    time.sleep(1)
    
    if choice[0].upper() == "Y":
        choice = True
    elif choice[0].upper() == "N":
        choice = False
    else:
        print("Please select yes or No")
        
        print("Thank you for playing !!!!")
        
    print("\n\n")