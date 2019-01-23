from Triangle import Triangle

class IsoscelesTriangle(Triangle):
    def __init__(self,leftBotton,baseLen,height,color,outlineC):
        points= [leftBotton]
        points.append((leftBotton[0]+baseLen,leftBotton[1]))
        points.append((leftBotton[0]+(baseLen/2),leftBotton[1]-height))
        print(points)
        super(IsoscelesTriangle,self).__init__(points,color,outlineC)
