
def split_list(l, size):
    return [l[i:i+size] for i in range(0, len(l), size)]


def computeBusStops(id, x, y, n):
    n = len(x)/n
    X = split_list(x, n)
    Y = split_list(x, n)

    # should be re-written in a sense that we return x, y values
    res_x = [sum(i)/float(len(i)) for i in X]
    res_y = [sum(i)/float(len(i)) for i in Y]

    result = []
    for k, i in enumerate(res_x):
         print res_x[k], res_y[k]


id = [0,1,2,3,4,5,6,7,8,9]
x = [2.0,2.0,4.0,4.0,3.0,8.0,7.0,7.0,9.0,9.0]
y = [4.0,2.0,2.0,4.0,3.0,8.0,9.0,7.0,7.0,9.0]
n = 2
computeBusStops(id, x, y, n)
