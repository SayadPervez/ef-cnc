from cv2 import COLOR_BAYER_BG2BGR
from shapes import *
from visualization import *
from functions import *
import numpy as np

spe = Cone(20,12)

x = rotate(evenize(spe.shapeMatrix),45)

arr2png(x).show()