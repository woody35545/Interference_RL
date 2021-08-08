import env
import __init__
import time as t
runtime = 0

print(f"train.py")
myEnv = env.make("myENv")
myEnv.init_users()
while True:
    print(f"Running time: {runtime}")
    myEnv.random_move_users()
    myEnv.print_users_location()
    t.sleep(1)
    runtime+=1