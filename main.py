from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1,algorithm2
from visualization import *

#x = [Rectangle(20,10),Circle(20),Square(6)]
#x = [Square(2),Square(2)]
x = [Circle(25),Square(15),Cone(10,9),Cone(20,3)]
c = Canvas(100,75)

result = algorithm2.run(c,x,True)
arr2png(result).show()