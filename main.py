from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as cont
import visualization as vis

canvas = Canvas(1300,1300)
rect = Rectangle(100,1350)
rect2 = Rectangle(100,2000)

d,ol=singleFit(canvas,[rect,rect2])
for _ in ol:
    print(d[_.uid])