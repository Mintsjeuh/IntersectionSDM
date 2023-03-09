#11.1 Noord
#2.1 Oost
#5.1 Zuid
#8.1 West

from numpy import dot, array, empty_like
from matplotlib.path import Path


def make_path(x1, y1, x2, y2):
    return Path([[x1, y1], [x2, y2]])


def perp(a):
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return
def seg_intersect(a1, a2, b1, b2):
    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = perp(da)
    denom = dot(dap, db)
    num = dot(dap, dp)

    x3 = ((num / denom.astype(float)) * db + b1)[0]
    y3 = ((num / denom.astype(float)) * db + b1)[1]
    p1 = make_path(a1[0], a1[1], a2[0], a2[1])
    p2 = make_path(b1[0], b1[1], b2[0], b2[1])
    if p1.contains_point([x3, y3]) and p2.contains_point([x3, y3]):
        return x3, y3
    else:
        return False


a_start = array([0.0, 0.0])
a_end = array([5.0, 5.0])

b_start = array([0.0, 5.0])
b_end = array([5.0, 0.0])

#print(seg_intersect(a_start, a_end, b_start, b_end))
