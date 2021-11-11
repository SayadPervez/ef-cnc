from shapes import *
from visualization import *
from functions import *
import numpy as np

'''
spe = Cone(20,12)

x = rotate(evenize(spe.shapeMatrix),70)

arr2png(x).show()

'''
spe = Cone(20,12)

x = rotate(evenize(outline_with_shape(spe.shapeMatrix,20)),70)

arr2png(x).show()
