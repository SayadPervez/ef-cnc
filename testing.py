from functions import *
from shapes import *
import algorithm1,algorithm2,algorithm3,algorithm4
import constants as const
from visualization import *
'''
const.sampl=1

print("\na1-S starting:")
canvas = Canvas(200,100)
shapes = [ 
            Square(20) ,
            Rectangle(35,25) , 
            Circle(7) ,
            Cone(17,20) ,
            Cone(12,4)
        ]

for shape in shapes:
    shape.shapeMatrix = outline_with_shape(shape,3)

c = canvas
li = shapes
print("Starting algorithm1")
out = binaryFilter(algorithm1.run(c,li,log_=True,constCompute=50))
print("Lowlevel rendering completed")
#arr2png(out).show()

const.sampl=10

canvas = Canvas(200,100)
shapes = [ 
            Square(20) ,
            Rectangle(35,25) , 
            Circle(7) ,
            Cone(17,20) ,
            Cone(12,4)
        ]
'''

sq = Cone(50,20,20)
#sq.shapeMatrix = outline_with_shape(sq,3)
sq.displayShape()
print(sq)
sq.tilt(20)
print(sq)
sq.displayShape()