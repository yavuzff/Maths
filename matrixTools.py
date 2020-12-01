#created for matrices revision

#2 by 1 matrix : [[2],[1]]
#1 by 2 matrix : [[3,2]]

def findDeterminant(matrix):
    #print (matrix,"matrix")
    
    #e.g. matrix [[36,-9],[-4,1]]
    if len(matrix) == 2:
        determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1]*matrix[1][0])

    #e.g. matrix [[3,1,4],[2,2,5],[-3,4,3]]
    elif len(matrix) == 3:
        
        first = matrix[0][0]*(findDeterminant([[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]))
        second = matrix[0][1]*(findDeterminant([[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]))
        third = matrix[0][2]*(findDeterminant([[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]))

        determinant = first - second + third
    else:
        determinant = None

    return determinant

def multiplyReciprocalDet(matrix,determinant):
    scalar = 1/determinant
    #print("scalar",scalar)
    
    newMatrix = [[str(j)+"/"+str(determinant) for j in i] for i in matrix]

    newMatrix = [[int(eval(j)) if eval(j).is_integer() == True else j for j in i ] for i in newMatrix ]
                 #[eval(j) for x in nested_list for d, y in enumerate(x) if d == 1]
    
    #newMatrix = [[j*scalar) for j in i] for i in matrix]
    
    return newMatrix

def minorsMatrix(matrix):
    newMatrix = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]

##    myMatrix = [[1,3,1],
##                [0,4,1],
##                [2,-1,0]]
    
    for row in range(0,3):
        for column in range(0,3):
            data = []
            for i in range (0,3):
                for j in range(0,3):
                    if i != row and j != column:
                        data.append(matrix[i][j])

            #converts the list len 4 to a 2d list
            matrix2x2 = [data[i:i+2] for i in range(0, len(data), 2)]
            
            #print ('2by2:',matrix2x2)
            minor = findDeterminant(matrix2x2)
            newMatrix[row][column] = minor
            
    return newMatrix


def cofactorsMatrix(matrix):
    index1 = [0,1,1,2]
    index2 = [1,0,2,1]

    for i in range (0,4):
        matrix[index1[i]][index2[i]] = -1 * matrix[index1[i]][index2[i]]

    return matrix

def transposeMatrix(matrix):
##    myMatrix = [[1,3,1],
##                [0,4,1],
##                [2,-1,0]]

    newMatrix = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range (0,3):
        newMatrix[i] = [matrix[0][i],matrix[1][i],matrix[2][i]]

    return newMatrix
    
def inverseMatrix(matrix):
    
    if len(matrix) == 2:
        determinant = findDeterminant(matrix)
        
        matrix[0][1] = -1 * matrix[0][1]
        matrix[1][0] = -1 * matrix[1][0]

        temp = matrix[0][0]
        matrix[0][0] = matrix[1][1]
        matrix[1][1] = temp

        inversedMatrix = multiplyReciprocalDet(matrix,determinant)


    elif len(matrix) == 3:

##        matrix = [[1,3,1],
##                  [0,4,1],
##                  [2,-1,0]]

        determinant = findDeterminant(matrix)
        print("Determinant:",determinant)

        if determinant != 0:
            matrixOfMinors = minorsMatrix(matrix)
            print("Minors:",matrixOfMinors)

            matrixOfCofactors = cofactorsMatrix(matrixOfMinors)
            print("Cofactors:",matrixOfCofactors)

            transposedMatrix = transposeMatrix(matrixOfCofactors)
            print("Transposed:",transposedMatrix)
            
            inversedMatrix = multiplyReciprocalDet(transposedMatrix,determinant)
            #print("Inversed:",inversedMatrix)

            print("Inversed:")
            outputMatrix(inversedMatrix)

        else:
            print("There is no inverse matrix as the determinant is 0.")
            inverseMatrix = None

    return inversedMatrix

def createMatrix(r,c):
    matrix = []
    for i in range (0,r):
        matrix.append([])
        for j in range(0,c):
            matrix[i].append(0)
    return matrix

def multiplyMatrix(m1,m2):

    nm = createMatrix(len(m1),len(m2[0]))
    
    for i in range (0,len(m1)):
        for k in range(0,len(m2[0])):
            newValue = 0
            for j in range(0,len(m1[i])):
##                print (m1[i][j]*m2[j][k])
                newValue = newValue + (m1[i][j]*m2[j][k])
##            print("NewValue",newValue)
            nm[i][k]= newValue
##            print(nm)
    return nm
    
def outputMatrix(matrix):
    width = 60
    stringMatrix = [[str(j) for j in i] for i in matrix]


##    print("Option 1:")
##    for i in stringMatrix:
##        print('\t|\t'.join(i).center(width))
##
##    print("\nOption 2:")
##    for i in stringMatrix:
##        print('\t|\t'.join(i))
##
##    print("\nOption 3:")
    for i in stringMatrix:
        print("  |  ".join(i).center(width))

def helpGeometrical():
    determinant = input("\nIs the determinant 0?\n")

    if determinant == 'y':
        print("\nThere is ONE point of intersection between the planes.")
        print("There is ONE solution.")
        print("The system of equations is CONSISTENT.")
        print("Use M^-1 * ANSWERS to find xyz matrix.")
        
    else:
        print("\nThere is either ZERO or INFINITE solutions.")
        parallel = input("\nAre any of the coefficients MULTIPLES?\n")

        if parallel == 'y':
            same = input("\nAre these equations the SAME (answer is multiple)?\n")

            if same == "y":
                print("\nAt least two planes fully OVERLAP")
                print("INFINITE solutions.")

            else:
                print("\nAt least 2 of the planes are PARALLEL.")
                print("Planes NEVER meet.")
                print("ZERO solutions.")

        else:
            print("\nCheck consistency by ELIMINATING a variable (subtract/add 1 and 2, then 2 and 3)")
            consistency = input("Are the equations SAME?\n")

            if consistency == "y":
                print("\nINFINITE solutions along a LINE - CONSISTENT.")
                print("Planes form a SHEAF")
                
            else:
                print("\nThere are ZERO solutions - INCONSISTENT.")
                print("Planes form a PRISM")

#stopped after here
def solveGeometrical(matrix,answerMatrix):
    determinant = findDeterminant(matrix)
    print("The determinant of this matrix is",determinant)
    
    if determinant!= None:
        if determinant  != 0:
            inversedMatrix = inverseMatrix(matrix)
            print(inversedMatrix)
            inversedMatrix = [[eval(str(x)) for x in y]for y in inversedMatrix]
            answer = multiplyMatrix(inversedMatrix, answerMatrix)

            print("\nThere is ONE point of intersection between the planes.")
            print("There is ONE solution.")
            print("The system of equations is CONSISTENT.")

            print("This point is:",answer)

        else:
            print("\nThere is either ZERO or INFINITE solutions.")

##            multiple = True
##
##            for i in range (0,len(matrix
        
    
#print (findDeterminant([[36,-9],[-4,1]]))

#print (findDeterminant([[12,5],[27,11]]))

#print (findDeterminant([[3,1,4],[2,2,5],[-3,4,3]]))
                                    
#outputMatrix(inverseMatrix([[1,2],[3,4]]))
