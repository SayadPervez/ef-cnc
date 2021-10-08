from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as cont
import visualization as vis

canvas = Canvas(1300,1300)
rect = Rectangle(100,1350)

print(singleFit(canvas,rect))