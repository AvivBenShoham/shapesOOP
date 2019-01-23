from Shape import Shape
import math
import tkinter
import time

class Polygon(Shape):

    def __init__(self, points, color,outlineC):
        super(Polygon, self).__init__(color,outlineC)
        self.points = points



#    def clacArea(self):
#        area = 0
 #       x = self.lines[len(self.lines)-1]
  #      for i in self.lines:

   #         area += (self.lines[i].getPoint1().getX())-self.line[i].getPoint2().getX)


    def calcArea(self):
        pass


    def changeDirection(self,canvas):
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        for x in self.points:
            if x[1] >= height:
                self.direction[0] = 'N'
            elif x[1] <= 0:
                self.direction[0] = 'S'
            if x[0] >= width:
                self.direction[1] = 'W'
            elif x[0] <= 0:
                self.direction[1] = 'E'


    def moveMe(self,canvas):
        while(self.animation==True):
           # canvas.create_polygon(self.points, fill = "white",outline = "white")
            lim = len(self.points)
            new_point_list = []
            for x in range(0,lim,1):
                self.changeDirection(canvas)

                if self.direction[1] == 'E':
                    if self.direction[0] == 'S':
                        new_point_list.append((self.points[x][0] + 3, self.points[x][1] + 3))
                    else:
                        new_point_list.append((self.points[x][0] + 3, self.points[x][1] - 3))
                else:
                    if self.direction[0] == 'S':
                        new_point_list.append((self.points[x][0] - 3, self.points[x][1] + 3))
                    else:
                        new_point_list.append((self.points[x][0] - 3, self.points[x][1] - 3))
            canvas.create_polygon(self.points, fill = "white",outline = "white")
            self.points = new_point_list
            canvas.create_polygon(self.points,fill = self.color,outline = self.outlineColor)
            time.sleep(1/60)
            #time.sleep(2)

    def drawMe(self,canvas):
        canvas.create_polygon(self.points,fill = self.color,outline = self.outlineColor)


    #returning the incline of x line (line number 1,2,3...)
    def getSlopeOfLine(self,x):
        if(x == len(self.points)):
            return ((self.points[0][1] - self.points[x-1][1]) / (self.points[0][0] - self.points[x - 1][0]))
        return ((self.points[x][1] - self.points[x-1][1]) / (self.points[x][0] - self.points[x- 1][0]))

    def sizeLine(self,x):
        if(x==len(self.points)):
            return math.sqrt((self.points[0][1]-self.points[x-1][1])**2+(self.points[0][0]-self.points[x-1][0])**2)
        return math.sqrt((self.points[x][1]-self.points[x-1][1])**2+(self.points[x][0]-self.points[x-1][0])**2)