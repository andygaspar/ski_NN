import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import copy

A = np.array([0, 0])
B = np.array([1, 1])
C = np.array([0, 2])
D = np.array([1, 3])
gates = np.array([A, B, C, D]).astype(float)
g = 9.81

def init_control(gates):
    P = gates[0].copy()
    P[1] += float(gates[0][1]+gates[1][1])/8
    x = [P[0],P[1]]
    P = gates[1].copy()
    P[1] -= float(np.abs(gates[0][1] - gates[1][1]))/8
    x += [P[0], P[1]]
    for i in range(1,len(gates)-1):
        P = gates[i+1].copy()
        P[1] -= float(np.abs(gates[i+1][1] - gates[i][1]) )/ 8
        x += [P[0], P[1]]
    return np.array(x)

x = init_control(gates)



def time(x, start, end, v_0=0):
    par_1_x = x[0]
    par_1_y = x[1]
    par_2_x = x[2]
    par_2_y = x[3]
    P_1 = np.array([par_1_x, par_1_y])
    P_2 = np.array([par_2_x, par_2_y])
    TJ = lambda k: start * (1 - k) ** 3 + 3 * P_1 * (1 - k) ** 2 * k + 3 * P_2 * (1 - k) * k ** 2 + end * k ** 3

    tj_x = lambda k: start[0] * (-3 * (1 - k) ** 2) + P_1[0] * 3 * (1 - 4 * k + 3 * k ** 2) + \
                     P_2[0] * 3 * (2 * k - 3 * k ** 2) + end[0] * (3 * k ** 2)
    tj_y = lambda k: start[1] * (-3 * (1 - k) ** 2) + P_1[1] * 3 * (1 - 4 * k + 3 * k ** 2) + \
                     P_2[1] * 3 * (2 * k - 3 * k ** 2) + end[1] * (3 * k ** 2)
    length = lambda k: np.sqrt(tj_x(k) ** 2 + tj_y(k) ** 2)
    v = lambda k: np.sqrt(2 * g * TJ(k)[1] + v_0 ** 2 - 2 * g * TJ(0)[1])
    T = lambda k: length(k) / (v_0 + v(k))
    return quad(T, 0, 1)[0], v(1)


def best_tj(x, gates):
    x_ = copy.deepcopy(x[:4])
    v = 0
    t, v = time(x_, gates[0], gates[1], v)

    for i in range(1,len(gates)-1):
        P = x[i * 2 :i * 2 + 2]
        P = 2 * gates[i].copy() - P
        x_ = [P[0], P[1]]
        x_ += list(x[(i + 1) * 2:(i + 1) * 2+2])
        t_, v = time(x_, gates[i], gates[i+1], v)
        t += t_
    return t


def trajectory(start, end, params):
    c_1_x = params[0]
    c_1_y = params[1]
    c_2_x = params[2]
    c_2_y = params[3]
    P_1 = np.array([c_1_x, c_1_y])
    P_2 = np.array([c_2_x, c_2_y])
    TJ = lambda k: start * (1 - k) ** 3 + 3 * P_1 * (1 - k) ** 2 * k + 3 * P_2 * (1 - k) * k ** 2 + end * k ** 3
    tj = np.array([TJ(i) for i in np.arange(0, 1.1, 0.1)])
    return tj[:, 0], -tj[:, 1]


def full_tj(x, gates):
    x_ = x[:4]
    control = [np.array(x[:2])]
    control += [np.array(x[2:4])]
    xx, yy = trajectory(gates[0], gates[1], x_)

    for i in range(1,len(gates)-1):
        P = x[i * 2:i * 2 + 2]
        P = 2 * gates[i].copy() - P
        x_ = [P[0], P[1]]
        control += [np.array(P)]
        x_ += list(x[(i + 1) * 2:(i + 1) * 2 + 2])
        control += [np.array(x[(i + 1) * 2:(i + 1) * 2 + 2])]
        xx_, yy_ = trajectory(gates[i], gates[i+1], x_)
        xx = np.append(xx, xx_)
        yy = np.append(yy, yy_)
    return xx, yy, np.array(control)


def constraint1(x, gates):
    der_2 = start * (-3 * (1 - k) ** 2) + P_1[0] * 3 * (1 - 4 * k + 3 * k ** 2) + P_2[0] * 3 * (2 * k - 3 * k ** 2) + end[0] * (3 * k ** 2)
    return

# optimize
# b = (1.0,5.0)
# bnds = (b, b, b, b)
con1 = {'type': 'ineq', 'fun': constraint1}
# con2 = {'type': 'eq', 'fun': constraint2}
# cons = ([con1,con2])
solution = minimize(best_tj, x, args=(gates), method='SLSQP')
# solution = minimize(time,x0,method='SLSQP',\
#                     bounds=bnds,constraints=cons)
sol = solution.x

# xx, yy = trajectory(gates[0], gates[1], sol[:4])
# plt.plot(xx, yy)
# xxx, yyy = trajectory(gates[1], gates[2], sol[4:])
xxx, yyy, control = full_tj(sol, gates)
print(control)
plt.plot(control[:,0], -control[:,1], 'ro')
plt.plot(xxx, yyy)
plt.show()