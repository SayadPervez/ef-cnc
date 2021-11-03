from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1,algorithm2,algorithm4,algorithm3
from visualization import *
from visualization import arr2png as a2p
import time

'''
shapeList = [Square(38),Rectangle(5,15)]
c = Canvas(50,50)
s = time.time()
result = algorithm3.run(c,shapeList,log_=True,constCompute=75)
print(time.time()-s)
a2p(result).show()
'''
'''
shapeList = [Square(38),Rectangle(5,15),Cone(20,8),Cone(25,10),Cone(20,12),Circle(10)]
sortedShapeList = triangleSort(shapeList)
coneCount = countShapes(sortedShapeList,'cone')
ones = [(-1)**i for i in range(coneCount)]
for q in range(coneCount):
    sortedShapeList[q].flaTilt(ones[q])

for _ in sortedShapeList:
    _.displayShape()
    input("...")
'''

sl = [Circle(10),Cone(20,8),Cone(20,8),Cone(20,8),Cone(20,12),Square(5),Cone(20,8),Cone(20,12)]
cv = Canvas(100,100)
s = time.time()
result = algorithm3.run(cv,sl,log_=True,constCompute=75)
print(time.time()-s)
a2p(result).show()