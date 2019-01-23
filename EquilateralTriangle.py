from IsoscelesTriangle import IsoscelesTriangle
import math
from Triangle import Triangle
class EquilateralTriangle(Triangle):
    def __init__(self,leftBotton,baseLen,color,outlineC):
        points = [leftBotton]
        points.append((leftBotton[0]+baseLen,leftBotton[1]))
        points.append((leftBotton[0]+(baseLen/2),leftBotton[1]-(math.sqrt(3)*baseLen/2)))
        super(EquilateralTriangle,self).__init__(points,color,outlineC)
