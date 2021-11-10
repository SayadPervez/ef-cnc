import numpy as np  
from PIL import Image as im
import cv2 as cv
from constants import *
import matplotlib.pyplot as plt

def arr2png(arr,name_=""):
    if("shapes" in str(type(arr))):
        arr=arr.shapeMatrix
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
    #pale black
    ar0[a=='0.7']=15
    ar1[a=='0.7']=15
    ar2[a=='0.7']=15

    ar[:,:,0]=ar0
    ar[:,:,1]=ar1
    ar[:,:,2]=ar2
    img=im.fromarray(ar,'RGB')
    if(name_==""):
        img.save('./IMG/img.png')
    else:
        img.save(str(name_)+".png")
    return(img)

def png2arr(img_path):
    img = im.open(img_path)
    ar=np.array(img,dtype='int64')
    s=np.shape(ar)
    a=np.zeros((s[0],s[1]),dtype=str)
    ar_avg=np.zeros((s[0],s[1]),dtype='int64')
    if len(s)==3:
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
        #pale black
        a[ar_avg==15]='0.7'
    if len(s)==2:
        a[ar==0]='1'   
    a=a.tolist()
    for i,x in enumerate(a):
        for j,e in enumerate(x):
            if e=='0':
                a[i][j]=0
            if e=='1':
                a[i][j]=1
            if e=='0.7':
                a[i][j]=0.7
    return(a)

