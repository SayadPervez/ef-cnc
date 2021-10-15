from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1,algorithm2
from visualization import *
from visualization import arr2png as a2p
import time

st = time.time()
x = [Square(25),Circle(8),Rectangle(10,5),Cone(12,15)]
c = Canvas(100,75)

result = algorithm2.run(c,x,log_=True,col=True)
en = time.time()
a2p(result).show()
print(en-st)