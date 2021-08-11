from obj import *
from setting import *
current_state = ""
current_action = ""
current_step = ""
state_indexing_table = {}

state_number=0
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


    def get_current_state(self):
        global current_state
        current_state = ""
        for i in range (get_MAX_USER_SIZE()):
            str_t = "("+str(self.users[i].get_x())+","+str(self.users[i].get_y())+")"
            current_state += str_t
        return current_state

    def state_indexing_table_update(self,_state):
        global state_indexing_table
        global state_number
        if state_indexing_table.get(str(_state)) == None:
            state_indexing_table[str(_state)] = int(state_number)
            state_number += 1
        else:
            None

    def get_state_indexing_table(self):
        return state_indexing_table

    def get_state_index(self,_state):
        return str(state_indexing_table[str(_state)])