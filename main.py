from functions import *
from shapes import Circle, Rectangle, Square,Cone
import constants as cont
import visualization as vis

#cone = Cone(24,27) # -> type 2
#cone = Cone(30,5) # -> type 1
cone = Cone(173.2,100)
cone.displayShape()
#x = vis.arr2png(vis.rotate(cone.shapeMatrix,180)).show()