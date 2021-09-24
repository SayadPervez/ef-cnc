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
    
def png2arr(img):
    ar=np.array(img,dtype='int64')
    print(np.shape(ar))
    l,b,h=np.shape(ar)
    a=np.zeros((l,b),dtype=str)
    ar_avg=np.zeros((l,b),dtype='int64')
    ar0=ar[:,:,0]
    ar1=ar[:,:,1]
    ar2=ar[:,:,2]
    ar_avg=(ar0+ar1+ar2)//3
    
    #red
    a[ar0==255 ]='r'
    #blue
    a[ar2==255]='b'
    #green
    a[ar1==255]='g'
    #white
    a[ar_avg==255]=0
    #black
    a[ar_avg==0]=1
    #magenta
    a[ar_avg==170]='m'
    a=a.tolist()
    for i,x in enumerate(a):
        for j,e in enumerate(x):
            if e=='0':
                a[i][j]=0
            if e=='1':
                a[i][j]=1

    return a

