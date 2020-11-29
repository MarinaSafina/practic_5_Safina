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
