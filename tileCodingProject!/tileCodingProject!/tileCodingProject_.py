from pylab import zeros, sin, cos, normal, random
from Tilecoder import numTilings, tilecode

# initialize weights appropriately here
weight = [0,0] * 968
# initialize step size parameter appropriately here
alpha = 0.1/numTilings
# initialize your global list of tile indices here
tileIndices = [-1]*numTilings
    
def f(x,y):
    # write your linear function approximator here (5 lines or so)
    tilecode(x, y, tileIndices)
    f = 0
    for i in range (0, numTilings):
        index = tileIndices[i]
        index = int(index)
        f = f + weight[index]
    return f
   
def learn(x,y,target):
    # write your gradient descent learning algorithm here (3 lines or so)
    tilecode(x, y, tileIndices)
    F = f(x, y)
    for i in range (0, numTilings):
        index = tileIndices[i]
        index = int(index)
        weight[index] = weight[index] + alpha * (target - F)

def test1():
   for x,y,target in \
         [ (0.1, 0.1, 3.0), \
           (4.0, 2.0, -1.0), \
           (5.99, 5.99, 2.0), \
           (4.0, 2.1, -1.0) ]:
        before = f(x,y)
        learn(x,y,target)
        after = f(x,y)
        print 'Example (', x, ',', y, ',', target, '):', 
        print '    f before learning: ', before, 
        print '    f after learning : ', after
    
def targetFunction(x,y):
    return sin(x-3.0)*cos(y) + normal(0,0.1)

def train(numSteps):
    for i in range(numSteps):
        x = random() * 6.0
        y = random() * 6.0
        target = targetFunction(x,y)
        learn(x,y,target)
    
def writeF(filename):
    fout = open(filename, 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            target = f(i * 6.0/steps, j * 6.0/steps)
            fout.write(repr(target) + ' ')
        fout.write('\n')
    fout.close()
        
def MSE(sampleSize):
    totalSE = 0.0
    for i in range(sampleSize):
        x = random() * 6.0
        y = random() * 6.0
        error = targetFunction(x,y) - f(x,y)
        totalSE = totalSE + error * error
    print 'The estimated MSE: ', (totalSE / sampleSize)
    
def test2():
    train(20)
    writeF('f20')
    MSE(10000)
    for i in range(10):
        train(1000)
        MSE(10000)
    writeF('f10000')

test1()

