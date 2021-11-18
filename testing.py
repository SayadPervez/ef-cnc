from functions import *
from shapes import *
import algorithm1,algorithm2,algorithm3,algorithm4
import constants as const
from visualization import *
from ezdxf import recover
from ezdxf.addons.drawing import matplotlib

def invertColor(imgarray):
    x = np.array(imgarray,dtype=str)
    x[x=='0']=1
    x[x=='m']=1
    x[x=='']=0
    return(typeToggle2d(x.tolist()))



arr2png(dxf2arr('./IMG/c100.dxf')).show()