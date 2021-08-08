import random as r

class user:
    def __init__(self):
        self.x=0
        self.y=0
        self.move_speed= 1
    def set_location(self,_x,_y):
        self.x=_x
        self.y=_y
    def get_x(self):
        return int(self.x)
    def set_x(self,_x):
        self.x=_x
    def get_y(self):
        return int(self.y)
    def set_y(self,_y):
        self.y=_y
    def get_move_speed(self):
        return self.move_speed
    def set_move_speed(self,_move_speed):
        self.move_speed=_move_speed
    def random_move(self): # testing Done
        move_ = r.randrange(0,4)
        if move_==0: # move UP, self.x + move_speed
            self.set_x(self.get_x()+self.get_move_speed())
        if move_==1: # move Down, self.x - move_speed
            self.set_x(self.get_x()-self.get_move_speed())
        if move_==2: # move Right, self.y + move_speed
            self.set_y(self.get_y()+self.get_move_speed())
        if move_==3: # move Left, self.y - move_speed
            self.set_y((self.get_y()-self.get_move_speed()))
class satelite:
    def __init__(self):
        self.x=0
        self.y=0
    def set_bounds(self,_width,_height):
        None # 구현 필요


