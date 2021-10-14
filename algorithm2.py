import functions as func
import numpy as np

def fitting(canvas,shapeList,log_=False):
    cArray = np.array(canvas.shapeMatrix) #cArray => canvasArray
    cx,cy = np.shape(cArray)
    for shape in shapeList:
        sArray = shape.shapeMatrix
        sx,sy = np.shape(sArray)
        newCanvas = np.copy(cArray)
        for col in range(0,cy-sy):
            doublebreak=False
            for row in range(0,cx-sx):
                newCanvas = np.copy(cArray)
                newCanvas[row:row+sx,col:col+sy]+=sArray
                if(func.isInterfering(newCanvas)):
                    pass
                else:
                    doublebreak=True
                    break
            if(doublebreak==True):
                break
        cArray = np.copy(newCanvas)
        if(log_):
            print(f"Completed placing {shape.myShape}")
        
    ret = cArray.tolist()
    return(ret)

def run(canvas,shapeList,log_):
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
    return(fitting(canvas,shapeList,log_))