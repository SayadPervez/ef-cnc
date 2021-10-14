from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1,algorithm2
from visualization import *
from visualization import arr2png as a2p

sq = Cone(10,2)
print(sq.shapeFrameDimension)
a2p(sq).show()

input("Waiting for it ...")

sq.tilt(15)
print(sq.shapeFrameDimension)
a2p(sq).show()