from obj import *
from __init__ import *

class make:
    def __init__(self,_name):
        self.name= str(_name)
        self.users = user_set
        self.actions = action_set

    def init_users(self): # episode 마다 새로 initialize
        for i in range (MAX_USER_SIZE):
            self.users[i] = user()
            self.users[i].set_location(r.randrange(min_x,max_x+1),r.randrange(min_y,max_y+1))
    def random_move_users(self):
        for i in range(MAX_USER_SIZE):
            self.users[i].random_move()
    def print_users_location(self):
        for i in range(MAX_USER_SIZE):
            print(f"{i}: ({self.users[i].get_x()},{self.users[i].get_y()})")