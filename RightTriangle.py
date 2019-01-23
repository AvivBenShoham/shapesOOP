from Triangle import Triangle

class RightTriangle(Triangle):
    def __init__(self,leftBotton,xDistanece,yDistance,color,outlineC):
        points = [leftBotton]
        points.append((leftBotton[0]+xDistanece,leftBotton[1]))
        points.append((leftBotton[0],leftBotton[1]-yDistance))
        print(points)
        super(RightTriangle,self).__init__(points,color,outlineC)
