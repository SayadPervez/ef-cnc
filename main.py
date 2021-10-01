from functions import *
from shapes import Circle, Rectangle, Square
import constants as cont
import visualization as vis

rect = Rectangle(40,20)
x = vis.rotate(rect.shapeMatrix,80)
'''
print(len(x),len(x[0]))
print(len(rect.shapeMatrix),len(rect.shapeMatrix[0]))
print(x==rect.shapeMatrix)
'''
vis.arr2png(x).show()