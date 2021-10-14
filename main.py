from functions import *
from shapes import Canvas, Circle, Rectangle, Square,Cone
import constants as const
import algorithm1
from visualization import *

#x = [Rectangle(2,1),Circle(2),Square(1)]
#x = [Square(2),Square(2)]
x = [Circle(25),Square(15),Cone(10,9),Cone(20,3)]
c = Canvas(100,75)

result = algorithm1.run(c,x)
#print(result)
import time
time.sleep(2)
arr2png(result).show()