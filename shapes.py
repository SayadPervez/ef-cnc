from functions import *
import constants as const
from math import sin,cos,radians,pi
from visualization import arr2png
import time

class Square:
    '''
    Give side in milli-meter( mm ) and angle in degrees( ° )
    '''
    def __init__(self,side,angle=0):
        self.myShape="square"
        self.length = side
        self.surfaceArea = side*side
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
                if(pospl(point2,point3,currentPoint)==1):
                    newShapeFrameMatrix[i][j]=0
                if(pospl(point3,point4,currentPoint)==1):
                    newShapeFrameMatrix[i][j]=0

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
            self.shapeMatrix = [[1]*siu]*siu
            self.shapeFrameDimension = [siu,siu]       # shapeFrameDimension changes on tilting
        else:
            self.tilt(angle)

class Rectangle:
    '''
    Give length and height in milli-meter( mm ) and angle in degrees( ° )
    '''
    def __init__(self,length,height,angle=0):
        self.myShape="rectangle"
        self.length = length
        self.height = height
        self.angle = angle
        self.surfaceArea = length*height
        self.__generateShapeMatrix__(length,height,angle)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nSide Length \t: {self.length} mm\nSide Height \t: {self.height} mm\nShape Tilt \t: {self.angle} °\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

    def tilt(self,angle):
        '''
        Tilts the shape to the given angle
        '''
        angle = (radians(90)-radians(angle)) if (angle!=90) else radians(angle)
        sinFactorHeight = (sin(angle)*self.height)*const.sampl
        cosFactorHeight =(cos(angle)*self.height)*const.sampl
        sinFactorLength = (sin(angle)*self.length)*const.sampl
        cosFactorLength =(cos(angle)*self.length)*const.sampl
        dy = (sinFactorLength + cosFactorHeight)
        dx = (cosFactorLength + sinFactorHeight)
        self.shapeFrameDimension = [ int(round(dx)) , int(round(dy)) ]
        #print(self.shapeFrameDimension)
        ###################################################################
        
        point1 = [cosFactorLength,0]
        point2 = [self.shapeFrameDimension[0],-1*cosFactorHeight]
        point3 = [sinFactorHeight,-1*self.shapeFrameDimension[1]]
        point4 = [0,-1*sinFactorLength]
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
                if(pospl(point2,point3,currentPoint)==1):
                    newShapeFrameMatrix[i][j]=0
                if(pospl(point3,point4,currentPoint)==1):
                    newShapeFrameMatrix[i][j]=0

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
    
    def __generateShapeMatrix__(self,length,height,angle=0):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[self.length*const.sampl,self.height*const.sampl,self.angle,'dm,dm,°']     # only angle of dimension changes on tilting
        if(angle==0 or angle%180==0):
            liu = length*const.sampl # liu => length in micrometers (u kind of looks like Mu)
            hiu = height*const.sampl # hiu => height in micrometers (u kind of looks like Mu)
            self.shapeMatrix = [[1]*liu]*hiu
            self.shapeFrameDimension = [liu,hiu]        # shapeFrameDimension changes on tilting
        elif angle==90:
            self.__generateShapeMatrix__(height,length,0)
            self.angle=90
        else:
            self.tilt(angle)

class Circle:
    '''
    Give radius in milli-meter( mm )
    '''
    def __init__(self,radius):
        self.myShape="circle"
        self.radius = radius
        self.surfaceArea = pi*radius*radius
        self.__generateShapeMatrix__(radius)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nShape Radius \t: {self.radius} mm\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

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
    
    def isPointInCircle(self,ptX,ptY,radius):
        if( (ptX-radius)**2 + (ptY-radius)**2 <= radius**2 ):
            return(True)
        else:
            return(False)

    def __generateShapeMatrix__(self,radius):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[self.radius*const.sampl,'dm']     # only angle of dimension changes on tilting
        diu = 2*radius*const.sampl # diu => diameter in micrometers (u kind of looks like Mu)
        self.shapeFrameDimension = [diu,diu]        # shapeFrameDimension changes on tilting
        shapeSkeleton = [[0]*diu for _ in range(diu)]
        for i in range(diu):
            for j in range(diu):
                if(self.isPointInCircle(i,j,diu/2)):
                    shapeSkeleton[i][j]=1
        self.shapeMatrix=shapeSkeleton