def rotate(obj,angle):
    """
    Will update later
    """
    if("shapes" in str(type(obj))):
        arr=obj.shapeMatrix
        if(obj.myShape=="CANVAS"):
            raise Exception("CANVAS cannot be rotated")
    arr = obj
    a=np.array(arr,dtype=str)
    a[a=='1']='r'
    l,b=np.shape(a)
    enlarge_factor = round((l**2+b**2)**0.5)*2
    r=np.zeros(  (  enlarge_factor  ,  enlarge_factor  )             ,dtype=str)
    r[(enlarge_factor//2)-(l//2):(enlarge_factor//2)+(l//2),(enlarge_factor//2)-(b//2):(enlarge_factor//2)+(b//2)]=a
    r[r=='']='0'
    r=arr2png(r,name_="")
    r=r.rotate(angle)
    r.save('./IMG/rotate.png')
    r=png2arr('./IMG/rotate.png')
    r=np.array(r,dtype=str)
    res=np.where(r=='r')
    top=min(res[1])
    bottom=max(res[1])
    right=max(res[0])
    left=min(res[0])
    rotated=r[left:right+1,top:bottom+1]
    rotated[rotated=='r']=1
    rotated = np.array(rotated,dtype=int)
    #rotated=arr2png(rotated,name_="")
    return(rotated.tolist())

def color(shape,color):
    arr=np.array(shape , dtype=str)
    arr[arr!='0']=color
    a=arr.tolist()
    for i,x in enumerate(a):
        for j,e in enumerate(x):
            if e=='0':
                a[i][j]=0
            if e=='1':
                a[i][j]=1
    return(a)

def outline_with_shape(shapemat,thick):
    if("shapes" in str(type(shapemat))):
        shapemat = shapemat.shapeMatrix
        thick = thick*sampl
    a=arr2png(shapemat)
    a.save("./IMG/a.png")
    x,y=a.size
    b=a.resize((x+2*thick+2,y+2*thick+2))
    b.save("./IMG/b.png")
    a=png2arr("./IMG/a.png")
    b=png2arr("./IMG/b.png")
    x,y=np.shape(np.array(a))
    j,k=np.shape(np.array(b))
    l=np.zeros((j+2,k+2),dtype=str)
    l[l=='']='0'
    l[ (j-x+2)//2 : x+((j-x+2)//2) ,(k-y+2)//2:y+((k-y+2)//2)]=a
    m=np.zeros((j+2,k+2),dtype=str)
    m[m=='']='0'
    m[1:j+1,1:k+1]=b
    b=arr2png(m)
    e=cv.Canny(np.array(b),1,50)
    e=im.fromarray(e)
    e.save('./IMG/e.png')
    e=np.array(png2arr('./IMG/e.png'),dtype=str)
    e[e=='0']='0.7'
    e[e=='1']='0'
    #arr2png(e).show()
    e[l=='1']='1'
    #arr2png(e).show()
    e.tolist()
    for i,x in enumerate(e):
        for j,k in enumerate(x):
            if k=='0':
                e[i][j]=0
            if k=='1':
                e[i][j]=1
            if k=='0.7':
                e[i][j]=0.7
    return(e)


def outline(shapemat,thick=0):
    r=outline_with_shape(shapemat,thick)
    r=np.array(r,dtype=str)
    r[r=='1']='0'
    r[r=='0.7']='1'
    #arr2png(r).show()
    r.tolist()
    for i,x in enumerate(r):
        for j,k in enumerate(x):
            if k=='0':
                r[i][j]=0
            if k=='1':
                r[i][j]=1
            if k=='0.7':
                r[i][j]=0.7
    return(r)

def free_surface_12(canvas_array):
    a=np.array(canvas_array,dtype=int)
    a1=np.array(canvas_array,dtype=str)
    l,b=np.shape(a)
    a_v=sum(a)
    a_h=sum(np.transpose(a))
    res1=np.where(a_v==0)
    res2=np.where(a_h==0)
    a1[:,res1]='b'
    a1[res2,:]='b'
    return(a1)

def free_surface_34(canvas_array):
    a=np.array(canvas_array,dtype=int)
    a1=np.array(canvas_array,dtype=str)
    k,o=np.shape(a)
    a_v=sum(a)
    a_h=sum(np.transpose(a))
    v=[5,10,20,30,40,50,60,70,80,90,100]
    s=np.zeros((101,101),int)
    for i in v:
        for j in v: 
            l1=np.array(np.where(a_h<(np.max(a_h)*i//100 )),dtype=int)
            b1=np.array(np.where(a_v<(np.max(a_v)*j//100)), dtype=int)
            l1.tolist()
            b1.tolist()
            top=l1[0][len(l1[0])*8//100] if l1!=[] else 0
            bottom=l1[0][len(l1[0])-len(l1[0])*8//100-1] if l1!=[] else k-1
            left=b1[0][len(b1[0])*8//100] if b1!=[] else 0
            right=b1[0][len(b1[0])-len(b1[0])*8//100-1]  if b1!=[] else o-1
            if np.sum(a[top:bottom+1,left:right+1])==0:
                l,b=np.shape(a[top:bottom+1,left:right+1])
                s[i][j]=l*b
    
    i,j=np.where(s==np.max(s))
    l1=np.array(np.where(a_h<(np.max(a_h)*i[0]//100 )),dtype=int)
    b1=np.array(np.where(a_v<(np.max(a_v)*j[0]//100)), dtype=int)
    top=l1[0][len(l1[0])*8//100]
    bottom=l1[0][len(l1[0])-len(l1[0])*8//100-1]
    left=b1[0][len(b1[0])*8//100]
    right=b1[0][len(b1[0])-len(b1[0])*8//100-1]
    a1[top:bottom+1,left:right+1]='b'
    return(a1)

def pieChart(li):
    li[0],li[2] = li[2],li[0]
    mylabels = ["Wastage","Re-usable","Shapes"]
    myexplode = [0, 0.2, 0]
    mycolors=['#b0bec5','#f50057','#0d47a1']
    plt.pie(li, labels = mylabels, explode = myexplode, colors=mycolors,startangle = 210,autopct='%1.0f%%')
    plt.title("Canvas Efficiency Chart")
    plt.show() 

def free_surface_area(canvas):
    a=np.array(canvas,str)
    w=len(np.where(a=='0')[0])
    b=len(np.where(a=='1')[0])
    bl=len(np.where(a=='b')[0])
    return([b,bl,w])