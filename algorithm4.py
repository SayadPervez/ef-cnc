import functions as func
import numpy as np
from math import ceil

def fitting(canvas,shapeList,log_=False,constCompute=False):
    cArray = np.array(canvas.shapeMatrix) #cArray => canvasArray
    cx,cy = np.shape(cArray)
    if(type(constCompute)==type(100)):
        pass
    elif(type(constCompute)==type(True) and constCompute==True):
        constCompute = 100
    else:
        constCompute = 1
    stepX = ceil(cx/constCompute)
    stepY = ceil(cy/constCompute)
    memoryX = 0
    memoryY = 0
    for shape in shapeList:
        sArray = shape.shapeMatrix
        sx,sy = np.shape(sArray)
        newCanvas = np.copy(cArray)
        isObjectPlaced=False
        for row in range(0,cx-sx,stepX):
            col=0
            if(row<memoryX and col<memoryY):
                continue
            newCanvas = np.copy(cArray)
            newCanvas[row:row+sx,col:col+sy]+=sArray
            if(func.isInterfering(newCanvas)):
                pass
            else:
                isObjectPlaced=True
                memoryX=row+(71/100*sx)
                memoryY=col+(71/100*sy)
                #print("choice 1")
                break
        if(isObjectPlaced==False):
            for col in range(0,cy-sy,stepY):
                row=0
                if(row<memoryX and col<memoryY):
                    continue
                newCanvas = np.copy(cArray)
                newCanvas[row:row+sx,col:col+sy]+=sArray
                if(func.isInterfering(newCanvas)):
                    pass
                else:
                    isObjectPlaced=True
                    memoryX=row+(71/100*sx)
                    memoryY=col+(71/100*sy)
                    #print("choice 2")
                    break
        if(isObjectPlaced==False):
            for row in range(0,cx-sx,stepX):
                col=cy-sy
                if(row<memoryX and col<memoryY):
                    continue
                newCanvas = np.copy(cArray)
                newCanvas[row:row+sx,col:col+sy]+=sArray
                if(func.isInterfering(newCanvas)):
                    pass
                else:
                    isObjectPlaced=True
                    memoryX=row+(71/100*sx)
                    memoryY=col+(71/100*sy)
                    #print("choice 3")
                    break
        if(isObjectPlaced==False):
            for col in range(0,cy-sy,stepY):
                row=cx-sx
                if(row<memoryX and col<memoryY):
                    continue
                newCanvas = np.copy(cArray)
                newCanvas[row:row+sx,col:col+sy]+=sArray
                if(func.isInterfering(newCanvas)):
                    pass
                else:
                    isObjectPlaced=True
                    memoryX=row+(71/100*sx)
                    memoryY=col+(71/100*sy)
                    #print("choice 4")
                    break
        if(isObjectPlaced==False):
            for col in range(0,cy-sy,stepY):
                doublebreak=False
                for row in range(0,cx-sx,stepX):
                    if(row<memoryX and col<memoryY):
                        continue
                    newCanvas = np.copy(cArray)
                    newCanvas[row:row+sx,col:col+sy]+=sArray
                    if(func.isInterfering(newCanvas)):
                        pass
                    else:
                        doublebreak=True
                        memoryX=row+(71/100*sx)
                        memoryY=col+(71/100*sy)
                        break
                if(doublebreak==True):
                    break
        cArray = np.copy(newCanvas)
        if(log_):
            print(f"Completed placing {shape.myShape}")
    ret = cArray.tolist()
    return(ret)

def run(canvas,shapeList,log_=False,constCompute=False):
    shapeList=func.sortSurfaceArea(shapeList)
    d,_=func.singleFit(canvas,shapeList)
    l1 = [d[_][0] for _ in d]
    if(all(l1)==False):
        tooLarge=[]
        for _ in shapeList:
            if(d[_.uid][0]==False):
                tooLarge.append((_.uid,_.myShape,_.dimensions))
        raise Exception(f"{tooLarge} shapes are too large to fit the given canvas...")
    # If program passes till here, 
    # All the given shapes can individually fit in the given canvas.
    if(func.fitAll(canvas,shapeList)==False):
        raise Exception(f"Fitting all shapes in the given canvas is mathematically impossible.")
    # If program passes till here,
    # All the given shapes can be theoretically arranged in the canvas. Practically, I doubt it
    #print(d)
    return(fitting(canvas,shapeList,log_,constCompute))