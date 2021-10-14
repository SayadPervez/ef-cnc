import functions as func
import numpy as np

def fitting(canvas,shapeList):
    cArray = np.array(canvas.shapeMatrix) #cArray => canvasArray
    cx,cy = np.shape(cArray)
    for shape in shapeList:
        sArray = shape.shapeMatrix
        sx,sy = np.shape(sArray)
        row,col=0,0
        for row in range(0,cx-sx):
            doublebreak=False
            for col in range(0,cy-sy):
                newCanvas = cArray
                newCanvas[row:row+sx,col:col+sy]+=sArray
                if(np.count_nonzero(newCanvas>2)==0):
                    newCanvas = cArray
                else:
                    doublebreak=True
                    break
            if(doublebreak==True):
                break
    return(newCanvas.tolist())
        
            
                


def run(canvas,shapeList):
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
    return(fitting(canvas,shapeList))