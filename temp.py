from shapes import *
from visualization import *
from functions import *
import numpy as np

sq = Square(6)
sq.shapeMatrix = outline_with_shape(sq,3)
sq.displayShape()
input("")
sq.shapeMatrix=rotate(sq,45)
sq.displayShape()