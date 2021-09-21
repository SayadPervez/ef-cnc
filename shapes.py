from functions import *
import constants as const

class Square:
    '''
    Square(side,angle=0)    is the object creation statement
    Give side in milli-meter( mm ) and angle in degrees( ° )
    '''
    def __init__(self,side,angle=0):
        self.myShape="square"
        self.length = side
        self.tilt = angle
        self.generateShapeMatrix(side,angle)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nSide Length \t: {self.length} mm\nShape Tilt \t: {self.tilt} °\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        print(repr(self))

    def displayShape(self):
        '''
        Warning : CPU intensive task
        '''
        temp = ""
        for li in self.shapeMatrix:
            for num in li:
                temp+=str(num)
            temp+="\n"
        print(temp)
    
    def generateShapeMatrix(self,side,angle=0):
        siu = side*const.sampl # sim => side in micrometers (u kind of looks like Mu)
        self.shapeMatrix = [[1 for _ in range(siu)] for _ in range(siu)]
        self.shapeFrameDimension = [siu,siu]
