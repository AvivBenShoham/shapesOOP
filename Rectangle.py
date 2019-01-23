from Quad import Quad

class Rectangle(Quad):
    def __init__(self,leftBottom,baseLen,sideLen,color,outlineC):
        points = [leftBottom]
        points.append((leftBottom[0]+baseLen,leftBottom[1]))
        points.append((leftBottom[0]+baseLen,leftBottom[1]+sideLen))
        points.append((leftBottom[0],leftBottom[1]+sideLen))


        super(Rectangle,self).__init__(points,color,outlineC)