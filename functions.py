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