#numerical methods for integration
import math

def f(x): #add the function here
    return math.sqrt(1+x**3)

    
def inputData(): #inputting values
    print('Enter min x value:')
    lower = float(input('>'))

    print('Enter max x value:')
    upper = float(input('>'))

    print('Enter number of strips:')
    n = float(input('>'))

    return lower,upper,(upper-lower)/n

def midordinate(): #using midordinate rule to estimate
    lower,upper,h = inputData()

    ordinates = generateOrdinates(lower,upper,h) #ordinates created

    midordinates = []

    for i in range (0,len(ordinates)-1):#midordinates created
        mid = (ordinates[i] + ordinates[i+1]) / 2
        midordinates.append(mid)

    total = 0
    for i in midordinates:# the values at each is summed
        total += f(i)

    return total*h #approximation returned

def generateOrdinates(lower,upper,h): #generates ordinates given lower and upper bound, and step length
    ordinates = [lower]
    total = lower

##    while total<upper:
##        total += h
##        ordinates.append(total)
##    return ordinates
    #code commented out above can sometimes go overboard due to rounding downs in floating point errors
    for i in range (int((upper-lower)/h)):
        total+=h
        ordinates.append(total)

    return ordinates

def simpsons(): #simpsons rule to approximate, more accurate than midordinate
    lower,upper,h = inputData()

    ordinates = generateOrdinates(lower,upper,h) #ordinates created
    
    values = [] #values of these stored

    for i in ordinates:
        values.append(f(i))

    total = 0
    
    for i in range (0,len(values)):
        if i == 0 or i == len(values)-1: #if first or last element
            total += values[i] #simply add
        elif i%2 == 1: #if odd indexed element
            total += 4*values[i] #multiply by 4 then add
        else: #if even indexed
            total += 2*values[i] #multiply by 2

    return (1/3)*h*total #return using rest of formula
    


    
