from functions import *
from shapes import Square
import constants as cont
from visualization import *

sq = Square(50,30)

initialShapeArray = sq.shapeMatrix

ret_array = png2arr("./IMG/img.png")

print(len(ret_array),len(ret_array[0]))
print(sq.shapeFrameDimension)






