import numpy as np  
from PIL import Image as im

def arr2png(arr):
    l,b=np.shape(arr)
    ar=np.zeros((l,b,3),dtype=np.uint8)
    a=np.array(arr, dtype=str)
    ar0=ar[:,:,0]
    ar1=ar[:,:,1]
    ar2=ar[:,:,2]
    #white
    ar0[a=='0']=255
    ar1[a=='0']=255
    ar2[a=='0']=255
    #red
    ar0[a=='r']=255
    #blue
    ar2[a=='b']=255
    #green
    ar1[a=='g']=255
    #magenta
    ar0[a=='m']=255
    ar2[a=='m']=255
    
    ar[:,:,0]=ar0
    ar[:,:,1]=ar1
    ar[:,:,2]=ar2
    img=im.fromarray(ar,'RGB')
    img.save('./IMG/img.png')
    return(img)

