from functions import *
from shapes import Rectangle, Square
import constants as cont
from visualization import *

sq = Rectangle(50,20,90)

initialShapeArray = sq.shapeMatrix
print(type(initialShapeArray))
image = arr2png(initialShapeArray,name_="") 
ret_array = png2arr("./IMG/img.png")
print(type(ret_array))
print(len(ret_array),len(ret_array[0]))
print(sq.shapeFrameDimension)
print(initialShapeArray==ret_array)
