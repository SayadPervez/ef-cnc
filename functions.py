import numpy as np

# pospl -> POSition Point Line
def pospl(pt1,pt2,pt3):
    '''
    Returns the position of the point pt3 according to the line vector pt1->pt2\n
    right hand fold => 1\n
    left hand fold => -1\n
    same line      =>  0
    '''
    x1,y1=pt1
    x2,y2=pt2
    xA,yA=pt3

    v1 = (x2-x1, y2-y1)   # Vector 1
    v2 = (x2-xA, y2-yA)   # Vector 2
    xp = v1[0]*v2[1] - v1[1]*v2[0]

    if(xp > 0):
        return(-1)#print('left hand fold')
    elif(xp < 0):
        return(1)#print('right hand fold')
    else:
        return(0)#print('same line')

# evenize -> makes arrays even in size for rotation compatibility
def evenize(a2dlist):
    '''
    Input and output are 2D list.
    If number of rows or columns is not even, this function fixes it.
    Used to achieve bug free rotation
    '''
    i,j = len(a2dlist),len(a2dlist[0])
    if(i%2==0 and j%2==0):
        return(a2dlist)
    elif(i%2!=0):
        # if number of rows (height) is not even
        min_index = min([sum(_) for _ in a2dlist])
        del(a2dlist[min_index])
        return(a2dlist)
    else:
        # if number of cols (width) is not even
        a = a2dlist.copy()
        x = np.array(a).T.tolist()
        min_index = min([sum(_) for _ in x])
        del(x[min_index])
        x = np.array(x).T.tolist()
        return(x)

def singleFit(canvas,objectList):
    returnDict = {}
    if(type(objectList)!=type([])):
        objectList = [objectList]
    for obj in objectList :
        cl,cb = canvas.shapeFrameDimension
        chypotunes = (cl**2 + cb**2)**0.5
        ol,ob = obj.shapeFrameDimension
        if(ol > cl and ob > cb):
            returnDict[obj]=(False,False)
        elif (ol <= cl and ob <= cb):
            returnDict[obj]=(True,0)
        elif (ol <= cl and ob > cb and ob <= cl and ol <= cb) or (ol > cl and ob <= cb and ol <= cb and ob <= cl):
            returnDict[obj]=(True,90)
        elif (ol<=chypotunes and ob/cb*100<=15 and ol/chypotunes*100<=75) or (ob<=chypotunes and ol/cl*100<=15 and ob/chypotunes*100<=75):
            returnDict[obj]=(True,45)
        else:
            returnDict[obj]=(False,False)
    return(returnDict,objectList)

def fitAll(canvas,objectList):
    '''
    This is a theoretical calculation and can sometimes fail to give practical results
    '''
    if(type(objectList)!=type([])):
        objectList = [objectList]
    canvasArea = canvas.surfaceArea
    objectArea = sum([_.surfaceArea for _ in objectList])
    return(True if canvasArea >= objectArea else False)

def sortSurfaceArea(objectList):
    if(type(objectList)!=type([])):
        objectList = [objectList]
    ret = {}
    for obj in objectList:
        ret[obj] = obj.surfaceArea
    ret = dict(sorted(ret.items(),key = lambda item:item[1]))
    return(list(ret.keys())[::-1])