#yavuz 2018
#converts any denary number to its equivalent value in any base

while True:
    #denaryNo = int(input("Enter the value in denary that you want to convert: "))
    print("Enter the value in denary that you want to convert: ")
    denaryNo = int(input('>'))
    print("Enter the base that the number will be converted in to: ")
    newBase = int(input('>'))

    modArray = []
    convertedNo = ''

    while denaryNo != 0: #loops until the value is 0
        modArray.append(denaryNo % newBase) #the remainder is added 
        denaryNo = denaryNo // newBase #integer division
    #print (modArray)

    for i in range (0,len(modArray)):
        convertedNo = convertedNo + str(modArray[len(modArray)-1-i]) 
        
    print (convertedNo)
