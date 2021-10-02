from functions import *
from shapes import Circle, Rectangle, Square
import constants as cont
import visualization as vis

rect = Rectangle(40,20)
x = vis.rotate(rect.shapeMatrix,180)
y = rect.shapeMatrix

print(x==y)