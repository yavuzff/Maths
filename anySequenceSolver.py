#USES RECURSION TO SOLVE ANY SEQUENCE
#(BUT FLOATING POINT ERRORS AFTER AROUND POWER 14)
#CREATED BY YAVUZ AFTER AN INTERESTING YEAR 10 SEQUENCES LESSON

def createSequence():#gets the sequence from the user
    s = []
    size = int(input("Please enter the amount of elements in the sequence: "))#first one is separate to output 'first'  s.append(add)
    for i in range (size):
        add = int(input("Please enter the next number in the sequence: "))#loops 4 more times to get 5 elements
        s.append(add)
    return s

def linearSeq(s): #finds the nth term of a linear sequence
    x = s[1] - s[0] #x is the difference between consecutive elements
    y = s[1] - x * 2 # y is the number we need to add to x*n to get the element
    if y == 0:
        ans = str(x) + "n" #doesnt have y if y is 0
    elif y > 0:
        ans = str(x) + "n + " + str(y)
    else:
        y = -y #converts y to a positive number if it is negative
        ans = str(x) + "n - " + str(y) #and minuses the positive number away
    return answer

def findDiff(d): #finds the difference between each term of a sequence
    diff = []
    for i in range (0,len(d)-1): #loops through each term, compares it to next one
        diff.append(d[i+1] - d[i])
        
    return diff


def solveSequence(seq):
    #inputs a sequence, finds the highest power term in the nth term,
    #then calls itself with the 'rest' sequence
    #to find the next highest power in the nth term
    #base case: repeats until all the differences are same(linear term)
    
    global answer, lastNum #keeps on adding to answer
    
    if all(i == seq[0] for i in seq): #base case, checks if all the terms are same
        lastNum = str(seq[0]) #if they are the linear term is returned
        return lastNum
    
    
    diff = findDiff(seq) #the difference between each term is received
    countDiff = 1 #the nth difference that is being checked
    fact = 1 #the constant difference is divided by the factorial of countdiff to get coefficent
    
    Found = False
    while not Found: #loops until the constant difference is found
        
        if all(i == diff[0] for i in diff): #checks if difference is constant
            Found = True #can leave the loop next time

        else: #if not constant
            diff = findDiff(diff) #find the next difference
            countDiff = countDiff + 1 #the nth difference increases

    
    for i in range (1,countDiff +1): #calculates factorial of nth difference
        fact = fact * i
                    
    coefficient = diff[0] / fact
    #the coefficient of the first term is the constant difference/factorial of nth difference

    ans = str(coefficient) + "n^" + str(countDiff) + " + "
    answer = answer + ans #the next part of ans is added to the final answer

    answerN = [] #the sequence made by this term is calculated
    for i in range (1,len(seq)+1):
        answerN.append(coefficient * i ** int(countDiff))
            
    rest = [] #the sequence needed on top of this sequence i.e. rest is calculated
    for i in range (0,len(seq)):
        rest1 = seq[i] - answerN[i]
        rest.append(rest1)
        
    solveSequence(rest) #the function is called again using the rest sequence

    

sequence = []

#User input based sequence - takes too long
#sequence = createSequence()


#PRE WRITTEN SEQUENCE
for i in range (1,15):
    sequence.append(21*i**12 - 787*i**10 + 21*i**9 - 65*i**8 - 9*i**7 + 87*i**6 + 11*i**5 + 4*i**4 + 7*i**3 + 1*i**2 + 5*i - 11 )
    #change/add/get rid of values as shown above
    

#print (sequence)

answer = ""
lastNum = 0

solveSequence(sequence)

answer = answer + lastNum
print ("Final answer:", answer)