class Cone:
    '''
    Give cone-height & cone-radius in milli-meter( mm )
    '''
    def __init__(self,cone_height,cone_radius):
        self.myShape="cone"
        self.cone_radius = round(cone_radius)
        self.cone_height = round(cone_height)
        self.slantHeight = round((cone_radius**2 + cone_height**2)**0.5)
        self.theta = 2*180*cone_radius/self.slantHeight
        self.surfaceArea = pi*(self.slantHeight**2)*self.theta/360
        #print('theta = ',self.theta)
        if(self.theta>=360):
            raise Exception("Illegal cone dimensions.")
            return(0)
        self.cone_type = 1 if self.theta<=180 else 2
        #print('Cone type : ',self.cone_type)
        self.__generateShapeMatrix__(self.slantHeight,self.cone_type)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nShape Radius \t: {self.radius} mm\nShape Height \t: {self.height} mm\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

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
    
    def isPointInCircle(self,ptX,ptY,radius):
        if( (ptX-radius)**2 + (ptY-(self.width*const.sampl/2))**2 <= radius**2 ):
            return(True)
        else:
            return(False)

    def __generateShapeMatrix__(self,radius,type):
        '''
        Generates 2D binary shape matrix
        '''
        riu = radius*const.sampl # riu => radius in micrometers (u kind of looks like Mu)
        # type 1 cone
        # here, radius and height are the same
        if(type==1):
            halfWidth = sin(radians(self.theta/2)) * self.slantHeight
            self.width = round(2 * halfWidth)
            hiu = riu # hiu => height in micrometers (u kind of looks like Mu)
            wiu = self.width*const.sampl # wiu => width in micrometers (u kind of looks like Mu)
            self.shapeFrameDimension = [wiu,hiu]        # shapeFrameDimension changes on tilting
            shapeSkeleton = [[0]*wiu for _ in range(hiu)]
            xh = round(((riu*riu) - (wiu/2)**2)**0.5)
            pointy = [wiu/2,-hiu]
            Intercept_1 = [0,-hiu+xh]
            Intercept_2 = [wiu,-hiu+xh]
            for i in range(hiu):
                for j in range(wiu):
                    currentPoint = [j,-i]
                    if(self.isPointInCircle(i,j,riu)):
                        shapeSkeleton[i][j]=1
                    if(pospl(pointy,Intercept_1,currentPoint)==1):
                        shapeSkeleton[i][j]=0
                    if(pospl(pointy,Intercept_2,currentPoint)==-1):
                        shapeSkeleton[i][j]=0
        else:
            # type 2 cone here
            dh = -1*cos(radians(self.theta/2))*riu
            h = riu
            wiu = round(2*riu)
            self.width = 2*radius
            hiu = round(h+dh) # actual height of the frame
            self.shapeFrameDimension = [wiu,hiu]        # shapeFrameDimension changes on tilting
            shapeSkeleton = [[0]*wiu for _ in range(hiu)]
            phi = 360-self.theta
            dw = round(riu*sin(radians(phi/2)))
            pointy = [wiu/2,-riu]
            Intercept_1 = [(wiu/2)-dw,-hiu]
            Intercept_2 = [(wiu/2)+dw,-hiu]
            for i in range(hiu):
                for j in range(wiu):
                    currentPoint = [j,-i]
                    if(self.isPointInCircle(i,j,riu)):
                        shapeSkeleton[i][j]=1
                    if(pospl(pointy,Intercept_1,currentPoint)==1 and pospl(pointy,Intercept_2,currentPoint)==-1):
                        shapeSkeleton[i][j]=0
        self.dimensions=[self.cone_height*const.sampl,self.cone_radius*const.sampl,'dm,dm']     # only angle of dimension changes on tilting
        self.shapeMatrix = shapeSkeleton

class Canvas:
    '''
    Give length and height in milli-meter( mm )
    '''
    def __init__(self,length,height):
        self.myShape="CANVAS"
        self.length = length
        self.height = height
        self.surfaceArea = length*height
        self.__generateShapeMatrix__(length,height)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nSide Length \t: {self.length} mm\nSide Height \t: {self.height} mm\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

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
    
    def __generateShapeMatrix__(self,length,height,angle=0):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[self.length*const.sampl,self.height*const.sampl,'dm,dm']
        liu = length*const.sampl # liu => length in micrometers (u kind of looks like Mu)
        hiu = height*const.sampl # hiu => height in micrometers (u kind of looks like Mu)
        self.shapeMatrix = [[0]*liu]*hiu
        self.shapeFrameDimension = [liu,hiu]        # shapeFrameDimension changes on tilting