class Win_Door:
    def __init__(self,x,y):
        self.square=x*y
class Room:
    def __init__(self,width,lenght,hight,wd):
        self.square=2*hight*(width+lenght)
        self.wd=[]
    def addWD(self,w,h):
        self.wd.append(Win_Door(w,h))
    def workSurface(self):
        new_square=self.square
        for i in self.wd:
            new_square-=i.square
        return new_square
    def roolons(self,rw,rl):
       roolon=rw*rl
       new_square=self.square
       for i in self.wd:
          new_square-=i.square
       roolon_needed=new_square/roolon
       return roolon_needed
        
r1=Room(6,3,2.7,0)
print(r1.square)
r1.addWD(1,1)
r1.addWD(1,1)
r1.addWD(1,2)
print(r1.workSurface())
print(r1.roolons(1,2))

