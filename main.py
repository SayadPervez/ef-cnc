from functions import *
from shapes import Square
import constants as cont

agl = 90

sq = Square(150)

print("angle - ",agl)

print("Before tilting : ",end="")
print(sq.shapeFrameDimension)

sq.tilt(agl)

print("After tilting : ",end="")
print(sq.shapeFrameDimension)


