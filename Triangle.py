from decimal import Decimal

from Polygon import Polygon
import math

class Triangle(Polygon):

    def __init__(self,points,color,outlineC):
        super(Triangle,self).__init__(points,color,outlineC)


    def calcArea(self):
        a = self.sizeLine(1)
        b = self.sizeLine(2)
        c = self.sizeLine(3)
        angle = math.acos(((a ** 2) + (b ** 2) - (c ** 2))/(2 * a * b))
        x = Decimal(a * b * math.sin(angle) * 0.5)
        return round(x, 3)


