import functions as func
import algorithm1

def run(canvas,shapeList,log_=False,constCompute=False):
    shapeList=func.triangleSort(shapeList)
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
    coneCount = func.countShapes(shapeList,'cone')
    ones = [(-1)**i for i in range(coneCount)]
    for q in range(coneCount):
        shapeList[q].flaTilt(ones[q])
    return(algorithm1.run(canvas,shapeList,log_,constCompute,noSort=True))