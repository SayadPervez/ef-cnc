from functions import *
from shapes import Circle, Rectangle, Square,Cone
import constants as cont
import visualization as vis

cone = Cone(24,27) # -> type 2
#cone = Cone(30,5) # -> type 1
#cone = Cone(17.32,10) # -> 180 deg cone
cone.displayShape()
vis.arr2png(vis.rotate(evenize(cone.shapeMatrix),17)).show()