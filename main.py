from functions import *
from shapes import Square
import constants as cont
from visualization import png2arr

sq = Square(50,30)

initialShapeArray = sq.shapeMatrix

ret_array = png2arr("./IMG/img.png")

print(initialShapeArray==ret_array)




