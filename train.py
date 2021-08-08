import env
import obj
import __init__
import time as t


u = obj.user()
u.set_name("u1")
print(f"train.py")

while True:

    u.random_move()
    u.print_location()
    t.sleep(1)