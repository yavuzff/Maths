#all numerical methods for aqa further maths
#outputs x and yvalues to help with working

import math

#dy/dx = f(x)
def f(x,y=None): #change function before running program #math.log(x,base=e) for logs
    return math.sqrt(x**2+y+1)

def inputData(): #inputting values
    print('Enter min x value:')
    lower = float(input('>'))

    print('Enter max x value:')
    upper = float(input('>'))

    print('Enter number of strips:')
    n = float(input('>'))

    return lower,upper,(upper-lower)/n

#NUMERICAL METHODS FOR DIFFERENTIATION:IN
#Euler's method both original and improved version:

def inputDataE(): #inputting values for eulers method
    print('Enter value of x:')
    firstx = float(input('>'))

    print('Enter corresponding y:')
    firsty = float(input('>'))

    print('Enter x value for desired y:')
    target = float(input('>'))

    print('Enter step size (h): ')
    h = float(input('>'))
    return firstx,firsty,target,h


def euler(): #normal eulers method
    firstx,firsty,target,h = inputDataE()
    values = [[firstx],[firsty],[]]

    while values[0][-1] < target:
        try:
            new = f(values[0][-1])
        except:
            new = f(values[0][-1],values[1][-1])
        values[2].append(new)
        values[0].append(values[0][-1]+h)
        newy = values[1][-1] + h*new
        values[1].append(newy)

    print('x-values:',values[0])
    print('y-values:',values[1])
    print('f(x):',values[2])
    return values[1][-1]
    
    
def improved(): #improved eulers method
    firstx,firsty,target,h = inputDataE()
    values = [[firstx],[firsty],[]]

    #first step is normal euler:
    try:
        new = f(values[0][-1])
    except:
        new = f(values[0][-1],values[1][-1])

    values[2].append(new)
    values[0].append(values[0][-1]+h)
    newy = values[1][-1] + h*new
    values[1].append(newy)

    #now comes improved euler

    while values[0][-1] < target:
        try:
            new = f(values[0][-1])
        except:
            new = f(values[0][-1],values[1][-1])
        values[2].append(new)
        values[0].append(values[0][-1]+h)
        newy = values[1][-2] + 2*h*new
        values[1].append(newy)

    print('x-values:',values[0])
    print('y-values:',values[1])
    print('f(x):',values[2])
    return values[1][-1]
        

#NUMERICAL METHODS FOR INTEGRATION:

def generateOrdinates(lower,upper,h): #generates ordinates given lower and upper bound, and step length
    ordinates = [lower]
    total = lower

    for i in range (int((upper-lower)/h)):
        total+=h
        ordinates.append(total)

    return ordinates


def midordinate(): #using midordinate rule to estimate
    lower,upper,h = inputData()

    ordinates = generateOrdinates(lower,upper,h) #ordinates created

    midordinates = []

    for i in range (0,len(ordinates)-1):#midordinates created
        mid = (ordinates[i] + ordinates[i+1]) / 2
        midordinates.append(mid)

    total = 0
    vals = []
    for i in midordinates:# the values at each is summed
        x = f(i)
        total += x
        vals.append(x)

    print('ordinates:',ordinates)
    print('midordinates:',midordinates)
    print('values',vals)
    
    return total*h #approximation returned


def simpsons(): #simpsons rule to approximate, more accurate than midordinate
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

    print('ordinates:',ordinates)
    print('values:',values)
        
    return (1/3)*h*total #return using rest of formula
    


    
