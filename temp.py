from shapes import *
from visualization import *
from functions import *
import numpy as np

def binaryFilter(canvas):
    a = np.array(canvas)
    a[a==1]=1
    a[a!=1]=0
    return((np.array(a,int)).tolist())

