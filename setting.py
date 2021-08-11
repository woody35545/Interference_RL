min_x = -10
max_x = 10
min_y = -10
max_y = 10
range_x = max_x-min_x # x축 range
range_y = max_y-min_y # y축 range
map_size = range_x*range_y # map pixel


MAX_USER_SIZE=3
MAX_SATELITE_SIZE=2
MAX_STATE_SIZE=0 #수정 필요
MAX_ACTION_SIZE=7
Q_MAX_STATE= map_size**MAX_USER_SIZE
Q_MAX_ACTION= MAX_ACTION_SIZE**MAX_USER_SIZE
user_set=[""]*MAX_USER_SIZE
action_set=[""]*MAX_ACTION_SIZE # 수정필요
state_set=[""]*MAX_STATE_SIZE # 수정필요


def get_MAX_USER_SIZE():
    return int(MAX_USER_SIZE)
def get_MAX_SATELITE_SIZE():
    return int(MAX_SATELITE_SIZE)
def set_MAX_USER_SIZE(_size):
    global MAX_USER_SIZE
    MAX_USER_SIZE=int(_size)
def set_MAX_SATELITE_SIZE(_size):
    global MAX_SATELITE_SIZE
    MAX_SATELITE_SIZE=int(_size)
def get_MAX_ACTION_SIZE(_size):
    return MAX_ACTION_SIZE
def set_MAX_ACTION_SIZE(_size):
    global MAX_ACTION_SIZE
    MAX_ACTION_SIZE=int(_size)

