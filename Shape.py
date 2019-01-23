from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    def __init__(self,color,outlineC):
        self.color = color
        self.outlineColor = outlineC
        self.animation = True
        self.direction = ["S","W"]

    @abstractmethod
    def drawMe(self,canvas):
        pass

    @abstractmethod
    def calcArea(self):
        pass

    @abstractmethod
    def moveMe(self,x,y):
        pass
        #for i in self.lines:
            #self.lines[i].moveLine(x,y)

    def setFillColor(self,color):
        self.color = color

    def animationOn(self):
        self.animation = True

    def animationOff(self):
        self.animation = False
