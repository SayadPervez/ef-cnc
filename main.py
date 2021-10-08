from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as cont
import visualization as vis
import algorithm1

canvas = Canvas(1300,1300)
rect = Rectangle(1300,1300)
rect2 = Rectangle(1,1)
#circle = Circle(650)

#allShapes = [rect,rect2,circle]
#allShapes = [rect,circle]
allShapes = [rect,rect2]
algorithm1.run(canvas,allShapes)