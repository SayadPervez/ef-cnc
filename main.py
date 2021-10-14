from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1
from visualization import *

#x = [Rectangle(2,1),Circle(2),Square(1)]
x = [Circle(2),Circle(2)]
c = Canvas(15,15)

result = algorithm1.run(c,x)
#print(result)
arr2png(result).show()