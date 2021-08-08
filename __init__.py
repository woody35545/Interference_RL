import numpy as np
import time as t
import random as r

MAX_USER_SIZE=2
MAX_SATELITE_SIZE=2
MAX_STATE_SIZE=0 #수정 필요
MAX_ACTION_SIZE=2

min_x = -10
max_x = 10
min_y = -10
max_y = 10
scale_size_x = max_x-min_x # x축 range
scale_size_y = max_y-min_y # y축 range
scale_size = scale_size_x*scale_size_y # map pixel 갯수
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

def state_indexing():
    #수정 필요
    None