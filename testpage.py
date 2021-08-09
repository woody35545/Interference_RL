dic_a = {}
var = ""

x1 = 1
x2 = 3
y1 = 2
y2 = 5
def is_exist(_key):
    if dic_a.get(str(_key)):
        return True
    else:
        return False
def data_in(_key,_val):
    if is_exist(_key):
        dic_a[str(_key)] += int(_val)

    else:
        dic_a[str(_key)] = int(_val)

data_in("011201301",1)
data_in("b",4)
data_in("a",1)
print(dic_a)

is_exist("a")
is_exist("A")

