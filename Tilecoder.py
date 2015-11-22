import math

#globals
numTilings = 8 
numGridSquares = 10.0
smallGridTotal = 6.0
tileMovementValue = -0.6/8
   

def tilecode(x,y,tileIndices):
    #This constant starts at zero and represents the movement of the tilings. 
    movementConstant = 0

    for i in range (0,numTilings):
        
        index = i* 121
        movementConstant = i * tileMovementValue

        xcoord = (x- movementConstant)/0.6  
        ycoord = (y- movementConstant)/0.6
        

        xcoord= math.floor(xcoord)
        ycoord= math.floor(ycoord)


        index = index + ( ycoord * 11 + xcoord)
        tileIndices[i] = int(index)
    
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
