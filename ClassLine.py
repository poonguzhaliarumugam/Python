
class Line:
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2
    def distance(self):
        x1,y1=self.c1
        x2,y2=self.c2
        return ((x2-x1)**2+(y2-y1)**2)**0.5
    def slope(self):
        x1,y1=self.c1
        x2,y2=self.c2
        return (y2-y1)/(x2-x1)  

coor1=(3,2)
coor2=(8,10)
li=Line(coor1,coor2)
print(li.distance())
print(li.slope())
     