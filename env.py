from obj import *
from __init__ import *
user_set=[""]*get_MAX_USER_SIZE()
action_set=[""]*MAX_ACTION_SIZE # 수정필요
class env:
    def __init__(self):
        self.users = user_set
        self.actions = action_set