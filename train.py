from __init__ import *
from agent import *
runtime = 0

print(f"train.py")

## AGENT IMPLEMENTS ##


myEnv.init_users()
myAgent = agent()

## AGENT_IMPLEPENTS ##
while True:
    print(f"Running time: {runtime}")
    state = "" # 매 에피소드 마다 state 초기화

    myEnv.random_move_users()
    state = myEnv.get_current_state()
    myAgent.do_action()
    myAgent.action_indexing_table_update(myAgent.get_current_action())
    myEnv.state_indexing_table_update(state)
    print(action_indexing_table)

    print(f"{myEnv.get_current_state()}") # temp #
    print(f"{myEnv.get_state_indexing_table()}") # temp #
    print("DEBUG " + myEnv.get_state_index(state))
    myEnv.print_users_location()
    t.sleep(10)
    runtime+=1