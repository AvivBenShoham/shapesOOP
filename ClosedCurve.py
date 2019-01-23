from abc import abstractmethod

from Shape import Shape



class ClosedCurve(Shape):

    def __init__(self,color,outlineC):
        super(ClosedCurve, self).__init__(color,outlineC)

    def calcArea(self):
        pass

    def moveMe(self):
        pass

    @abstractmethod
    def drawMe(self,canvas):
        pass
