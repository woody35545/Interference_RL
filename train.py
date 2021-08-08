import env
import obj
import __init__
import time as t


u = obj.user()
print(f"train.py")

while True:

    u.random_move()
    print(u.get_x())
    t.sleep(1)