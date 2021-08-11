from __init__ import *
action_indexing_table = {}
action_number = 0
class agent:
    def __init__(self):
        self. name = None
        self.env = ""
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