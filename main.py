from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1,algorithm2
from visualization import *
from visualization import arr2png as a2p

x = [Square(25),Square(15),Rectangle(10,5),Square(10),Rectangle(30,25),Square(15),Rectangle(40,50)]
c = Canvas(100,75)

result = algorithm2.run(c,x,log_=True,col=True)
arr2png(result).show()

