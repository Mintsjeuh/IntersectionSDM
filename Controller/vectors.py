#11.1 Noord
#2.1 Oost
#5.1 Zuid
#8.1 West

from numpy import dot, array, empty_like
from matplotlib.path import Path


def make_path(x1,y1,x2,y2):
    return Path([[x1,y1],[x1,y2],[x2,y2],[x2,y1]])


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
    if(denom != 0):
        x3 = ((num / denom.astype(float)) * db + b1)[0]
        y3 = ((num / denom.astype(float)) * db + b1)[1]
        return x3, y3
    else:
        return False

north_west_path = [[3.0, 7.0], [3.0, 6.0], [1.0, 5.0], [0.0, 5.0]]
east_west_path = [[7.0, 5.0], [0.0, 5.0]]

for i in range(len(north_west_path)):
    if(i == len(north_west_path) - 1):
        break
    else:
        for j in range(len(east_west_path)):
            if(j == len(east_west_path) - 1):
                break
            else:
                intersect = seg_intersect(array(north_west_path[i]), array(north_west_path[i+1]), array(east_west_path[j]), array(east_west_path[j+1]))
                print(intersect)

#
# a_start = array([0.0, 0.0])
# a_end = array([5.0, 0.0])
#
# b_start = array([5.0, 0.0])
# b_end = array([0.0, 0.0])
#
# seg_intersect(a_start, a_end, b_start, b_end)
# print(seg_intersect(a_start, a_end, b_start, b_end))
