from functions import *
from shapes import Square
import constants as cont
from visualization import *

sq = Square(50,30)

initialShapeArray = sq.shapeMatrix
print(type(initialShapeArray))
image = arr2png(initialShapeArray,name_="") 
ret_array = png2arr("./IMG/img.png")
print(type(ret_array))
print(len(ret_array),len(ret_array[0]))
print(sq.shapeFrameDimension)
if initialShapeArray==ret_array:
    print(1)
else:
    print(0)






