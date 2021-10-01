from functions import *
from shapes import Circle, Rectangle, Square
import constants as cont
import visualization as vis

rect = Rectangle(20,6)
#rect.displayShape()
x = vis.rotate(rect.shapeMatrix,360)
print(len(x),len(x[0]))
print(len(rect.shapeMatrix),len(rect.shapeMatrix[0]))







