from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1

x = [Rectangle(2,1),Circle(1),Square(1)]
y = [_.uid for _ in x]
z = sortSurfaceArea(x)

for _ in z:
    print(_.myShape)