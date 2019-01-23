from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,leftBottom,baseLen,color,outlineC):
        super(Square,self).__init__(leftBottom,baseLen,baseLen,color,outlineC)