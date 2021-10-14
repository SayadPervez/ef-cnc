from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1,algorithm2
from visualization import *
from visualization import arr2png as a2p

x = [Circle(25),Square(15),Cone(10,9),Cone(20,3)]
c = Canvas(100,75)

result = algorithm1.run(c,x,log_=True,col=False)
arr2png(result).show()