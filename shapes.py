from functions import *
import constants as const
from math import sin,cos,radians

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
        Tilts the shape
        '''
        angle = radians(angle)
        dy = ((sin(angle)*self.length) + (cos(angle)*self.length))*const.sampl
        dx = dy
        self.shapeFrameDimension = [ int(round(dx)) , int(round(dy)) ]

    def displayShape(self):
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
    
    def __generateShapeMatrix__(self,side,angle=0):
        '''
        Generates 2D binary shape matrix
        '''
        siu = side*const.sampl # sim => side in micrometers (u kind of looks like Mu)
        self.shapeMatrix = [[1 for _ in range(siu)] for _ in range(siu)]
        self.shapeFrameDimension = [siu,siu]        # shapeFrameDimension changes on tilting
        self.dimensions=[self.length*const.sampl,self.angle,'dm,°']     # only angle of dimension changes on tilting
