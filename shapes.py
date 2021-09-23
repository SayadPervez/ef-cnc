from functions import *
import constants as const
from math import sin,cos,radians
from visualization import arr2png

class Square:
    '''
    Give side in milli-meter( mm ) and angle in degrees( ° )
    '''
    def __init__(self,side,angle=0):
        self.myShape="square"
        self.length = side
        self.angle = angle
        self.__generateShapeMatrix__(side,angle)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nSide Length \t: {self.length} mm\nShape Tilt \t: {self.angle} °\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

    def tilt(self,angle):
        '''
        Tilts the shape to the given angle
        '''
        angle = radians(angle)
        sinFactor = (sin(angle)*self.length)*const.sampl
        cosFactor=(cos(angle)*self.length)*const.sampl
        dy = ( sinFactor + cosFactor )
        dx = dy
        self.shapeFrameDimension = [ int(round(dx)) , int(round(dy)) ]
        #print(self.shapeFrameDimension)
        ###################################################################
        point1 = [sinFactor,0]
        point2 = [self.shapeFrameDimension[0],-1*sinFactor]
        point3 = [cosFactor,-1*self.shapeFrameDimension[1]]
        point4 = [0,-1*cosFactor]
        #edge 1 -> point 4 through 1
        newShapeFrameMatrix=[]
        for i in range(self.shapeFrameDimension[0]):
            temp = []
            for j in range(self.shapeFrameDimension[1]):
                currentPoint = [i,-1*j]
                if(pospl(point4,point1,currentPoint)==1):
                    temp.append(0)
                else:
                    temp.append(1)
            newShapeFrameMatrix.append(temp)
        #edge 2 -> point 1 through 2
        for i in range(self.shapeFrameDimension[0]):
            for j in range(self.shapeFrameDimension[1]):
                currentPoint = [i,-1*j]
                if(pospl(point1,point2,currentPoint)==1):
                    newShapeFrameMatrix[i][j]=0
                else:
                    pass
        #edge 3 -> point 2 through 3
        for i in range(self.shapeFrameDimension[0]):
            for j in range(self.shapeFrameDimension[1]):
                currentPoint = [i,-1*j]
                if(pospl(point2,point3,currentPoint)==1):
                    newShapeFrameMatrix[i][j]=0
                else:
                    pass
        #edge 4 -> point 3 through 4
        for i in range(self.shapeFrameDimension[0]):
            for j in range(self.shapeFrameDimension[1]):
                currentPoint = [i,-1*j]
                if(pospl(point3,point4,currentPoint)==1):
                    newShapeFrameMatrix[i][j]=0
                else:
                    pass
        self.shapeMatrix = newShapeFrameMatrix

    def printShape(self):
        '''
        Prints shape to console in binary 

        #### Warning : CPU intensive task
        '''
        temp = ""
        for li in self.shapeMatrix:
            for num in li:
                temp+=str(num)
            temp+="\n"
        print(temp)

    def displayShape(self):
        '''
        Displays shape as a image
        '''
        (arr2png(self.shapeMatrix)).show()
    
    def __generateShapeMatrix__(self,side,angle=0):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[self.length*const.sampl,self.angle,'dm,°']     # only angle of dimension changes on tilting
        if(angle==0 or angle%90==0):
            siu = side*const.sampl # sim => side in micrometers (u kind of looks like Mu)
            self.shapeMatrix = [[1 for _ in range(siu)] for _ in range(siu)]
            self.shapeFrameDimension = [siu,siu]        # shapeFrameDimension changes on tilting
        else:
            self.tilt(angle)

