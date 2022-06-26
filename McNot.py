import numpy as np
def McNot(x,w,t):
    net = np.dot(x,w)
    if net>t:
        output = 1
    else:
        output = 0
    return output
x0 = np.array([0,1])
x3 = np.array([1,1])
w = np.array([-1,1])
t = 0
ans1 = McNot(x0,w,t)
print (x0, "value", ans1)
ans2 = McNot(x3,w,t)
print (x3, "value", ans2)
