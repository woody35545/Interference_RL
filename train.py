import env
import __init__
import time as t
runtime = 0

print(f"train.py")
myEnv = env.make("myENv")
myEnv.init_users()
state_dic = {}
state_number =  0

def state_indexing_in(_state):
    global state_number
    if state_dic.get(str(_state)) == None:
        state_dic[str(_state)] = state_number
        state_number+=1
    else:
        None

while True:
    print(f"Running time: {runtime}")
    myEnv.random_move_users()
    state = "" # 매 에피소드 마다 state 초기화
    #for i in range(len(myEnv.users)):
        #state += "("+str(myEnv.users[i].x)+","+str(myEnv.users[i].y)+")"
    #state_indexing_in(state)
    state = myEnv.get_current_state()
    myEnv.state_indexing_table_update(state)
    print(f"{myEnv.get_current_state()}")
    print(f"{myEnv.get_state_indexing_table()}")
    print("DEBUG " + myEnv.get_state_index(state))
    myEnv.print_users_location()
    t.sleep(1)
    runtime+=1