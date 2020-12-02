#THIS PROGRAM HELPS TO IMPROVE YOUR MENTAL MATHS
#IT WILL GIVE YOU A CUBE OF NUMBERS BETWEEN 1-100
#YOU WILL NEED TO ENTER THE ORIGINAL NUMBER
#AND IT TELLS YOU THE TIME IT TOOK YOU TO SOLVE IT

import random                                                   #importing the random library to choose a random number
import time                                                     #importing time library to find the amount of time it took to answer 

def createList(n):                                              #function that stores the values for a chosen power for every number between 1 and 100
    numberList = []
    for i in range (1,101):                                     #loops through every number between 1 and 100
        numberList.append(i**n)                                 #adds its cube to the list
    return numberList                                           #returns the final numbers

def askNumber(givenList):                                       #function that chooses a random cube number and checks the answer
    randomNumber = random.randint(0,99)                         #chooses a random number
    number = str(givenList[randomNumber])                       #random number converted to string to avoid using multiple data types in the answer
    start = time.time()                                         #time before the input is taken
    answer = input("Find the cube root of: "+ number + "\n")
    end = time.time()                                           #time after the input is taken
    totalTime = end -  start                                    #time it took to type the input
    if answer == '':                                            #if input is empty
        return True                                             #quit the subroutine
    answer = int(answer)
    if answer**3 == givenList[randomNumber]:
        print("Right answer. It took you",totalTime," sseconds.\n")
    else:
        rightAnswer = round(givenList[randomNumber]**(1/3))     #right answer is the random number to the power of a third(cuberoot) and is rounded 
        print("Wrong answer. The right answer was",rightAnswer,"\nIt took you",totalTime,"seconds.\n")



#--------------------------------MAIN PROGRAM----------------------------------------------------------------------------------------------------------------------------------------------------------#

input("This program will help you improve your mental maths skills.\nIt will give you the cube of a number between 1 and 100.\nYou will have to guess what number cubed makes that number.\nYou will also be given the amount of time it took you to find that number.\nPress enter when you want to quit.\nPress enter to start:")

power = 3                               #chosen power is 3
cubeNumbers = createList(power)         #calls function to find all cube numbers between 1 and 100
end = False                             #end shows if the user doesnt want to continue or not
while end == False:
    if askNumber(cubeNumbers) == True:  #calls the function to ask a number and if the answer is just enter then end becomes true
        end = True



