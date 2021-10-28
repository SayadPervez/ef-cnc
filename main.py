from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1,algorithm2,algorithm4
from visualization import *
from visualization import arr2png as a2p
import time

shapeList = [Circle(5),Circle(5),Circle(5),Circle(5),Circle(5),Circle(5),Circle(5)]
c = Canvas(50,50)
s = time.time()
result = algorithm1.run(c,shapeList,log_=True,constCompute=75)
print(time.time()-s)
a2p(result).show()