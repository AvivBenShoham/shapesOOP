from decimal import Decimal

from Polygon import Polygon
import math


class Quad(Polygon):

    def __init__(self,points,color,outlineC):
        super(Quad,self).__init__(points,color,outlineC)



    def calcArea(self):
        a = self.sizeLine(1)
        b = self.sizeLine(2)
        diagonalLength = math.sqrt(((self.points[2][1]-self.points[0][1])**2)+ ((self.points[2][0]-self.points[0][0])**2))
        angle = math.acos(((a** 2) + (b ** 2) - (diagonalLength ** 2)) / (2 * a * b))
        x = Decimal(a * b * math.sin(angle))
        return round(x, 3)


    def getPointVar(self,numberOfPoint,xOry):
        return self.points[numberOfPoint][xOry]