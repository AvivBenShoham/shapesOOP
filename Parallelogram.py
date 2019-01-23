from Quad import Quad
import math

class Parallelogram(Quad):
    def __init__(self,leftBottom,leftAngle,baseLen,height,color,outlineC):
        angle = math.radians(leftAngle)
        points = [leftBottom]
        points.append((leftBottom[0]+baseLen,leftBottom[1]))
        x = leftBottom[0]+baseLen+height/math.tan(angle)
        y = leftBottom[1]-height
        point = (leftBottom[0]+height/math.tan(angle),leftBottom[1]-height)
        points.append((x,y))
        points.append(point)


        super(Parallelogram,self).__init__(points,color,outlineC)