#Euler's method both original and improved version:

import math

#dy/dx = f(x)
def f(x,y=None): #change function before running program
    #math.log(x,base=e) for logs
    return x+3+math.sin(y)

def inputData(): #inputting values
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
    firstx,firsty,target,h = inputData()
    values = [[firstx],[firsty],[]]

    while values[0][-1] < target:
        try:
            new = f(values[0][-1])
        except:
            new = f(values[0][-1],values[1][-1])
            
        values[0].append(values[0][-1]+h)
        newy = values[1][-1] + h*new
        values[1].append(newy)

    return values[1][-1]
    
    
def improved(): #improved eulers method
    firstx,firsty,target,h = inputData()
    values = [[firstx],[firsty],[]]

    #first step is normal euler:
    try:
        new = f(values[0][-1])
    except:
        new = f(values[0][-1],values[1][-1])
            
    values[0].append(values[0][-1]+h)
    newy = values[1][-1] + h*new
    values[1].append(newy)

    #now comes improved euler

    while values[0][-1] < target:
        try:
            new = f(values[0][-1])
        except:
            new = f(values[0][-1],values[1][-1])

        values[0].append(values[0][-1]+h)
        newy = values[1][-2] + 2*h*new
        values[1].append(newy)

    return values[1][-1]
        
