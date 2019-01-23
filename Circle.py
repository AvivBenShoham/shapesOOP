import math

from Shape import Shape
from ClosedCurve import ClosedCurve

import time
class Circle(ClosedCurve):

    def __init__(self,radios,center,color,outlineC): #center is the circle center
        super(Circle,self).__init__(color,outlineC)
        self.radios = radios
        self.center = center

    def drawMe(self,canvas):
        canvas.create_oval(self.center[0]-self.radios,self.center[1]+self.radios,self.center[0]+self.radios,self.center[1]-self.radios, fill = self.color,outline = self.outlineColor)

    def moveMe(self,canvas):
        while True:
            canvas.create_oval(self.center[0] - self.radios, self.center[1] + self.radios, self.center[0] + self.radios,
                               self.center[1] - self.radios, fill="white", outline="white")

            self.changeDirection(canvas)
            if self.direction[1] == 'E':
                if self.direction[0] == 'S':
                    self.center[0] = self.center[0]+3
                    self.center[1] = self.center[1]+3
                else:
                    self.center[0] = self.center[0]+3
                    self.center[1] = self.center[1]-3
            else:
                if self.direction[0] == 'S':
                    self.center[0] = self.center[0]-3
                    self.center[1] = self.center[1]+3
                else:
                    self.center[0] = self.center[0]-3
                    self.center[1] = self.center[1]-3

            canvas.create_oval(self.center[0] - self.radios, self.center[1] + self.radios, self.center[0] + self.radios,
                               self.center[1] - self.radios, fill=self.color, outline=self.outlineColor)

            time.sleep(1/30)

    def changeDirection(self,canvas):
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        if self.center[1]+self.radios >= height:
            self.direction[0] = 'N'
        elif self.center[1]-self.radios <= 0:
            self.direction[0] = 'S'
        if self.center[0]+self.radios >= width:
            self.direction[1] = 'W'
        elif self.center[0]-self.radios <= 0:
                self.direction[1] = 'E'




    def calcArea(self):
        return math.pi*self.radios*self.radios