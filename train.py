from __init__ import *
import env
runtime = 0

print(f"train.py")
myEnv = env.make("myENv")
myEnv.init_users()
state_dic = {}
state_number =  0
action_indexing_table = {}
action_number = 0
## AGENT IMPLEMENTS ##
class agent:
    def __init__(self):
        self. name = None
        self.current_action = ""
    def action_indexing_table_update(self, _action):
        global action_indexing_table
        global action_number
        if action_indexing_table.get(str(_action)) == None:
            action_indexing_table[str(_action)] = int(action_number)
            action_number += 1
        else:
            None
    def get_current_action(self):
        self.current_action = ""
        for i in range (MAX_USER_SIZE):
            self.current_action += str(myEnv.users[i].freq,)
        print(self.current_action)
        return str(self.current_action)
    def do_action(self):
        for i in range(MAX_USER_SIZE):
            myEnv.users[i].set_freq(r.randrange(0, 5))
            print(f"f_do_action TEST: {i}: {myEnv.users[i].freq}")
## AGENT_IMPLEPENTS ##
myAgent = agent()
while True:
    print(f"Running time: {runtime}")
    state = "" # 매 에피소드 마다 state 초기화

    myEnv.random_move_users()
    state = myEnv.get_current_state()
    myAgent.do_action()
    myAgent.action_indexing_table_update(myAgent.get_current_action())
    myEnv.state_indexing_table_update(state)
    print(action_indexing_table)

    #print(f"{myEnv.get_current_state()}") # temp #
    #print(f"{myEnv.get_state_indexing_table()}") # temp #
    #print("DEBUG " + myEnv.get_state_index(state))
    #myEnv.print_users_location()
    t.sleep(1)
    runtime+=1