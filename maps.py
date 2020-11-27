import matplotlib.pyplot as plt
import numpy as np


def simulate(x,r, iteration): # x[n+1] = f(x[n]) = rx[n](1 − x[n])
    pop_size=[]
    while(iteration!=0):
        pop_size.append(x)
        x = x*r*(1-x)
        iteration -= 1
    return pop_size

def get_diff(obs1, obs2):
    difference = []
    zip_object = zip(obs1, obs2)
    for list1_i, list2_i in zip_object:
        difference.append(list1_i-list2_i)
    return difference

# observation1= simulate(0.2, 2, 500)
# observation2= simulate(0.200001, 2, 500)

# observation1= simulate(0.2, 3.4, 500)
# observation2= simulate(0.200001, 3.4, 500)

# observation1= simulate(0.2, 3.72, 500000)
# observation2= simulate(0.200001, 3.72, 500000)
#
# diff = get_diff(observation1,observation2)
# diff = list(map(abs, diff))
# print(sum(diff)/500000)
# plt.plot(diff ,  'o', color='red')
# plt.show()

def bifurcation_diagram(r_min, r_max, x_init, r_step):
    bifurcation_y = []
    bifurcation_x = []
    r_step = 1/r_step
    for i in range(int(r_step*(r_max - r_min))):
        r= r_min + i / r_step
        x=simulate(x_init,r,1000)
        x=findBasinOfAttarction(x)
        for i in x:
            bifurcation_x.append(r)
            bifurcation_y.append(i)
    plt.scatter(bifurcation_x,bifurcation_y, marker=",", s=0.02)
    plt.savefig('bifurcation.png', dpi=600)

def findBasinOfAttarction(x):
    x=x[500:]
    x = list(set(np.around(x, 2)))
    return x

bifurcation_diagram(2.8, 3.6, 0.2, 0.00001)