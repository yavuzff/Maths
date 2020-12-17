#program that shows how the ratio between consecutive pairs of
#fibonacci numbers approaches the golden ratio

#The original image produced by this graph is called fibonacciRatioGraph

import matplotlib.pyplot as plt

def fibonacci(n): #function that returns the first n fibonacci numbers
    if n == 1:
        return [1] #return first number
    
    elif n == 2:
        return [1,1] #return first two numbers
    
    else: #if larger than 3
        num1 = 1  #starting numbers
        num2 = 1
        fibonacci = [1,1] 

        for i in range (0,n-2): #loops n-2 times as the list already has 2 nums
            new = num1+num2 #the new num is the total of the previous 2
            fibonacci.append(new)
            num1 = num2 #the last two are updated
            num2 = new

        return fibonacci

def otherSequence(n):
    if n == 1:
        return [3] #return first number
    
    elif n == 2:
        return [3,7] #return first two numbers
    
    else: #if larger than 3
        num1 = 3  #starting numbers
        num2 = 7
        seriesNum = [3,7] 

        for i in range (0,n-2): #loops n-2 times as the list already has 2 nums
            new = num1+num2 #the new num is the total of the previous 2
            seriesNum.append(new)
            num1 = num2 #the last two are updated
            num2 = new

        return seriesNum
    

def ratio(series): #return the ratio between consecutive elements of a series
    ratio = []
    for i in range (1,len(series)): #loops by starting from 1
        #appends the ith/i-1th element
        ratio.append(series[i]/series[i-1])
        
    return ratio

def drawFibo(x,y): #function to draw the fibonacci graph
    
    plt.plot(x,y,color='red',label = 'Fibonacci Numbers Ratio') #the points are plotted
    plt.xlabel('Pair Index') #axis are labelled
    plt.ylabel('Ratio')
    plt.title('Ratio between consecutive numbers of a Fibonacci-like sequence')
    plt.axis(xmin=0,xmax=25) # the x-axis max is 30


GOLDEN = 1.6180339887498948482045868343656381177203091798057628621354486227052604628189024497072072041893911374
#^golden ratio to 100 d.p.

n = 41 #51 numbers used to get 50 ratios

series = fibonacci(n) #series is formed
numRatio = ratio(series) #the ratio between the numbers formed

goldenLine = [GOLDEN]*len(numRatio) #the y values for the graph are all the golden ratio 
index = range(len(numRatio)) #the x values are the index of the numbers

randomSeq = otherSequence(n) #a different sequence using the fibonacci sequence rule is formed
ratioRandom = ratio(randomSeq) #the ratio of this sequence is stored

plt.plot(index,goldenLine,color = 'gold',label='Golden ratio') #the golden ratio graph is plotted
plt.plot(index,ratioRandom,color = 'green',label='Fibonacci but starts with 3,7 Ratio') #the random sequence graph is plotted
drawFibo(index,numRatio) #the fibonacci ratio is plotted

handles, labels = plt.gca().get_legend_handles_labels() #the handles and labels of the graphs are received
order = [0,2,1] #the order of the labels are changed
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order]) #the legend is formed with the order

plt.show() #outputs the graph

