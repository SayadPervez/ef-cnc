from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1,algorithm2
from visualization import *
from visualization import arr2png as a2p
import time

st = time.time()
x = [Square(250),Circle(80),Rectangle(100,50),Cone(120,150)]
c = Canvas(1000,750)

result = algorithm2.run(c,x,log_=True,col=True,constCompute=10)
en = time.time()
a2p(result).show()
print(en-st)