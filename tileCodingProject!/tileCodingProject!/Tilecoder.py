import numpy


#globals
numTilings = 8
numGridSquares = 10
smallGridTotal = 6
tileMovementValue = -0.6/8


    

#say 4 and 2
def tilecode(x,y,tileIndices):
    #Get amount of division.
    ySpacing = smallGridTotal / numGridSquares
    xSpacing = smallGridTotal /numGridSquares
    
    #This constant starts at zero and represents the movement of the tilings. 
    movementConstant = 0
    print 192192
    print 32131232123123
    for i in range (0,7):

        xcoord = 0
        ycoord = 0 

        movementConstant = i * tileMovementValue
        print "spaaaaaace", ySpacing, xSpacing 
        xcoord = x/(xSpacing + movementConstant)
        ycoord = y/(ySpacing + movementConstant)

        index = ycoord * 11 + xcoord
        print index
        tileIndices[i] = index

  
   



def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
