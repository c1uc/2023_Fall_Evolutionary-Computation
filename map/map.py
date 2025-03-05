import numpy as np

a = np.zeros((46, 46))
rng = np.random.default_rng()


def fitness(x, y):
    val1 = 0.01 * (y - 30) * (y - 35) * (y - 40)
    fit1 = 8 * (10 < abs(x - val1) and abs(x - val1) < 15)

    val2 = 0.01 * (x - 30) * (x - 35) * (x - 40)
    fit2 = 8 * (10 < abs(y - val2) and abs(y - val2) < 15)

    fit3 = 1 * (rng.random() < 0.01)
    return np.clip(fit1 + fit2 + fit3, 0, 8)


for i in range(46):
    for j in range(46):
        a[i][j] = fitness(i, j)

np.savetxt('map.txt', a, fmt='%d', delimiter='')
