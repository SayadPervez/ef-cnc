from functions import *
import constants as const

class Square:
    '''
    Give side in milli-meter( mm ) and angle in degrees( ° )
    '''
    def __init__(self,side,angle=0):
        self.myShape="square"
        self.length = side
        self.tilt = angle
        self.__generateShapeMatrix__(side,angle)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nSide Length \t: {self.length} mm\nShape Tilt \t: {self.tilt} °\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

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
        self.shapeFrameDimension = [siu,siu]
