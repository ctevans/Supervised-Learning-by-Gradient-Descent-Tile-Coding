import numpy
import math

#globals
numTilings = 8 
numGridSquares = 10.0
smallGridTotal = 6.0
tileMovementValue = -0.6/8


    

#say 4 and 2
def tilecode(x,y,tileIndices):
    #Get amount of division.
    ySpacing = smallGridTotal / numGridSquares
    xSpacing = smallGridTotal /numGridSquares
    
    print ySpacing
    print xSpacing
    #This constant starts at zero and represents the movement of the tilings. 
    movementConstant = 0


    for i in range (0,8):
        ycoord = 0
        xcoord = 0

        
        index = i* 121
        movementConstant = i * tileMovementValue

        xcoord = (x- movementConstant)/xSpacing   
        ycoord = (y- movementConstant)/ySpacing
        

        xcoord= math.floor(xcoord)
        ycoord= math.floor(ycoord)

        print xcoord, " xcoord " , ycoord, " y coord"  

        index = index + ( ycoord * 11 + xcoord)
        tileIndices[i] = index

  
   



def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)

printTileCoderIndices(6.0,6.0)

printTileCoderIndices(1019191.0,12919221.0)