import random as r
import time as t
import numpy as np
from rewards import *
max_user_size = 2
max_user_location = 12
max_action_size = 7
Q_x_size = max_user_location**max_user_size
Q_y_size = max_action_size**max_user_size
Q = np.full((Q_x_size,Q_y_size),0)
reward =0
max_reward = max_user_size
step = 1
episode= 1
state_indexing_table={}
action_indexing_table={}
state_num = 0
action_num = 0
current_state = ""
current_action = ""



class user:
    def __init__(self):
        self.loc = 0
        self.freq = 0
        self.move_speed= 1
    def set_freq(self,_freq):
        self.freq = _freq
    def random_init(self):
        self.loc = int(r.randrange(1,max_user_location+1))
    def random_move(self): # testing Done
        move_ = r.randrange(0,10)
        if move_==0 and self.loc <max_user_location+1: # move UP, self.x + move_speed
            self.loc += 1
        if move_==1 and self.loc > 1: # move Down, self.x - move_speed
            self.loc += -1
        else:
            None


users = [""]*max_user_size
for i in range(len(users)):
    users[i] = user()
    users[i].random_init()
def get_current_action():
    global current_action
    current_action = ""
    for i in range (max_user_size):
        current_action += str(users[i].freq)
    return str(current_action)
def action_indexing_table_update(_action):
    global action_indexing_table
    global action_num
    if action_indexing_table.get(str(_action)) == None:
        action_indexing_table[str(_action)] = int(action_num)
        action_num += 1
    else:
        None
def get_current_state():
    global current_state
    state_= ""
    for i in range (max_user_size):
        state_ += str(users[i].loc)
    current_state = state_
    return str(state_)
def get_action_index(_action):
    return int(action_indexing_table[str(_action)])
def state_indexing_table_update(_state):
    global state_indexing_table
    global state_num
    if state_indexing_table.get(str(_state)) == None:
        state_indexing_table[str(_state)] = int(state_num)
        state_num += 1
    else:
        None
def get_state_index(_state):
    return int(state_indexing_table[str(_state)])
def reset():
    None
def to_next_episode():
    global step,episode,reward
    for i in range(len(users)):
        users[i].random_init()
    state_indexing_table_update(get_current_state())
    print(state_indexing_table)
    reward = 0
    step = 1
    episode += 1
def to_next_step():
    global step
    for i in range(len(users)):
        users[i].random_move()
    step += 1
def rewarding(_user):
    reward_ = 0
    loc = _user.loc
    freq= _user.freq
    if loc == 1:
        reward_ = loc1_reward_table[freq]
    elif loc == 2:
        reward_ = loc2_reward_table[freq]
    elif loc == 3:
        reward_ = loc3_reward_table[freq]
    elif loc == 4:
        reward_ = loc4_reward_table[freq]
    elif loc == 5:
        reward_ = loc5_reward_table[freq]
    elif loc == 6:
        reward_ = loc6_reward_table[freq]
    elif loc == 7:
        reward_ = loc7_reward_table[freq]
    elif loc == 8:
        reward_ = loc8_reward_table[freq]
    elif loc == 9:
        reward_ = loc9_reward_table[freq]
    elif loc == 10:
        reward_ = loc10_reward_table[freq]
    elif loc == 11:
        reward_ = loc11_reward_table[freq]
    elif loc == 12:
        reward_ = loc12_reward_table[freq]


    return reward_
def argmax():
    current_state_index = get_state_index(get_current_state())
    armax_action_index = -1
    for i in range(Q_y_size):
        if armax_action_index <  Q[current_state_index,i]:
            armax_action_index = Q[current_state_index,i]
        elif:
            None
    return temp


def random_action():
    for i in range(len(users)):
        users[i].set_freq(r.randrange(1,max_action_size+1))
def update_Q():
    current_q_state_index = get_state_index(get_current_state())
    current_q_action_index = get_action_index(get_current_action())
    Q[current_q_state_index,current_q_action_index] += reward
    print(f"Q_UPDATE >> Q[{current_q_state_index,current_q_action_index}]={Q[current_q_state_index,current_q_action_index] } ")
while True:
    print(f"epi:{episode},step:{step}")
    current_state = get_current_state()
    state_indexing_table_update(current_state)
    random_action()
    action_indexing_table_update(get_current_action())
    reward = 0
    for i in range(len(users)):
        print(f"users[{i}] | .loc: {users[i].loc}, .freq: {users[i].freq}")
    for i in range(len(users)):
        reward += rewarding(users[i])
    update_Q()

    print(f"rewrad: {reward}")
    if current_action == current_state:

        to_next_episode()
    else:
        to_next_step()

    t.sleep(1)